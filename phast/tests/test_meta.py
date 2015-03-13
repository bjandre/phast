#!/usr/bin/env python

import unittest

from phast.tests.test_phast_base import TestPhastBase


class TestPhastMeta(TestPhastBase):
    """unit test suite for the test code in the TestPhastBase class.

    """

    def setUp(self):
        super(TestPhastMeta, self).setUp()
        self.startrule = "program"
        self.test_dir = "phast/tests"

    def tearDown(self):
        super(TestPhastMeta, self).tearDown()

    def test_bad_filename(self):
        """Test that the generate_ast function returns None for a bad filename
        """
        filename = "bad-filename"
        self.assertRaises(IOError, self._generate_ast_from_file, filename)

    def test_not_f03(self):
        code_src = u"""#include <stdio.h>
int main(int argc, char** argv) {
   printf("Hello, world!\\n");
   return 0;
}
"""
        self.check_source(name='not_f03',
                          compilable=True, valid_src=False,
                          code_str=code_src)


if __name__ == "__main__":
    unittest.main()
    print(unittest.TestResult.unexpectedSuccess)
