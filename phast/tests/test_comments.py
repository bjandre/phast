#!/usr/bin/env python

import unittest

from phast.tests.test_phast_base import TestPhastBase


class TestPhastComments(TestPhastBase):
    """unittest suite for phast's ability to process fortran 2003
    comments. section 3.3.1.1 of the fortran standard.

    NOTE(bja, 201503) comments must include a newline. blank lines are
    considered comments.

    """

    def setUp(self):
        super(TestPhastComments, self).setUp()
        self.startrule = "comment"
        self.test_dir = "phast/tests"

    def tearDown(self):
        super(TestPhastComments, self).tearDown()

    def test_comment_blank_line(self):
        code_str = """
"""
        self.check_source(name='comment_blank_line',
                          compilable=False,
                          valid_src=True,
                          code_str=code_str)
        
    def test_comment_blank_lines(self):
        code_str = """


"""
        self.check_source(name='comment_blank_lines',
                          compilable=False,
                          valid_src=True,
                          code_str=code_str)
        
    def test_comment_empty(self):
        code_str = """!
"""
        self.check_source(name='comment_empty',
                          compilable=False,
                          valid_src=True,
                          code_str=code_str)
        
    def test_comment(self):
        code_str = """! this is a comment
"""
        self.check_source(name='comment',
                          compilable=False,
                          valid_src=True,
                          code_str=code_str)
        
    def test_comment_leading_whitespace(self):
        code_str = """           ! this is a comment
"""
        self.check_source(name='comment_leading_whitespace',
                          compilable=False,
                          valid_src=True,
                          code_str=code_str)
        
    def test_comment_leading_blank_lines(self):
        code_str = """


           ! this is a comment
"""
        self.check_source(name='comment_leading_blank_lines',
                          compilable=False,
                          valid_src=True,
                          code_str=code_str)
        
    def test_comment_trailing_blank_lines(self):
        code_str = """
           ! this is a comment


"""
        self.check_source(name='comment_trailing_blank_lines',
                          compilable=False,
                          valid_src=True,
                          code_str=code_str)
        
    def test_comment_block(self):
        code_str = """
    ! this is a comment
    ! this is another comment
    ! stil another
"""
        self.check_source(name='comment_block',
                          compilable=False,
                          valid_src=True,
                          code_str=code_str)
        
    def test_comment_special_char_arrow(self):
        code_str = """! this is a comment with an => in it.
"""
        self.check_source(name='comment_special_char_arrow',
                          compilable=False,
                          valid_src=True,
                          code_str=code_str)

    def test_comment_special_char_colon_colon(self):
        code_str = """! this is a comment with an :: in it.
"""
        self.check_source(name='comment_special_char_colon_colon',
                          compilable=False,
                          valid_src=True,
                          code_str=code_str)

    def test_comment_special_char_paren_slash(self):
        code_str = """! this is a comment with an (/ in it.
"""
        self.check_source(name='comment_special_char_paren_slash',
                          compilable=False,
                          valid_src=True,
                          code_str=code_str)


    def test_comment_special_char_slash_paren(self):
        code_str = """! this is a comment with an /) in it.
"""
        self.check_source(name='comment_special_char_slash_paren',
                          compilable=False,
                          valid_src=True,
                          code_str=code_str)


    def test_comment_special_char_semicolon(self):
        code_str = """! this is a comment with ; in it.
"""
        self.check_source(name='comment_special_char_semicolon',
                          compilable=False,
                          valid_src=True,
                          code_str=code_str)





if __name__ == "__main__":
    unittest.main()
    print(unittest.TestResult.unexpectedSuccess)
