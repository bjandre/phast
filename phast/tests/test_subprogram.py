#!/usr/bin/env python

import unittest

from phast.tests.test_phast_base import TestPhastBase


class TestPhastSubprogram(TestPhastBase):
    """unittest suite for phast's ability to process fortran 2003
    subprograms

    """

    def setUp(self):
        super(TestPhastSubprogram, self).setUp()
        self.startrule = "external_subprogram"
        self.test_dir = "phast/tests"

    def tearDown(self):
        super(TestPhastSubprogram, self).tearDown()


    def test_subprogram_empty_subroutine(self):
        code_str = """subroutine foo_empty_subroutine
  
end subroutine foo_empty_subroutine

"""
        self.check_source(name='subprogram_empty_subroutine', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_empty_subroutine_paren(self):
        code_str="""subroutine foo_empty_subroutine_paren()
  
end subroutine

"""
        self.check_source(name='subprogram_empty_subroutine_paren', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_empty_subroutine_whitespace_paren(self):
        code_str = """subroutine foo_empty_subroutine_whitespace_paren ()
  
end subroutine foo_empty_subroutine_whitespace_paren

"""
        self.check_source(name='subprogram_empty_subroutine_whitespace_paren', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_empty_function_paren(self):
        code_str = """function foo_empty_function_paren()
  
end function
"""
        self.check_source(name='subprogram_empty_function_paren', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_empty_function_whitespace_paren(self):
        code_str = """function foo_empty_function_whitespace_paren ()
  
end function foo_empty_function_whitespace_paren

"""
        self.check_source(name='subprogram_empty_function_whitespace_paren', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_empty_function_paren_result(self):
        code_str = """function foo_empty_function_paren_result()result(foo)
  
end function foo_empty_function_paren_result

"""
        self.check_source(name='subprogram_empty_function_paren_result', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_empty_function_whitespace_paren_whitespace_result(self):
        code_str = """function foo_empty_function_ws_paren_ws_result () result (foo)
  
end function foo_empty_function_ws_paren_ws_result

"""
        self.check_source(name='subprogram_empty_function_whitespace_paren_whitespace_result', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_intrinsic_types(self):
        code_str = """subroutine foo_intrinsic_types
  ! some function
  character :: a
  character :: aa, aaa
  complex :: b
  double precision :: c
  integer :: d
  logical :: e
  real :: f
end subroutine foo_intrinsic_types

"""
        self.check_source(name='subprogram_intrinsic_types', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_intrinsic_types_kinds(self):
        code_str = """subroutine foo_intrinsic_types_kinds
  ! some function
  character(5) :: a
  character(len=5) :: aa
  character(*), parameter :: aaa = "aaa"
  character(:), allocatable :: aaaa
  complex(kind=8) :: b
  doubleprecision :: c
  doubleprecision::cc
  integer(kind(0)) :: d
  integer(kind=8), dimension(:), allocatable :: dd
  integer(kind=8), dimension(:,:), allocatable :: ddee
  integer(kind=8), dimension(10) :: ddd
  integer(kind=8), allocatable :: dddd(:)
  integer(kind=8), allocatable :: ddddee(:, :)
  integer(kind=8) :: ddddd(10)
  ! integer, bind(C) :: dddddd ! bind(C) must be declared in a module
  logical(kind=1) :: e
  real(kind=selected_real_kind(5,6)) :: f
  real(kind(0.0)) :: ff
end subroutine foo_intrinsic_types_kinds

"""
        self.check_source(name='subprogram_intrinsic_types_kinds', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_array(self):
        code_str = """subroutine foo_array

  implicit none

  real, dimension(50) :: bar
  integer :: baz(10, 10, 10)
  integer :: x, y, z
  integer :: v(2), u(3)

  bar = 1
  bar(1) = 2

  x = 1
  y = 2
  z = 3
  baz = 60
  baz(:, :, :) = 61
  baz(x, :, :) = 62
  baz(x, y, :) = 63
  baz(x, y, z) = 64

  baz (2:8, 1, 2) = 70
  baz (2:8:2, 1, 2) = 72
  baz (2:8:2, 3:9:3, 1:9:1) = 73

  v = (/ 4, 5 /)
  baz(1, :, v) = 80
  baz(v, 1, :) = 81

  u = (/ 6, 7, 8 /)
  baz(u, v, :) = 90
  
end subroutine foo_array

"""
        self.check_source(name='subprogram_array', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_derived_type(self):
        code_str = """subroutine foo_derived_type

  implicit none

  type :: bar
     integer :: a
     real :: b(2)
  end type bar

  type(bar) :: baz
  type(bar), dimension(5) :: boo

  baz%a = 1
  baz % a = 2

  boo(1)%a = 2
  boo ( 2 ) % a = 2
  boo(3)%a = 3 + baz%a
  boo(4)%a=3+baz%a
  
end subroutine foo_derived_type

"""
        self.check_source(name='subprogram_derived_type', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_function(self):
        code_str = """function foo_dummy()
  implicit none
  real :: foo_dummy
  
end function foo_dummy

"""
        self.check_source(name='subprogram_function', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_initialization_expression(self):
        code_str = """subroutine foo_init()

  real :: alice = 0.0
  
end subroutine foo_init

"""
        self.check_source(name='subprogram_initialization_expression', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_parameter(self):
        code_str = """subroutine foo_param()

  integer, parameter :: eve = 10
  
end subroutine foo_param

"""
        self.check_source(name='subprogram_parameter', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_assignment_statement(self):
        code_str = """subroutine foo_assign()

  real :: three

  three = 3.14159
  three = -3.0
  three = 1.0 + 2.0
  
end subroutine foo_assign

"""
        self.check_source(name='subprogram_assignment_statement', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_assignment_logical(self):
        code_str = """subroutine test_assign_logical()

  logical :: bool

  bool = .false.
  bool=.true.

  
end subroutine test_assign_logical

"""
        self.check_source(name='subprogram_assignment_logical', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_real_literal_constant(self):
        code_str = """subroutine foo_real_kinds()

  integer, parameter :: r8 = selected_real_kind(12) ! 8 byte real
  real(r8) :: x

  x = 1.0d-12
  x = 1.0e-12_r8
  x = -1.0e-12_r8
  x = 1._r8
  x = .1_r8
  x = -.1_r8
  x = 1.2345
  x = 1234.5
  x = 1234e-3
  
end subroutine foo_real_kinds
"""
        self.check_source(name='subprogram_real_literal_constant', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_assign_string_literal(self):
        code_str = """subroutine foo_assign_string_literal()

  character(12) :: str = 'A string'

  str = "A string"
  str = ' don''t '
  str = "Hi ""Bob""."
  str = '_!@#$%^*()-'
  
end subroutine foo_assign_string_literal

"""
        self.check_source(name='subprogram_assign_string_literal', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_implicit_none(self):
        code_str = """subroutine foo_implicit_none()

  implicit none
  
end subroutine foo_implicit_none

"""
        self.check_source(name='subprogram_implicit_none', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_implicit_none_assignment(self):
        code_str = """subroutine foo_implicit_none_assign()

  implicit none
  
  real, parameter :: one = 1.0
  real :: two, three

  two = 2.0
  three = one + two
  
end subroutine foo_implicit_none_assign

"""
        self.check_source(name='subprogram_implicit_none_assignment', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_implicit_none_assignment_comments(self):
        code_str = """subroutine foo_implicit_none_assign()
  ! comment
  implicit none
  ! another
  real, parameter :: one = 1.0  ! still another
  real :: two, three ! hello, world
  ! lets do something
  two = 2.0 ! look at that
  three = one + two ! we can add manually!
  
end subroutine foo_implicit_none_assign

"""
        self.check_source(name='subprogram_implicit_none_assignment_comments', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_dummy_args(self):
        code_str = """subroutine foo_dummy_args(bar, baz, bob, boo)
  ! some function
  integer, intent(in) :: bar ! some input
  real, intent(out) :: baz ! some output
  real, intent(inout) :: bob ! some inoutput
  real, intent(in out) :: boo ! some inoutput

end subroutine foo_dummy_args


"""
        self.check_source(name='subprogram_dummy_args', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_3statements(self):
        code_str = """subroutine foo_func_dummy()
  implicit none
  real :: abc, bcd, cde
  
  abc = 1.0
  bcd = 2.0
  cde = 3.0

end subroutine foo_func_dummy
"""
        self.check_source(name='subprogram_3statements', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_if(self):
        code_str = """subroutine foo_if()
  implicit none
  integer :: abc = 1

  if (abc > 0 ) abc = 2
end subroutine foo_if
"""
        self.check_source(name='subprogram_if', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_if_then(self):
        code_str = """subroutine foo_if_then()
  implicit none
  integer :: abc = 1

  if (abc > 0 ) then
     abc = 2
  end if
end subroutine foo_if_then
"""
        self.check_source(name='subprogram_if_then', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_if_logical_and(self):
        code_str = """subroutine foo_if_logical_and()
  implicit none
  integer :: abc = 1
  integer :: cde = 2
  integer, parameter :: xyz = 2

  if (abc > 0 .and. cde == xyz) then
     abc = 2
  end if
end subroutine foo_if_logical_and
"""
        self.check_source(name='subprogram_if_logical_and', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_if_logical_paren(self):
        code_str = """subroutine foo_if_logical_paren()
  implicit none
  integer :: abc = 1
  integer :: cde = 2
  integer, parameter :: xyz = 2

  if (abc > 0 .and. (abc <=  cde .and. cde <= xyz)) then
     abc = 2
  end if
end subroutine foo_if_logical_paren
"""
        self.check_source(name='subprogram_if_logical_paren', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_if_nested(self):
        code_str = """subroutine foo_if_nested()
  implicit none
  integer :: abc = 1
  integer :: cde = 2
  integer, parameter :: xyz = 2

  if (abc > 0 ) then
     if (cde == xyz) then
        abc = 2
     end if
  end if
end subroutine foo_if_nested
"""
        self.check_source(name='subprogram_if_nested', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_if_elseif_else(self):
        code_str = """subroutine foo_if_elseif_else()
  implicit none
  integer :: abc = 1
  integer :: cde = 2

  if (abc > 0 ) then
     cde = 0
  else if (abc == 0) then
     cde = 1
  elseif(abc < 0)then
     cde = 2
  else
     ! should never be here!
     cde = 3
  end if
end subroutine foo_if_elseif_else
"""
        self.check_source(name='subprogram_if_elseif_else', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_if_named(self):
        code_str = """subroutine foo_if_named()
  implicit none
  integer :: abc = 1

  check_abc : if (abc > 0 ) then
     abc = 2
  end if check_abc
end subroutine foo_if_named
"""
        self.check_source(name='subprogram_if_named', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_relational_op(self):
        code_str = """subroutine foo_relational_op()

  logical :: bar

  bar = 1.0 == 2.0
  bar = 1.0 .eq. 2.0
  bar = 1.0==2.0
  bar = 1.0.eq.2.0
  bar = 1.0 /= 2.0
  bar = 1.0 .ne. 2.0
  bar = 1.0 < 2.0
  bar = 1.0 .lt. 2.0
  bar = 1.0 <= 2.0
  bar = 1.0 .le. 2.0
  bar = 1.0 > 2.0
  bar = 1.0 .gt. 2.0
  bar = 1.0 >= 2.0
  bar = 1.0 .ge. 2.0

end subroutine foo_relational_op
"""
        self.check_source(name='subprogram_relational_op', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_logical_op(self):
        code_str = """subroutine foo_logical_op()

  logical :: bar

  bar = (1.0 <= 2.0) .and. (2.0 <= 1.0)
  bar = (1.0 <= 2.0) .or. (2.0 <= 1.0)
  bar = .not. (1.0 <= 2.0)

end subroutine foo_logical_op
"""
        self.check_source(name='subprogram_logical_op', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_equivalence_op(self):
        code_str = """subroutine foo_equivalence_op()

  logical :: bar

  bar = (1.0 <= 2.0) .eqv. (2.0 <= 1.0)
  bar = (1.0 <= 2.0) .neqv. (2.0 <= 1.0)

end subroutine foo_equivalence_op
"""
        self.check_source(name='subprogram_equivalence_op', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_paren_expression(self):
        code_str = """subroutine foo_paren_expression()

  logical :: bar

  bar = 1.0 <= 2.0
  bar = (1.0 <= 2.0)

end subroutine foo_paren_expression
"""
        self.check_source(name='subprogram_paren_expression', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_do_loop(self):
        code_str = """subroutine foo_do_loop()

  integer :: n, m

  do n = 1, 5
     m = n
  end do

  a_loop : do n = 1, 6, 2
     m = n
  end do a_loop

end subroutine foo_do_loop
"""
        self.check_source(name='subprogram_do_loop', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_labeled_stmt(self):
        code_str = """subroutine test_labeled_stmt()
  implicit none
  integer :: a

010 a = 10

end subroutine test_labeled_stmt
"""
        self.check_source(name='subprogram_labeled_stmt', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_write(self):
        code_str = """subroutine foo_write()
  implicit none
  integer :: out = 6

  write(out, *) 'This is a test!',' It is only a test.'
  write ( out, * ) 'This is a test!' , ' It is only a test.'
  write(*, '(a, i5)') "int = ", out

end subroutine foo_write
"""
        self.check_source(name='subprogram_write', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_format_stmt(self):
        code_str = """subroutine subprogram_format_stmt()
  implicit none

  write(*, 9999) 1, 2.0

0001 format()
0010 format('string')
0100 format(i10)
1000 format ('int = ', i10)
2000 format (1x)
0200 format (f21.15)
0020 format (e21.15e3)
0002 format (a5)
9999 format ('int = ', i10, '  float = ', e5.4)

end subroutine subprogram_format_stmt
"""
        self.check_source(name='subprogram_format_stmt', compilable=True, valid_src=True, code_str=code_str)

    def test_subprogram_cpp_predefined(self):
        code_str = """subroutine foo_param()

  integer, parameter :: version = __LINE__
  character :: file_name = __FILE__
  
end subroutine foo_param
"""
        self.check_source(name='subprogram_cpp_predefined', compilable=True, valid_src=True, code_str=code_str)


if __name__ == "__main__":
    unittest.main()
