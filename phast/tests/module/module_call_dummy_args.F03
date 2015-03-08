module call_dummy_args

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
