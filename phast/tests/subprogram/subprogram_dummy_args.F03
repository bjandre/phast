subroutine foo_dummy_args(bar, baz, bob, boo)
  ! some function
  integer, intent(in) :: bar ! some input
  real, intent(out) :: baz ! some output
  real, intent(inout) :: bob ! some inoutput
  real, intent(in out) :: boo ! some inoutput

end subroutine foo_dummy_args

