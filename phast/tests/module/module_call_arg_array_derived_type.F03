module call_arg_array_derived_type
  ! tes whether we can make subroutine call whose args are 
  implicit none

  type :: baz_type
     integer :: a
     integer, dimension(4) :: b
  end type baz_type
  
contains

  subroutine foo_dummy(bar)
    integer :: bar
  end subroutine foo_dummy
  
  subroutine foo_call_dummy_args()
    implicit none
    type(baz_type), dimension(3) :: baz
    integer :: n

    call foo_dummy(baz(n)%a)
    call foo_dummy(baz(n)%b(3))
    call foo_dummy ( baz ( n ) % a )
    call foo_dummy ( baz( n ) % b ( 3 ) )
  
  end subroutine foo_call_dummy_args
end module call_arg_array_derived_type
