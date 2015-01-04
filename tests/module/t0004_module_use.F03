module t0004_module_use
  use t0001_minimal_module
  use t0002_minimal_module_comments, only : &
       bar
  use t0002_minimal_module_comments, only : &
       baz => bob
  use t0003_module_var, only : coffee, cream, sugar

contains
  
  subroutine xyz

  end subroutine xyz
  
end module t0004_module_use
