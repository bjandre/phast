subroutine foo_write()
  implicit none
  integer :: out = 6

  write(out, *) 'This is a test!',' It is only a test.'
  write ( out, * ) 'This is a test!' , ' It is only a test.'
  write(*, '(a, i5)') "int = ", out

end subroutine foo_write

