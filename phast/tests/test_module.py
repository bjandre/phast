#!/usr/bin/env python

import unittest

from phast.tests.test_phast_base import TestPhastBase

from grako.contexts import FailedParse

class TestPhastModule(TestPhastBase):
    """unittest suite for phast's ability to process fortran 2003 modules
    """

    def setUp(self):
        super(TestPhastModule, self).setUp()
        self.startrule = "module"
        self.test_dir = "phast/tests"

    def tearDown(self):
        super(TestPhastModule, self).tearDown()

    def test_minimal_module(self):
        code_str = """module minimal_module
  
contains
  
  subroutine foo()

  end subroutine foo
  
end module minimal_module

"""
        self.check_source(name='minimal_module',
                          compilable=True, valid_src=True,
                          code_str=code_str)

    def test_0002(self):
        code_str = """module minimal_module_comments   ! this is module test_module_03
  ! comment in an empty module
  ! another comment
contains
  ! comment  
  subroutine bar()
    ! subroutine comment
  end subroutine bar

  subroutine baz()
    ! subroutine comment
  end subroutine baz
  ! comment
  
end module minimal_module_comments

"""
        self.check_source(name='minimal_module_comments',
                          compilable=True, valid_src=True,
                          code_str=code_str)

    def test_0003(self):
        """
        """
        code_str = """module public_vars

  integer, public :: coffee
  integer, public :: cream_use
  integer, public :: use_sugar
  
contains
  
  subroutine maker()

    real :: water

  end subroutine maker
  
end module public_vars


"""
        self.check_source(name='public_vars',
                          compilable=True, valid_src=True,
                          code_str=code_str)

    def test_0004(self):
        """
        """
        code_str = """module module_use
  use t0001_minimal_module
  use t0002_minimal_module_comments, only : &
       bar
  use t0002_minimal_module_comments, only : &
       bob => baz
  use t0003_module_param, only : coffee, cream_use, use_sugar

contains
  
  subroutine xyz

  end subroutine xyz
  
end module module_use
"""
        # NOTE(bja, 201503) this can't be compiled by gfortran because
        # the used module files don't exist!
        self.check_source(name='module_use',
                          compilable=False, valid_src=True,
                          code_str=code_str)

    def test_0005(self):
        """
        """
        code_str = """module implicit_none

  implicit none
  
contains
  
  subroutine foo()

    implicit none
    
  end subroutine foo
  
end module implicit_none

"""
        self.check_source(name='implicit_none',
                          compilable=True, valid_src=True,
                          code_str=code_str)

    def test_0006(self):
        """
        """
        code_str = """module dummy_args
  ! this is a module
  
  implicit none

  private
  integer, parameter :: r64 = selected_real_kind(12)

contains
  
  subroutine foo(bar, baz)
    ! some function
    integer, intent(in) :: bar ! some input
    real(r64), intent(out) :: baz ! some output
    real :: alice, eve
    
  end subroutine foo
  
end module dummy_args

"""
        self.check_source(name='dummy_args',
                          compilable=True, valid_src=True,
                          code_str=code_str)

    def test_0007(self):
        """
        """
        code_str = """module minimal_module_fail

contains
  
end module minimal_module_fail


"""
        self.check_source(name='minimal_module_fail', compilable=True, valid_src=False, code_str=code_str)


    def test_module_call_dummy_args(self):
        code_str = """module call_dummy_args

  implicit none
  
contains

  subroutine foo_dummy()

  end subroutine foo_dummy
  
  subroutine foo_dummy_args(bar, baz)
    ! some function
    implicit none
    integer, intent(in) :: bar ! some input
    real, intent(out) :: baz ! some output

    real :: alice, eve
  
  end subroutine foo_dummy_args

  subroutine foo_call_dummy_args()
    implicit none
    integer :: bar ! some input
    real :: baz ! some output

    call foo_dummy
    call foo_dummy()
    call foo_dummy ( )
    call foo_dummy_args(bar, baz)
  
  end subroutine foo_call_dummy_args
end module call_dummy_args
"""
        self.check_source(name='call_dummy_args',
                          compilable=True, valid_src=True,
                          code_str=code_str)

    def test_module_call_arg_array_derived_type(self):
        code_str = """module call_arg_array_derived_type
  ! tes whether we can make subroutine call whose args are 
  implicit none

  type :: baz_type
     integer :: a
     integer, dimension(4) :: b
  end type baz_type
  
contains

  subroutine foo_dummy(bar)
    integer :: bar
  end subroutine foo_dummy
  
  subroutine foo_call_dummy_args()
    implicit none
    type(baz_type), dimension(3) :: baz
    integer :: n

    call foo_dummy(baz(n)%a)
    call foo_dummy(baz(n)%b(3))
    call foo_dummy ( baz ( n ) % a )
    call foo_dummy ( baz( n ) % b ( 3 ) )
  
  end subroutine foo_call_dummy_args
end module call_arg_array_derived_type
"""
        self.check_source(name='call_arg_array_derived_type',
                          compilable=True, valid_src=True,
                          code_str=code_str)

    def test_module_call_function(self):
        code_str = """module call_function
  implicit none
contains
  function foo_dummy()
    implicit none
    real :: foo_dummy
    return
  end function foo_dummy

  function bar_dummy(a, b) result(c)
    implicit none
    integer, intent(in), optional :: a
    real, intent(in) :: b
    real :: c
    c = b
  end function bar_dummy

  subroutine test_call_function_dummy()
    implicit none
    real :: baz ! some output
    real :: fuzzy = 3.0
    
    baz = foo_dummy()
    baz = bar_dummy(1, fuzzy)
    baz = bar_dummy(b=fuzzy)
    baz = bar_dummy(b=fuzzy, a=1)
  end subroutine test_call_function_dummy
end module call_function
"""
        self.check_source(name='call_function',
                          compilable=True, valid_src=True,
                          code_str=code_str)

    def test_module_call_procedure(self):
        code_str = """module test_call_procedure
  
contains
  
  subroutine test_foo()
    implicit none

  end subroutine test_foo

  subroutine test_bar(abc, init)
    implicit none
    integer, intent(in) :: abc
    logical, intent(in) :: init

  end subroutine test_bar

  subroutine test_baz(abc, xyz)
    implicit none
    integer, intent(in) :: abc
    integer, intent(out) :: xyz
    xyz = 2*abc
  end subroutine test_baz

  subroutine test_calls()
    implicit none
    integer :: abc, xyz

    abc = 1

    call test_foo()
    call test_baz(abc, xyz)
    call test_bar(abc, .false.)
    call test_bar(abc, init=.false.)
    
  end subroutine test_calls

end module test_call_procedure
"""
        self.check_source(name='call_procedure',
                          compilable=True, valid_src=True,
                          code_str=code_str)


if __name__ == "__main__":
    unittest.main()
    print(unittest.TestResult.unexpectedSuccess)
