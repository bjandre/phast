If one judges the health of a programming language by its tool
ecosystem, then Fortran is in hospice care. Unfortunately there is
still too much "useful" legacy code to allow euthanasia.

Attempt to create an open source set of tools for refactoring and
linting "Modern" Fortran.

Use the draft Fortran 2003 ISO standard to hand create an EBNF grammar
for Fortran 2003.

Use something like [[ grako, https://bitbucket.org/apalala/grako ]] to
generate a parser and AST from the EBNF grammar.

gfortran list of [[ fortran standards documents, https://gcc.gnu.org/wiki/GFortranStandards ]]
