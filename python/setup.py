from distutils.core import setup
from distutils.extension import Extension
import os
import sys
import platform

openmm_dir = '/usr/local/openmm'
coulombplugin_header_dir = '/home/mike/repos/openmmcoulombplugin/openmmapi/include'
coulombplugin_library_dir = '/home/mike/repos/openmmcoulombplugin'

# setup extra compile and link arguments on Mac
extra_compile_args = ['-std=c++11']
extra_link_args = []

if platform.system() == 'Darwin':
    extra_compile_args += ['-stdlib=libc++', '-mmacosx-version-min=10.7']
    extra_link_args += ['-stdlib=libc++', '-mmacosx-version-min=10.7', '-Wl', '-rpath', openmm_dir+'/lib']

extension = Extension(name='_coulombplugin',
                      sources=['CoulombPluginWrapper.cpp'],
                      libraries=['OpenMM', 'CoulombPlugin'],
                      include_dirs=[os.path.join(openmm_dir, 'include'), coulombplugin_header_dir],
                      library_dirs=[os.path.join(openmm_dir, 'lib'), coulombplugin_library_dir],
                      extra_compile_args=extra_compile_args,
                      extra_link_args=extra_link_args
                     )

setup(name='coulombplugin',
      version='1.0',
      py_modules=['coulombplugin'],
      ext_modules=[extension],
     )
