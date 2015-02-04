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

    def test_subroutine_comment_special_chars(self):
        filename = "{0}/subroutine_comment_special_chars.F03".format(self.test_dir)
        ast = self.generate_ast(filename)
        self.assertIsNotNone(ast, msg=ast.__repr__())

    def test_subroutine_initialization_expression(self):
        filename = "{0}/subroutine_initialization_expression.F03".format(self.test_dir)
        ast = self.generate_ast(filename)
        self.assertIsNotNone(ast, msg=ast.__repr__())

    def test_subroutine_parameter(self):
        filename = "{0}/subroutine_initialization_expression.F03".format(self.test_dir)
        ast = self.generate_ast(filename)
        self.assertIsNotNone(ast, msg=ast.__repr__())

    def test_subroutine_assignment_statement(self):
        filename = "{0}/subroutine_assignment_statement.F03".format(self.test_dir)
        ast = self.generate_ast(filename)
        self.assertIsNotNone(ast, msg=ast.__repr__())

    def test_subroutine_implicit_none_assignment(self):
        filename = "{0}/subroutine_implicit_none_assignment.F03".format(self.test_dir)
        ast = self.generate_ast(filename)
        self.assertIsNotNone(ast, msg=ast.__repr__())

    def test_subroutine_implicit_none_assignment_comments(self):
        filename = "{0}/subroutine_implicit_none_assignment_comments.F03".format(self.test_dir)
        ast = self.generate_ast(filename)
        self.assertIsNotNone(ast, msg=ast.__repr__())

    def test_subroutine_dummy_args(self):
        filename = "{0}/subroutine_dummy_args.F03".format(self.test_dir)
        ast = self.generate_ast(filename)
        self.assertIsNotNone(ast)

    def test_subroutine_3statements(self):
        filename = "{0}/subroutine_3statements.F03".format(self.test_dir)
        ast = self.generate_ast(filename)
        self.assertIsNotNone(ast)

#    def test_subroutine_function(self):
#        filename = "{0}/subroutine_function.F03".format(self.test_dir)
#        ast = self.generate_ast(filename)
#        self.assertIsNotNone(ast)
#
# NOTE(bja, 2015-02) these are invalid tests for subroutine, need to be moved to module
#    def test_subroutine_call_function(self):
#        filename = "{0}/subroutine_call_function.F03".format(self.test_dir)
#        ast = self.generate_ast(filename)
#        self.assertIsNotNone(ast)
#
#    def test_subroutine_call_dummy_args(self):
#        filename = "{0}/subroutine_call_dummy_args.F03".format(self.test_dir)
#        ast = self.generate_ast(filename)
#        self.assertIsNotNone(ast)
#
#    def test_subroutine_call_function_call_procedure(self):
#        filename = "{0}/subroutine_call_function_call_procedure.F03".format(self.test_dir)
#        ast = self.generate_ast(filename)
#        self.assertIsNotNone(ast)



if __name__ == "__main__":
    unittest.main()
