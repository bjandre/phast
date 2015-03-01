#!/usr/bin/env python
"""Python class containing the semantic actions for the grako based fortran 2003 parser.

Author: Ben Andre <bjande@gmail.com>

Copyright (C) 2014-2015 Benjamin Andre

This Source Code Form is subject to the terms of the Mozilla Public
License, v.2.0. If a copy of the MPL was not distributed with this
file, you can obtain one at http://mozilla.org/MPL/2.0/

"""

from __future__ import print_function

import sys

if sys.hexversion < 0x02070000:
    print(70 * "*")
    print("ERROR: {0} requires python >= 2.7.x. ".format(sys.argv[0]))
    print("It appears that you are running python {0}".format(
        ".".join(str(x) for x in sys.version_info[0:3])))
    print(70 * "*")
    sys.exit(1)

from collections import OrderedDict
import os
import traceback

import grako

# -------------------------------------------------------------------------------
#
# FIXME: work functions
#
# -------------------------------------------------------------------------------
class Fortran2003SemanticActions(object):
    """
    """

    def __init__(self):
        pass

    def _default(self, ast, *args, **kwargs):
        """default action
        """
        return ast

    # -------------------------------------------------------------------------
    #
    # generic functions to convert an ast into a a string
    #
    # -------------------------------------------------------------------------
    def _ast_to_str(self, ast):
        """
        """
        ast_str = u''
        if type(ast) == list:
            ast_str += self._ast_list_to_str(ast)
        elif type(ast) == dict:
            ast_str += self._ast_dict_to_str(ast)
        elif type(ast) == str:
            ast_str += u'{0}'.format(ast)
        elif type(ast) == unicode:
            ast_str += ast
        elif type(ast) == grako.contexts.Closure:
            if len(ast) > 0:
                ast_str += self._ast_list_to_str(ast)
        else:
            raise RuntimeError("Unknown AST element type '{0}' for: {1}".format(type(ast), ast))
        return ast_str

    def _ast_list_to_str(self, ast):
        """
        """
        ast_str = u''
        for e in ast:
            ast_str += self._ast_to_str(e)
        return ast_str

    def _ast_dict_to_str(self, ast):
        """
        """
        ast_str = u''
        for e in ast:
            ast_str += self._ast_to_str(ast[e])
        return ast_str

    
    # -------------------------------------------------------------------------
    #
    # semantic actions for grammar rules
    #
    # -------------------------------------------------------------------------
    def name(self, ast):
        """R304 : C301
        join the name object back into a single string instead of an array
        of characters.

        """
        c301 = 'C301 - max name length is 64 characters'
        max_length = 64
        ast_str = self._ast_to_str(ast)
        if len(ast_str) > max_length:
            raise RuntimeError("R304 - name : {0} : len(name) == {1}.".format(c301, len(ast_str)))
        return ast_str

    def ws_opt(self, ast):
        """join the whitespace, spaces and tabs, back into a single string.
        """
        ws = u''.join(ast)
        return ws

    def ws_req(self, ast):
        """join the whitespace, spaces and tabs, back into a single string.
        """
        ws = u''.join(ast)
        return ws

    def comment_text(self, ast):
        """join all the comment text back into a single string
        """
        comment_str = self._ast_to_str(ast)
        
        return comment_str

    def comment(self, ast):
        """
        """
        comment_group = []
        for c in ast['comment']:
            if len(c) > 0:
                comment_group.append(c)
        return comment_group

    def continuation(self, ast):
        """Continuation is a closure, and will return an empty list for the
        ast if it doesn't match, so we return an empty string instead.

        """
        if len(ast) == 0:
            return u''
        else:
            return ast

    def kind_param(self, ast):
        """
        """
        return ast

    def kind_constant(self, ast):
        """
        """
        kind_const = {'kind_constant': u''.join(ast)}
        return kind_const
        
    def sign(self, ast):
        """
        """
        s = u''.join(ast)
        return(s)
        
    def digit_string(self, ast):
        """join individual digits into a string
        """
        digit_str = self._ast_to_str(ast)
        return digit_str

    def signed_digit_string(self, ast):
        """
        """
        signed_digit_str = self._ast_to_str(ast)
        return signed_digit_str
    
    def significand(self, ast):
        """convert the significand into a single unified string
        """
        sig = {'significand': u''.join(ast)}
        return sig

    def exponent_letter(self, ast):
        el = {'exponent_letter': ast}
        return el

    def exponent(self, ast):
        exp = {'exponent': ast}
        return exp
    
    def real_literal_constant(self, ast):
        """convert real literal constant into a single string, enforce rule
        constraints.

        R417 : C411 - if both kind_constant and exponent_letter,
        exponent letter shall be 'E'

        """
        c411 = ("C411 - if both kind_constant and expenent_letter are "
                "specified, exponent_letter shall be 'e'.")
        exponent_letter = None
        kind_constant = None
        for e in ast:
            if type(e) == dict:
                if 'exponent_letter' in e:
                    exponent_letter = e['exponent_letter']
                elif 'kind_constant' in e:
                    kind_constant = e['kind_constant']
        if exponent_letter and kind_constant:
            if exponent_letter.lower() != u'e':
                raise RuntimeError(
                    "R417 real_literal_constant : {0}".format(c411))

        ast_str = self._ast_to_str(ast)    
        return ast_str

    
if __name__ == "__main__":
    try:
        sys.exit(0)
    except Exception as error:
        print(str(error))
        traceback.print_exc()
        sys.exit(1)
