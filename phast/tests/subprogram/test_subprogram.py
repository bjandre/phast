#!/usr/bin/env python

import unittest

from phast.tests.test_phast_base import TestPhastBase


class TestPhastSubprogram(TestPhastBase):
    """unittest suite for phast's ability to process fortran 2003 modules
    """

    def setUp(self):
        super(TestPhastSubprogram, self).setUp()
        self.startrule = "external_subprogram"
        self.test_dir = "phast/tests/subprogram"

    def tearDown(self):
        super(TestPhastSubprogram, self).tearDown()


    def test_subprogram_empty_subroutine(self):
        filename = "subprogram_empty_subroutine.F03"
        self.generate_write(filename)

    def test_subprogram_empty_subroutine_paren(self):
        filename = "subprogram_empty_subroutine_paren.F03"
        self.generate_write(filename)

    def test_subprogram_empty_subroutine_whitespace_paren(self):
        filename = "subprogram_empty_subroutine_whitespace_paren.F03"
        self.generate_write(filename)

    def test_subprogram_empty_function_paren(self):
        filename = "subprogram_empty_function_paren.F03"
        self.generate_write(filename)

    def test_subprogram_empty_function_whitespace_paren(self):
        filename = "subprogram_empty_function_whitespace_paren.F03"
        self.generate_write(filename)

    def test_subprogram_empty_function_paren_result(self):
        filename = "subprogram_empty_function_paren_result.F03"
        self.generate_write(filename)

    def test_subprogram_empty_function_whitespace_paren_whitespace_result(self):
        filename = "subprogram_empty_function_whitespace_paren_whitespace_result.F03"
        self.generate_write(filename)

    def test_subprogram_comment_special_chars(self):
        filename = "subprogram_comment_special_chars.F03"
        self.generate_write(filename)

    def test_subprogram_intrinsic_types(self):
        filename = "subprogram_intrinsic_types.F03"
        self.generate_write(filename)

    def test_subprogram_intrinsic_types_kinds(self):
        filename = "subprogram_intrinsic_types_kinds.F03"
        self.generate_write(filename)

    def test_subprogram_array(self):
        filename = "subprogram_array.F03"
        self.generate_write(filename)

    def test_subprogram_derived_type(self):
        filename = "subprogram_derived_type.F03"
        self.generate_write(filename)

    def test_subprogram_function(self):
        filename = "subprogram_function.F03"
        self.generate_write(filename)

    def test_subprogram_initialization_expression(self):
        filename = "subprogram_initialization_expression.F03"
        self.generate_write(filename)

    def test_subprogram_parameter(self):
        filename = "subprogram_initialization_expression.F03"
        self.generate_write(filename)

    def test_subprogram_assignment_statement(self):
        filename = "subprogram_assignment_statement.F03"
        self.generate_write(filename)

    def test_subprogram_assignment_logical(self):
        filename = "subprogram_assignment_logical.F03"
        self.generate_write(filename)

    def test_subprogram_real_literal_constant(self):
        filename = "subprogram_real_literal_constant.F03"
        self.generate_write(filename)

    def test_subprogram_assign_string_literal(self):
        filename = "subprogram_assign_string_literal.F03"
        self.generate_write(filename)

    def test_subprogram_implicit_none(self):
        filename = "subprogram_implicit_none.F03"
        self.generate_write(filename)

    def test_subprogram_implicit_none_assignment(self):
        filename = "subprogram_implicit_none_assignment.F03"
        self.generate_write(filename)

    def test_subprogram_implicit_none_assignment_comments(self):
        filename = "subprogram_implicit_none_assignment_comments.F03"
        self.generate_write(filename)

    def test_subprogram_dummy_args(self):
        filename = "subprogram_dummy_args.F03"
        self.generate_write(filename)

    def test_subprogram_3statements(self):
        filename = "subprogram_3statements.F03"
        self.generate_write(filename)

    def test_subprogram_if(self):
        filename = "subprogram_if.F03"
        self.generate_write(filename)

    def test_subprogram_if_then(self):
        filename = "subprogram_if_then.F03"
        self.generate_write(filename)

    def test_subprogram_if_logical_and(self):
        filename = "subprogram_if_logical_and.F03"
        self.generate_write(filename)

    def test_subprogram_if_logical_paren(self):
        filename = "subprogram_if_logical_paren.F03"
        self.generate_write(filename)

    def test_subprogram_if_nested(self):
        filename = "subprogram_if_nested.F03"
        self.generate_write(filename)

    def test_subprogram_if_elseif_else(self):
        filename = "subprogram_if_elseif_else.F03"
        self.generate_write(filename)

    def test_subprogram_if_named(self):
        filename = "subprogram_if_named.F03"
        self.generate_write(filename)

    def test_subprogram_relational_op(self):
        filename = "subprogram_relational_op.F03"
        self.generate_write(filename)

    def test_subprogram_logical_op(self):
        filename = "subprogram_logical_op.F03"
        self.generate_write(filename)

    def test_subprogram_equivalence_op(self):
        filename = "subprogram_equivalence_op.F03"
        self.generate_write(filename)

    def test_subprogram_paren_expression(self):
        filename = "subprogram_paren_expression.F03"
        self.generate_write(filename)

    def test_subprogram_do_loop(self):
        filename = "subprogram_do_loop.F03"
        self.generate_write(filename)

    def test_subprogram_labeled_stmt(self):
        filename = "subprogram_labeled_stmt.F03"
        self.generate_write(filename)

    def test_subprogram_write(self):
        filename = "subprogram_write.F03"
        self.generate_write(filename)

    def test_subprogram_format_stmt(self):
        filename = "subprogram_format_stmt.F03"
        self.generate_write(filename)

    def test_subprogram_cpp_predefined(self):
        filename = "subprogram_cpp_predefined.F03"
        self.generate_write(filename)


if __name__ == "__main__":
    unittest.main()
