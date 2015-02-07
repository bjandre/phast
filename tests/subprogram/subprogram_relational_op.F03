subroutine foo_relational_op()

  logical :: bar

  bar = 1.0 == 2.0
  bar = 1.0 .eq. 2.0
  bar = 1.0==2.0
  bar = 1.0.eq.2.0
  bar = 1.0 /= 2.0
  bar = 1.0 .ne. 2.0
  bar = 1.0 < 2.0
  bar = 1.0 .lt. 2.0
  bar = 1.0 <= 2.0
  bar = 1.0 .le. 2.0
  bar = 1.0 > 2.0
  bar = 1.0 .gt. 2.0
  bar = 1.0 >= 2.0
  bar = 1.0 .ge. 2.0

end subroutine foo_relational_op

