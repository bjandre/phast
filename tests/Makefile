SUBDIRS = \
	subprogram \
	module

# MAKECMDGOALS is the make option: make 'clobber' or 'all'
TARGET = $(MAKECMDGOALS)

# if target is undefined (i.e. MAKECMDGOALS is undefined), target = all
ifeq (,$(TARGET))
	TARGET = all
endif

#
# macro for executing TARGET in all SUBDIRS
#
ifdef SUBDIRS
$(SUBDIRS) : FORCE
	@if [ -d $@ ]; then \
		$(MAKE) --directory=$@ $(TARGET); \
	fi	
	@echo Build complete: $@ : $(shell date)
endif	

#
# all - Make everything in the listed sub directories
#
all : $(SUBDIRS)

test : $(SUBDIRS) py-unit

py-unit : FORCE
	PYTHONPATH="${PYTHONPATH}:.." python -m unittest discover

py3-unit : FORCE
	PYTHONPATH="${PYTHONPATH}:.." python3 -m unittest discover


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

