#!/usr/bin/env python

import unittest
from phast.fortran_2003 import fortran_2003Parser

class phast_module(unittest.TestCase):
    """unittest suite for phast's ability to process fortran 2003 modules
    """

    def setUp(self):
        self.whitespace = " \t"
        self.startrule = "external_subprogram"
        self.parser = fortran_2003Parser(parseinfo=False, ignorecase=True, trace_length=512)
        self.text = None
        self.ast = None
        self.test_dir = "subroutine"

    def tearDown(self):
        pass

    def generate_ast(self, filename):
        #import os.path
        #self.assertTrue(os.path.exists(filename))
        ast = None
        try:
            with open(filename) as f:
                self.text = f.read()
        except Exception:
            pass
        else:
            ast = self.parser.parse(self.text, self.startrule, filename, whitespace=self.whitespace)
        return ast

    def test_bad_filename(self):
        """Test that the generate_ast function returns None for a bad filename
        """
        filename = "bad-filename"
        ast = self.generate_ast(filename)
        self.assertIsNone(ast)

    def test_0008(self):
        filename = "{0}/t0008_subroutine_dummy_args.F03".format(self.test_dir)
        ast = self.generate_ast(filename)
        self.assertIsNotNone(ast)

    def test_0009(self):
        filename = "{0}/t0009_subroutine_expression.F03".format(self.test_dir)
        ast = self.generate_ast(filename)
        self.assertIsNotNone(ast, msg=ast.__repr__())



if __name__ == "__main__":
    unittest.main()
