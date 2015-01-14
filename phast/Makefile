PARSER = fortran_2003.py
GRAMMAR = ../fortran_2003.ebnf

$(PARSER) : $(GRAMMAR)
	grako -o $@ $<

#
# all - Make everything in the listed sub directories
#
all : $(PARSER)

test : all

#
# clean - Clean up the directory.
#
clean : $(SUBDIRS)
	-rm -f *~ *.CKP *.ln *.BAK *.bak .*.bak \
		core errs \
		,* .emacs_* \
		tags TAGS \
		make.log MakeOut

#
# clobber - Really clean up the directory.
#
clobber : clean $(SUBDIRS)
	-rm -f .Makedepend *.o *.mod *.il *.pyc

#
# FORCE - Null rule to force things to happen.
#
FORCE :

