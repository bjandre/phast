subroutine foo_if_elseif_else()
  implicit none
  integer :: abc = 1
  integer :: cde = 2

  if (abc > 0 ) then
     cde = 0
  else if (abc == 0) then
     cde = 1
  else if (abc < 0) then
     cde = 2
  else
     ! should never be here!
     cde = 3
  end if
end subroutine foo_if_elseif_else

