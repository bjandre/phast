subroutine foo_real_kinds()

  integer, parameter :: r8 = selected_real_kind(12) ! 8 byte real
  real(r8) :: x

  x = 1.0d-12
  x = 1.0e-12_r8
  x = -1.0e-12_r8
  x = 1._r8
  x = .1_r8
  x = -.1_r8
  
end subroutine foo_real_kinds

