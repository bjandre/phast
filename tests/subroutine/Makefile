FC=gfortran
TEST_SRCS = \
	./t0008_subroutine_dummy_args.F03 \
	./t0009_subroutine_expression.F03

TEST_OBJS = \
	$(TEST_SRCS:%.F03=%.o)

TEST_LIBRARIES = libf03testmodule.a

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
# Generic rule to generate objects
#
%.o : %.F03
	$(FC) -c $(FFLAGS) -o $@ $<

libf03testmodule.a : $(TEST_OBJS)
	$(AR) $(ARFLAGS) $@ $(TEST_OBJS)

#
# 
#
all : $(TEST_LIBRARIES)

test : $(TEST_LIBRARIES)

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

