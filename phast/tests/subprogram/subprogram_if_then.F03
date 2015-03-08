subroutine foo_if_then()
  implicit none
  integer :: abc = 1

  if (abc > 0 ) then
     abc = 2
  end if
end subroutine foo_if_then

