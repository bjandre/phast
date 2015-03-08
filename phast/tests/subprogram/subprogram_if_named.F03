subroutine foo_if_named()
  implicit none
  integer :: abc = 1

  check_abc : if (abc > 0 ) then
     abc = 2
  end if check_abc
end subroutine foo_if_named

