subroutine foo_equivalence_op()

  logical :: bar

  bar = (1.0 <= 2.0) .eqv. (2.0 <= 1.0)
  bar = (1.0 <= 2.0) .neqv. (2.0 <= 1.0)

end subroutine foo_equivalence_op

