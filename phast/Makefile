SUBDIRS = \
	tests

PARSER = fortran_2003.py
GRAMMAR = fortran_2003.ebnf

# MAKECMDGOALS is the make option: make 'clobber' or 'all'
TARGET = $(MAKECMDGOALS)

# if target is undefined (i.e. MAKECMDGOALS is undefined), target = all
ifeq (,$(TARGET))
	TARGET = all
endif

#
# all - Make everything in the listed sub directories
#
ifdef SUBDIRS
$(SUBDIRS) : FORCE
	@echo $@ : $(TARGET)
	@if [ -d $@ ]; then \
		$(MAKE) --directory=$@ $(TARGET); \
	fi	
	@echo Build complete: $@ : $(TARGET) : $(shell date)
endif	

all : $(PARSER) $(SUBDIRS)

test : all $(SUBDIRS)

$(PARSER) : $(GRAMMAR)
	grako -o $@ $<

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
	-rm -f .Makedepend *.o *.mod *.il *.pyc $(PARSER)

#
# FORCE - Null rule to force things to happen.
#
FORCE :

