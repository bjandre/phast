module foo_call_function
  implicit none
contains
  function foo_dummy()
    implicit none
    real :: foo_dummy
    return
  end function foo_dummy

  subroutine call_foo_dummy()
    implicit none
    real :: baz ! some output
    
    baz = foo_dummy()
  
  end subroutine call_foo_dummy
end module foo_call_function
