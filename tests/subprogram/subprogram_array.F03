subroutine foo_array

  implicit none

  real, dimension(50) :: bar
  integer :: baz(10, 10, 10)
  integer :: x, y, z
  integer :: v(2), u(3)

  bar = 1
  bar(1) = 2

  x = 1
  y = 2
  z = 3
  baz = 60
  baz(:, :, :) = 61
  baz(x, :, :) = 62
  baz(x, y, :) = 63
  baz(x, y, z) = 64

  baz (2:8, 1, 2) = 70
  baz (2:8:2, 1, 2) = 72
  baz (2:8:2, 3:9:3, 1:9:1) = 73

  v = (/ 4, 5 /)
  baz(1, :, v) = 80
  baz(v, 1, :) = 81

  u = (/ 6, 7, 8 /)
  baz(u, v, :) = 90
  
end subroutine foo_array

