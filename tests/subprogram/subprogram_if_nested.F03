subroutine foo_if_nested()
  implicit none
  integer :: abc = 1
  integer :: cde = 2
  integer, parameter :: xyz = 2

  if (abc > 0 ) then
     if (cde == xyz) then
        abc = 2
     end if
  end if
end subroutine foo_if_nested

