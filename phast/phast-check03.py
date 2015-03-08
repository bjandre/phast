#!/usr/bin/env python
"""Python program to test if a fortran 2003 file can be paresd by the
grako based parser.

Based on example driver included in grako parsers.

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

import argparse
import json
import os
import traceback

if sys.version_info[0] == 2:
    from ConfigParser import SafeConfigParser as config_parser
else:
    from configparser import ConfigParser as config_parser


from phast.fortran_2003 import fortran_2003Parser
from phast.fortran_2003_semantics import Fortran2003SemanticActions
from phast.phast_utils import PhastWriter

    
# -------------------------------------------------------------------------------
#
# User input
#
# -------------------------------------------------------------------------------

def commandline_options():
    """Process the command line arguments.

    """
    parser = argparse.ArgumentParser(
        description='simple parser for grako based fortran 2003 parser.')

    parser.add_argument('--backtrace', action='store_true',
                        help='show exception backtraces as extra debugging '
                        'output')

    parser.add_argument('--debug', action='store_true',
                        help='extra debugging output')

    parser.add_argument('-l', '--list', action=ListRules, nargs=0,
                        help="list all rules and exit")

    parser.add_argument('-t', '--trace', action='store_true',
                        help="output trace information")
    
    parser.add_argument('file', metavar="FILE", help="the input file to parse")

    parser.add_argument('startrule', metavar="STARTRULE",
                        help="the start rule for parsing")

    options = parser.parse_args()
    return options


# -------------------------------------------------------------------------------
#
# FIXME: work functions
#
# -------------------------------------------------------------------------------
class ListRules(argparse.Action):
    """Class to print rules from a grako parser.
    """

    def __call__(self, parser, namespace, values, option_string):
        print('Rules:')
        for r in fortran_2003Parser.rule_list():
            print(r)
        print()
        sys.exit(0)



# -------------------------------------------------------------------------------
#
# main
#
# -------------------------------------------------------------------------------

def main(options):
    whitespace = ""

    with open(options.file) as f:
        text = f.read()
    parser = fortran_2003Parser(parseinfo=True, ignorecase=True, trace_length=512)
    print("--> parser.trace_length = {0}".format(parser.trace_length))
    semantic_actions = Fortran2003SemanticActions()
    ast = parser.parse(
        text,
        options.startrule,
        filename=options.file,
        trace=options.trace,
        semantics=semantic_actions,
        whitespace=whitespace,
        nameguard=False)
    print('AST:')
    print(ast)
    print()
    print('JSON:')
    print(json.dumps(ast, indent=2))
    print()
    print("source: ")
    #phast_writer = PhastWriter("{0}.tmp".format(options.file))
    phast_writer = PhastWriter()
    phast_writer.write(ast)
    phast_writer.close()


if __name__ == "__main__":
    options = commandline_options()
    try:
        status = main(options)
        sys.exit(status)
    except Exception as error:
        print(str(error))
        if options.backtrace:
            traceback.print_exc()
        sys.exit(1)
