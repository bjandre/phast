subroutine foo_implicit_none_assign()

  implicit none
  
  real, parameter :: one = 1.0
  real :: two, three

  two = 2.0
  three = one + two
  
end subroutine foo_implicit_none_assign

