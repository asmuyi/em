"""Generate a list from string input that might include unit such as um.

"""

from __future__ import absolute_import

import numpy as np
import sys
import conunit as cu

def getarray(str_array):
    """Get number array or list from string.

    :param str_array: a str array
    :type str_array: str
    :return: number
    :rtype: float list
    Example::

      getarray('2:2:8')
    will generate a list of [2,4,6,8]

    or::

      getarray('2um:2um:8um')

    Add the input method of doing something like::

      getarray("2 4 6 8")

    """
    if ':' in str_array:
        s=str_array.split(':')
        if 'm' in s[0]:
            s2=[cu.convlen(x) for x in s]
        else: 
            s2=[float(x) for x in s]
        ns=round((s2[2]-s2[0])/s2[1])+1
        s3=np.linspace(s2[0],s2[2],ns)
    else:
	s=str_array.split(" ")[:-1]
	if 'm' in s[0]:
	    s3=[cu.convlen(x) for x in s]
	else:
	    s3=[float(x) for x in s]
        
    return s3

if __name__ == "__main__":
    print "getarray running"
    if ":" in sys.argv[1]:
	str_array=sys.argv[1]
    else:
	str_array = '' 
	for arg in sys.argv[1:]:
	    str_array += arg+' '
    print str_array,"-> ",getarray(str_array)
           
            
