SRC_SUBDIRS = \
	phast

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
	@echo Build complete: $@ : $(TARGET) : $(shell date)
endif	

#
# all - Make everything in the listed sub directories
#
all : $(SRC_SUBDIRS)
	python setup.py develop

#
# testing. We include subdirs to build compile with gfortran, for now. python2 vs python3 testing is handled by the virtual env.
#
test : all $(SRC_SUBDIRS) py-unit

py-unit : FORCE
	python -m unittest discover
#	PYTHONPATH="${PYTHONPATH}:.." python -m unittest discover

#
# virtual environments
#
env : phast-env2 phast-env3

phast-env2 :
	virtualenv -p python2 $@

phast-env3 :
	virtualenv -p python3 $@

#
# release info
#
version : FORCE
	@git describe --always 2>/dev/null > VERSION

#
# clean - Clean up the directory.
#
clean : $(SRC_SUBDIRS)
	-rm -f *~ *.CKP *.ln *.BAK *.bak .*.bak \
		core errs \
		,* .emacs_* \
		tags TAGS \
		make.log MakeOut \
		*.tmp tmp.txt

#
# clobber - Really clean up the directory.
#
clobber : clean $(SRC_SUBDIRS)
	-rm -f .Makedepend *.o *.mod *.il *.pyc
	-rm -rf *.egg-info build


clobber-env : FORCE
	-rm -rf phast-env2 phast-env3 

#
# FORCE - Null rule to force things to happen.
#
FORCE :

