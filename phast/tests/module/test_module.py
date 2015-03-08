#!/usr/bin/env python

import unittest

from phast.tests.test_phast_base import TestPhastBase


class TestPhastModule(TestPhastBase):
    """unittest suite for phast's ability to process fortran 2003 modules
    """

    def setUp(self):
        super(TestPhastModule, self).setUp()
        self.startrule = "module"
        self.test_dir = "phast/tests/module"

    def tearDown(self):
        super(TestPhastModule, self).tearDown()

    def test_0001(self):
        filename = "t0001_minimal_module.F03"
        self.generate_write(filename)

    def test_0002(self):
        filename = "t0002_minimal_module_comments.F03"
        self.generate_write(filename)

    def test_0003(self):
        """
        """
        filename = "t0003_module_param.F03"
        self.generate_write(filename)

    def test_0004(self):
        """
        """
        filename = "t0004_module_use.F03"
        self.generate_write(filename)

    def test_0005(self):
        """
        """
        filename = "t0005_module_implicit_none.F03"
        self.generate_write(filename)

    def test_0006(self):
        """
        """
        filename = "t0006_module_dummy_args.F03"
        self.generate_write(filename)

    def test_0007(self):
        """
        """
        filename = "t0007_minimal_module_fail.F03"
        ast = self._generate_ast(filename)
        self.assertIsNone(ast)

    def test_module_call_dummy_args(self):
        filename = "module_call_dummy_args.F03"
        self.generate_write(filename)

    def test_module_call_arg_array_derived_type(self):
        filename = "module_call_arg_array_derived_type.F03"
        self.generate_write(filename)

    def test_module_call_function(self):
        filename = "module_call_function.F03"
        self.generate_write(filename)

    def test_module_call_procedure(self):
        filename = "module_call_procedure.F03"
        self.generate_write(filename)


if __name__ == "__main__":
    unittest.main()
    print(unittest.TestResult.unexpectedSuccess)
