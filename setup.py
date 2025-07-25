# setup.py
from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize

setup(
    name='ur_ikfast',
    version='0.1.0',
    license='MIT',
    long_description=open('README.md').read(),
    packages=find_packages(),          # find your ur5e, ur3, etc. dirs
    ext_modules=cythonize([
        Extension(
            "ur5e_ikfast",
            ["ur5e/ur5e_ikfast.pyx", "ur5e/ikfast_wrapper.cpp"],
            language="c++",
            libraries=["lapack"],
        )
    ], language_level="3"),
    zip_safe=False,
)

