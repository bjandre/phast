subroutine foo_implicit_none_assign()
  ! comment
  implicit none
  ! another
  real, parameter :: one = 1.0  ! still another
  real :: two, three ! hello, world
  ! lets do something
  two = 2.0 ! look at that
  three = one + two ! we can add manually!
  
end subroutine foo_implicit_none_assign

