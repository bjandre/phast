FC=gfortran
TEST_SRCS = \
	./subroutine_comment_special_chars.F03 \
	./subroutine_initialization_expression.F03 \
	./subroutine_parameter.F03 \
	./subroutine_assignment_statement.F03 \
	./subroutine_implicit_none_assignment.F03 \
	./subroutine_implicit_none_assignment_comments.F03 \
	./subroutine_dummy_args.F03 \
	./subroutine_3statements.F03 \
	./subroutine_function.F03

# NOTE(bja, 2015-02) these are invalid tests for subroutine, need to be moved to module
#	./subroutine_call_dummy_args.F03 \
#	./subroutine_call_function.F03 \
#	./subroutine_call_function_call_procedure.F03 


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

