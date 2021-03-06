try:
    from setuptools import setup, Extension
except ImportError:
    from distutils.core import setup, Extension

import numpy
# For rebuilding Cython extensions
try:
    from Cython.Distutils import build_ext
    USECYTHON = True
except ImportError:
    USECYTHON = False


config = {
    'description': 'coral',
    'author': 'Nick Bolten',
    'url': 'https://github.com/klavinslab/coral',
    'download_url': 'https://github.com/klavinslab/coral.git',
    'author_email': 'nbolten _at_ gmail',
    'version': '0.1.0',
    'install_requires': ['nose', 'numpy', 'biopython', 'intermine',
                         'requests'],
    'extras_require': {'plotting': ['matplotlib'],
                       'documentation': ['sphinx']},
    'packages': ['coral',
                 'coral.analysis',
                 'coral.analysis._sequence',
                 'coral.analysis._sequencing',
                 'coral.analysis._structure',
                 'coral.constants',
                 'coral.database',
                 'coral.design',
                 'coral.design._oligo_synthesis',
                 'coral.design._sequence_generation',
                 'coral.seqio',
                 'coral.reaction',
                 'coral.sequence'],
    'package_data': {'coral': ['coral/analysis/_sequencing/data/*']},
    'include_package_data': True,
    'scripts': [],
    'name': 'coral',
    'license': 'Copyright University of Washington'
}

seq_extension = Extension('coral.analysis._sequencing.calign',
                          ['coral/analysis/_sequencing/calign.c'],
                          include_dirs=[numpy.get_include()])
EXTENSIONS = [seq_extension]

if USECYTHON:
    setup(cmdclass={'build_ext': build_ext},
          ext_modules=EXTENSIONS,
          test_suite='nose.collector',
          **config)
else:
    setup(ext_modules=EXTENSIONS,
          test_suite='nose.collector',
          **config)
