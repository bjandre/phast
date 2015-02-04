FC=gfortran
TEST_SRCS = \
	./subprogram_comment_special_chars.F03 \
	./subprogram_initialization_expression.F03 \
	./subprogram_parameter.F03 \
	./subprogram_assignment_statement.F03 \
	./subprogram_implicit_none_assignment.F03 \
	./subprogram_implicit_none_assignment_comments.F03 \
	./subprogram_dummy_args.F03 \
	./subprogram_3statements.F03 \
	./subprogram_function.F03


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

