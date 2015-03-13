#!/usr/bin/env python

import copy
import hashlib
import os
import subprocess
import unittest

from phast.fortran_2003 import fortran_2003Parser
from phast.fortran_2003_semantics import Fortran2003SemanticActions
from phast.phast_utils import PhastWriter

from grako.exceptions import FailedParse 

class TestPhastBase(unittest.TestCase):
    """unittest suite for phast's ability to process fortran 2003 modules
    """
    _compiler_cmds = []
    _devnull = None
    @classmethod
    def setUpClass(cls):
        """Run once per class
        """
        cls._compiler_cmds = []
        cls._check_compiler()
    
    @classmethod
    def _check_compiler(cls):
        """
        """
        try:
            from subprocess import DEVNULL # py3k
        except ImportError:
            import os
            DEVNULL = open(os.devnull, 'wb')
        cls._devnull = DEVNULL

        cmd = ['gfortran', '--version']
        try:
            subprocess.check_call(cmd, stdout=cls._devnull, stderr=subprocess.STDOUT)
            cls._compiler_cmds = ['gfortran', '-c', '-std=f2003', '-fsyntax-only', '-pedantic-errors', '-J', ]
        except subprocess.CalledProcessError:
            # gfortran unavailable...?
            cls._compiler_cmds = []

    def setUp(self):
        """run before every test function
        """
        self.whitespace = ""
        self.nameguard = False
        self.semantic_actions = Fortran2003SemanticActions()
        self.parser = fortran_2003Parser(parseinfo=True,
                                         ignorecase=True,
                                         trace_length=512)
        self.text = None
        self.ast = None
        self.startrule = 'program'
        self.test_dir = 'phast/tests'

    def tearDown(self):
        pass

    def _generate_ast_from_file(self, src_file):
        """
        """
        ast = None
        try:
            with open(src_file) as f:
                self.text = f.read()
        except IOError as e:
            err_msg = "Could not find fortran file '{0}'. cwd = {1}".format(
                src_file, os.getcwd())
            e.strerror += err_msg
            raise e
        except Exception:
            pass
        else:
            try:
                ast = self.parser.parse(
                    self.text, self.startrule, src_file,
                    semantics=self.semantic_actions,
                    whitespace=self.whitespace,
                    nameguard=self.nameguard)
            except FailedParse:
                pass
        return ast

    def _generate_ast_from_str(self, code_str):
        """
        """
        ast = None
        try:
            ast = self.parser.parse(code_str, self.startrule,
                                    semantics=self.semantic_actions,
                                    whitespace=self.whitespace,
                                    nameguard=self.nameguard)
        except FailedParse:
            pass
        return ast

    def _hash_file(self, filename):
        h = hashlib.sha256()
        with open(filename, 'r') as src:
            for s in src.readlines():
                h.update(s.encode('utf-8'))
        return h.digest()

    def _write_ast(self, src_file, ast):
        hash_orig = self._hash_file(src_file)
        tmp = "{0}.tmp".format(src_file)
        phast_writer = PhastWriter(tmp)
        phast_writer.write(ast)
        del phast_writer
        hash_new = self._hash_file(tmp)
        self.assertEqual(hash_orig, hash_new)
        if hash_orig == hash_new:
            os.remove(tmp)

    def _compile_src(self, src_file, valid_src):
        """Check to see if the source file can be compiled by the compiler. assert that the actual compilability agrees with what the test developer expected.
        """
        mod_file = "{0}.mod".format(src_file[0:-4])
        cmd = copy.deepcopy(self._compiler_cmds)
        cmd.append(self.test_dir) # module file directory
        cmd.append(src_file)

        can_compile = True
        try:
            subprocess.check_call(cmd, stdout=self._devnull, stderr=subprocess.STDOUT)
            if os.path.isfile(mod_file):
                os.remove(mod_file)
            
        except subprocess.CalledProcessError:
            #print("could not compile '{0}'".format(src_file))
            can_compile = False
        self.assertTrue(can_compile == valid_src)
        return can_compile
            
    def check_source(self, name, compilable=False, valid_src=True, filename=None, code_str=None):
        if filename and code_str:
            # FIXME(bja, 2015-03) should be an error!
            pass

        if filename:
            src_file = os.path.join(self.test_dir, filename)
        if code_str:
            filename = "{0}.F03".format(name)
            src_file = os.path.join(self.test_dir, filename)
            with open(src_file, 'w') as tmp:
                tmp.write(code_str)

        can_compile = compilable
        if compilable:
            can_compile = self._compile_src(src_file, valid_src)
        
        if filename:
            ast = self._generate_ast_from_file(src_file)

        if code_str:    
            ast = self._generate_ast_from_str(code_str)

        if valid_src:
            self.assertIsNotNone(ast, msg=ast.__repr__())
        else:
            self.assertIsNone(ast)

        # check the ast can be written to recreate the original source
        # file.
        if valid_src:
            self._write_ast(src_file, ast)
        
        if code_str:
            # FIXME(bja, 201503) if we created the input file and
            # everything worked as espected, then we remove the file?
            os.remove(src_file)


if __name__ == "__main__":
    unittest.main()
