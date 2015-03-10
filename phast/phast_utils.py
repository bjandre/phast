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
# Writing utilities
#
# -------------------------------------------------------------------------------
class PhastWriter(object):
    """
    """

    def __init__(self, filename=None):
        self._filename = filename
        if self._filename is not None:
            self._file = open(self._filename, 'w')
        else:
            self._file = sys.stdout

    def __del__(self):
        if self._filename is not None:
            self._file.close()
        
    def write(self, ast):
        """
        """
        for a in ast:
            if type(a) == type(u''):
                print(a, file=self._file, end='')
            else:
                self.write(a)
    

# -------------------------------------------------------------------------------
#
# Whitespace utilities
#
# -------------------------------------------------------------------------------

if __name__ == "__main__":
    try:
        sys.exit(0)
    except Exception as error:
        print(str(error))
        traceback.print_exc()
        sys.exit(1)
