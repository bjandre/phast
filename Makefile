SRC_SUBDIRS = \
	phast

TEST_SUBDIRS = \
	tests

# MAKECMDGOALS is the make option: make 'clobber' or 'all'
TARGET = $(MAKECMDGOALS)

# if target is undefined (i.e. MAKECMDGOALS is undefined), target = all
ifeq (,$(TARGET))
	TARGET = all
endif

#
# macro for executing TARGET in all SUBDIRS
#
ifdef SRC_SUBDIRS
$(SRC_SUBDIRS) : FORCE
	@if [ -d $@ ]; then \
		$(MAKE) --directory=$@ $(TARGET); \
	fi	
	@echo Build complete: $@ : $(shell date)
endif	

ifdef TEST_SUBDIRS
$(TEST_SUBDIRS) : FORCE
	@if [ -d $@ ]; then \
		$(MAKE) --directory=$@ $(TARGET); \
	fi	
	@echo Build complete: $@ : $(shell date)
endif	

#
# all - Make everything in the listed sub directories
#
all : $(SRC_SUBDIRS)

test : all $(TEST_SUBDIRS)

#
# clean - Clean up the directory.
#
clean : $(SRC_SUBDIRS) $(TEST_SUBDIRS)
	-rm -f *~ *.CKP *.ln *.BAK *.bak .*.bak \
		core errs \
		,* .emacs_* \
		tags TAGS \
		make.log MakeOut \
		*.tmp 

#
# clobber - Really clean up the directory.
#
clobber : clean $(SRC_SUBDIRS) $(TEST_SUBDIRS)
	-rm -f .Makedepend *.o *.mod *.il *.pyc

#
# FORCE - Null rule to force things to happen.
#
FORCE :

