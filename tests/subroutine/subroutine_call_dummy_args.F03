subroutine foo_dummy_args(bar, baz)
  ! some function
  integer, intent(in) :: bar ! some input
  real, intent(out) :: baz ! some output

  real :: alice, eve
  
end subroutine foo_dummy_args

subroutine foo_call_dummy_args()
  implicit none
  integer :: bar ! some input
  real :: baz ! some output

  call foo_dummy_args(bar, baz)
  
end subroutine foo_call_dummy_args

