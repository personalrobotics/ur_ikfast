from setuptools import setup, Extension
from Cython.Build import cythonize
# If you need NumPy headers, uncomment these two lines:
# import numpy
# include_dirs = [numpy.get_include()]
include_dirs = []

extensions = [
    # Put the built module inside the 'ur5e' package (import as 'from ur5e import ur5e_ikfast')
    Extension(
        name="ur5e.ur5e_ikfast",
        sources=["ur5e/ur5e_ikfast.pyx", "ur5e/ikfast_wrapper.cpp"],
        language="c++",
        include_dirs=include_dirs,
        libraries=["lapack"],   # adjust/remove if not needed on your system
        # library_dirs=[],      # e.g., ['/usr/lib/x86_64-linux-gnu']
        # extra_compile_args=["-O3"],
    ),
]

setup(
    ext_modules=cythonize(extensions, language_level="3"),
)
