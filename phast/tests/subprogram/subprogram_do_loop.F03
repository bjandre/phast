subroutine foo_do_loop()

  integer :: n, m

  do n = 1, 5
     m = n
  end do

  a_loop : do n = 1, 6, 2
     m = n
  end do a_loop

end subroutine foo_do_loop

