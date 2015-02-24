subroutine foo_intrinsic_types_kinds
  ! some function
  character(5) :: a
  character(len=5) :: aa
  character(*), parameter :: aaa = "aaa"
  character(:), allocatable :: aaaa
  complex(kind=8) :: b
  doubleprecision :: c
  doubleprecision::cc
  integer(kind(0)) :: d
  integer(kind=8), dimension(:), allocatable :: dd
  integer(kind=8), dimension(:,:), allocatable :: ddee
  integer(kind=8), dimension(10) :: ddd
  integer(kind=8), allocatable :: dddd(:)
  integer(kind=8), allocatable :: ddddee(:, :)
  integer(kind=8) :: ddddd(10)
  ! integer, bind(C) :: dddddd ! bind(C) must be declared in a module
  logical(kind=1) :: e
  real(kind=selected_real_kind(5,6)) :: f
  real(kind(0.0)) :: ff
end subroutine foo_intrinsic_types_kinds

