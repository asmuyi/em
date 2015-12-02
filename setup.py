"""EM scripts setup files

"""

import os
import sys
from setuptools import setup

setup(
    name = "EM package",
    version = "0.1",
    author = "asmuyi"
    author_email = "asmuyi@gmail.com"
    description = ("A collection of EM related Python routines for
			simple structures"),
    url = "https://github.com/asmuyi/em",
    long_description=read('README'),
	"Development Status :: 2 - pre-Alpha",
	"Topic :: Scientific/Engineering",
	"License :: BSD License",
    ],
)

def update_path():
    src_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    old_path = os.getcwd()
    #TODO: 

