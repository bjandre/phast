#
# all - Make everything in the listed sub directories
#
all : FORCE

test : FORCE

#
# clean - Clean up the directory.
#
clean : FORCE
	-rm -f *~ *.CKP *.ln *.BAK *.bak .*.bak \
		core errs \
		,* .emacs_* \
		tags TAGS \
		make.log MakeOut \
		*.tmp

#
# clobber - Really clean up the directory.
#
clobber : clean 
	-rm -f .Makedepend *.o *.mod *.il *.pyc

#
# FORCE - Null rule to force things to happen.
#
FORCE :

