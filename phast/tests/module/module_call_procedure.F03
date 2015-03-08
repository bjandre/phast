module test_call_procedure
  
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
