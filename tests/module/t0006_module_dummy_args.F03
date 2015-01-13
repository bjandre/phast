module t0006_module_dummy_args
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
  
end module t0006_module_dummy_args

