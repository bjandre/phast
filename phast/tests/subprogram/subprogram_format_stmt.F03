subroutine test_format_stmt()
  implicit none

  write(*, 9999) 1, 2.0

0001 format()
0010 format('string')
0100 format(i10)
1000 format ('int = ', i10)
2000 format (1x)
0200 format (f21.15)
0020 format (e21.15e3)
0002 format (a5)
9999 format ('int = ', i10, '  float = ', e5.4)

end subroutine test_format_stmt

