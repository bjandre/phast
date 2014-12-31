module t0003_module_use
  use t0001_minimal_module, only : foo
  use t0002_minimal_module_comments, only : &
       bar, baz

contains
  
  subroutine xyz

  end subroutine xyz
  
end module t0003_module_use
