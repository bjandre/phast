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
        self.test_dir = "subprogram"

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

    def test_subprogram_comment_special_chars(self):
        filename = "{0}/subprogram_comment_special_chars.F03".format(self.test_dir)
        ast = self.generate_ast(filename)
        self.assertIsNotNone(ast, msg=ast.__repr__())

    def test_subprogram_initialization_expression(self):
        filename = "{0}/subprogram_initialization_expression.F03".format(self.test_dir)
        ast = self.generate_ast(filename)
        self.assertIsNotNone(ast, msg=ast.__repr__())

    def test_subprogram_parameter(self):
        filename = "{0}/subprogram_initialization_expression.F03".format(self.test_dir)
        ast = self.generate_ast(filename)
        self.assertIsNotNone(ast, msg=ast.__repr__())

    def test_subprogram_assignment_statement(self):
        filename = "{0}/subprogram_assignment_statement.F03".format(self.test_dir)
        ast = self.generate_ast(filename)
        self.assertIsNotNone(ast, msg=ast.__repr__())

    def test_subprogram_implicit_none_assignment(self):
        filename = "{0}/subprogram_implicit_none_assignment.F03".format(self.test_dir)
        ast = self.generate_ast(filename)
        self.assertIsNotNone(ast, msg=ast.__repr__())

    def test_subprogram_implicit_none_assignment_comments(self):
        filename = "{0}/subprogram_implicit_none_assignment_comments.F03".format(self.test_dir)
        ast = self.generate_ast(filename)
        self.assertIsNotNone(ast, msg=ast.__repr__())

    def test_subprogram_dummy_args(self):
        filename = "{0}/subprogram_dummy_args.F03".format(self.test_dir)
        ast = self.generate_ast(filename)
        self.assertIsNotNone(ast)

    def test_subprogram_3statements(self):
        filename = "{0}/subprogram_3statements.F03".format(self.test_dir)
        ast = self.generate_ast(filename)
        self.assertIsNotNone(ast)

    def test_subprogram_function(self):
        filename = "{0}/subprogram_function.F03".format(self.test_dir)
        ast = self.generate_ast(filename)
        self.assertIsNotNone(ast)
 
    def test_subprogram_if(self):
        filename = "{0}/subprogram_if.F03".format(self.test_dir)
        ast = self.generate_ast(filename)
        self.assertIsNotNone(ast)
 
    def test_subprogram_if_then(self):
        filename = "{0}/subprogram_if_then.F03".format(self.test_dir)
        ast = self.generate_ast(filename)
        self.assertIsNotNone(ast)
 
    def test_subprogram_if_logical_and(self):
        filename = "{0}/subprogram_if_logical_and.F03".format(self.test_dir)
        ast = self.generate_ast(filename)
        self.assertIsNotNone(ast)
 
    def test_subprogram_if_nested(self):
        filename = "{0}/subprogram_if_nested.F03".format(self.test_dir)
        ast = self.generate_ast(filename)
        self.assertIsNotNone(ast)
 
    def test_subprogram_if_elseif_else(self):
        filename = "{0}/subprogram_if_elseif_else.F03".format(self.test_dir)
        ast = self.generate_ast(filename)
        self.assertIsNotNone(ast)
 
    def test_subprogram_if_named(self):
        filename = "{0}/subprogram_if_named.F03".format(self.test_dir)
        ast = self.generate_ast(filename)
        self.assertIsNotNone(ast)
 

if __name__ == "__main__":
    unittest.main()
