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

import os
import traceback


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

    def name(self, ast):
        """join the name object back into a single string instead of an array
        of characters.

        """
        name_str = u'{0}{1}'.format(ast[0], "".join(ast[1]))
        return name_str

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
        comment_str = u'{0}{1}'.format(ast[0], ''.join(ast[1]))
        
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
            return ""
        else:
            return ast
    

if __name__ == "__main__":
    try:
        sys.exit(0)
    except Exception as error:
        print(str(error))
        traceback.print_exc()
        sys.exit(1)
