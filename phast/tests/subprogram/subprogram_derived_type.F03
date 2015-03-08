subroutine foo_derived_type

  implicit none

  type :: bar
     integer :: a
     real :: b(2)
  end type bar

  type(bar) :: baz
  type(bar), dimension(5) :: boo

  baz%a = 1
  baz % a = 2

  boo(1)%a = 2
  boo ( 2 ) % a = 2
  boo(3)%a = 3 + baz%a
  boo(4)%a=3+baz%a
  
end subroutine foo_derived_type

