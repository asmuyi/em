"""EM scripts setup files

"""

import os,sys,subprocess
from setuptools import setup

def update_path():
    python_path = sys.path
    current_path = os.getcwd()
    current_platform = sys.platform

    print python_path

    if current_path not in python_path:
	if "win" in current_platform:
	    print "Adding current directory to PYTHONPATH..."
	    subprocess.call(["set","PYTHONPATH="+
		"%PYTHONPATH%;"+current_path],shell=True)
	    subprocess.check_output(["echo","%PYTHONPATH%"],shell=True)
	    print sys.path
	else:
	    sys.path.insert(0,current_path)

	setup(
		name = "EM package",
		version = "0.1",
		author = "asmuyi",
		author_email = "asmuyi@gmail.com",
		description = ("A collection of EM related" 
			"Python routines for simple structures"),
		url = "https://github.com/asmuyi/em",
		long_description=read('README'),
		classifiers = [
		"Development Status :: 2 - pre-Alpha",
		"Topic :: Scientific/Engineering",
		"License :: BSD License",
		],
	)

if __name__ == '__main__':
    update_path()

    

