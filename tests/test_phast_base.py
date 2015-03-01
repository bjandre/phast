#!/usr/bin/env python

import hashlib
import os
import unittest

from phast.fortran_2003 import fortran_2003Parser
from phast.fortran_2003_semantics import Fortran2003SemanticActions
from phast.phast_utils import PhastWriter

class TestPhastBase(unittest.TestCase):
    """unittest suite for phast's ability to process fortran 2003 modules
    """

    def setUp(self):
        self.whitespace = ""
        self.nameguard = False
        self.semantic_actions = Fortran2003SemanticActions()
        self.parser = fortran_2003Parser(parseinfo=True,
                                         ignorecase=True,
                                         trace_length=512)
        self.text = None
        self.ast = None
        self.startrule = None
        self.test_dir = None

    def tearDown(self):
        pass

    def _generate_ast(self, filename):
        #import os.path
        #self.assertTrue(os.path.exists(filename))
        ast = None
        try:
            with open(filename) as f:
                self.text = f.read()
        except Exception:
            pass
        else:
            ast = self.parser.parse(self.text, self.startrule, filename,
                                    semantics=self.semantic_actions,
                                    whitespace=self.whitespace,
                                    nameguard=self.nameguard)
        return ast

    def _hash_file(self, filename):
        h = hashlib.sha256()
        with open(filename, 'r') as src:
            for s in src.readlines():
                h.update(s)
        return h.digest()
    
    def _write_ast(self, filename, ast):
        hash_orig = self._hash_file(filename)
        tmp = "{0}.tmp".format(filename)
        phast_writer = PhastWriter(tmp)
        phast_writer.write(ast)
        phast_writer.close()
        hash_new = self._hash_file(tmp)
        self.assertEqual(hash_orig, hash_new)
        if hash_orig == hash_new:
            os.remove(tmp)

    def generate_write(self, filename):
        filename = "{0}/{1}".format(self.test_dir, filename)
        ast = self._generate_ast(filename)
        self.assertIsNotNone(ast, msg=ast.__repr__())
        #self._write_ast(filename, ast)

    
    def test_bad_filename(self):
        """Test that the generate_ast function returns None for a bad filename
        """
        filename = "bad-filename"
        ast = self._generate_ast(filename)
        self.assertIsNone(ast)

    def test_not_f03(self):
        c_file = u"""#include <stdio.h>
int main(int argc, char** argv) {
   printf("Hello, world!\\n");
   return 0;
}
"""
        filename = "tmp.c"
        with open(filename, 'w') as tmp_c:
            tmp_c.write(c_file)
        self.assertRaises(Exception, self._generate_ast, filename)

if __name__ == "__main__":
    unittest.main()
