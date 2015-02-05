FC=gfortran
TEST_SRCS = \
	./t0001_minimal_module.F03 \
	./t0002_minimal_module_comments.F03 \
	./t0003_module_param.F03 \
	./t0004_module_use.F03 \
	./t0005_module_implicit_none.F03 \
	./t0006_module_dummy_args.F03 \
	./t0007_minimal_module_fail.F03 \
	./module_call_dummy_args.F03 \
	./module_call_function.F03

# NOTE(bja, 2015-02) these are invalid tests for subprogram, need to be moved to module
#	./subprogram_call_function_call_procedure.F03 


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

