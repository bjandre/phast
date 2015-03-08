subroutine foo_assign_string_literal()

  character(12) :: str = 'A string'

  str = "A string"
  str = ' don''t '
  str = "Hi ""Bob""."
  str = '_!@#$%^*()-'
  
end subroutine foo_assign_string_literal

