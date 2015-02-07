subroutine foo_logical_op()

  logical :: bar

  bar = (1.0 <= 2.0) .and. (2.0 <= 1.0)
  bar = (1.0 <= 2.0) .or. (2.0 <= 1.0)
  bar = .not. (1.0 <= 2.0)

end subroutine foo_logical_op

