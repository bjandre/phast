#!/usr/bin/env python

import unittest
from phast.fortran_2003 import fortran_2003Parser

class phast_module(unittest.TestCase):
    """unittest suite for phast's ability to process fortran 2003 modules
    """

    def setUp(self):
        self.whitespace = " \t"
        self.startrule = "module"
        self.parser = fortran_2003Parser(parseinfo=False, ignorecase=True, trace_length=512)
        self.text = None
        self.ast = None
        self.test_dir = "module"

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

    def test_0001(self):
        filename = "{0}/t0001_minimal_module.F03".format(self.test_dir)
        ast = self.generate_ast(filename)
        self.assertIsNotNone(ast)

    def test_0002(self):
        filename = "{0}/t0002_minimal_module_comments.F03".format(self.test_dir)
        ast = self.generate_ast(filename)
        self.assertIsNotNone(ast, msg=ast.__repr__())

    def test_0003(self):
        """
        """
        filename = "{0}/t0003_module_param.F03".format(self.test_dir)
        ast = self.generate_ast(filename)
        self.assertIsNotNone(ast)

    def test_0004(self):
        """
        """
        filename = "{0}/t0004_module_use.F03".format(self.test_dir)
        ast = self.generate_ast(filename)
        self.assertIsNotNone(ast)

    def test_0005(self):
        """
        """
        filename = "{0}/t0005_module_implicit_none.F03".format(self.test_dir)
        ast = self.generate_ast(filename)
        self.assertIsNotNone(ast)

    def test_0006(self):
        """
        """
        filename = "{0}/t0006_module_dummy_args.F03".format(self.test_dir)
        ast = self.generate_ast(filename)
        self.assertIsNotNone(ast)

    def test_0007(self):
        """Test that the generate_ast function returns none when the parser fails.
        """
        filename = "{0}/t0007_minimal_module_fail.F03".format(self.test_dir)
        self.assertRaises(Exception, self.generate_ast, filename)

    def test_module_call_dummy_args(self):
        filename = "{0}/module_call_dummy_args.F03".format(self.test_dir)
        ast = self.generate_ast(filename)
        self.assertIsNotNone(ast)
 
    def test_module_call_function(self):
        filename = "{0}/module_call_function.F03".format(self.test_dir)
        ast = self.generate_ast(filename)
        self.assertIsNotNone(ast)

# NOTE(bja, 2015-02) these are invalid tests for subprogram, need to be moved to module
#    def test_module_call_function_call_procedure(self):
#        filename = "{0}/module_call_function_call_procedure.F03".format(self.test_dir)
#        ast = self.generate_ast(filename)
#        self.assertIsNotNone(ast)



if __name__ == "__main__":
    unittest.main()
