module foo_call_function
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
end module foo_call_function
