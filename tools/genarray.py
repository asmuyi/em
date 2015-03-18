# -*- coding: utf-8 -*-
"""
Generate a list from string input that might include unit such as um.
"""

import numpy as np
import conunit as cu

def getarray(str_array):
    """Get number array or list from string.

    :param str_array: a str array
    :type str_array: str
    :return: number
    :rtype: float
    Example::

      getarray('2:2:8')
    or::

      getarray('2um:2um:8um')
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
        s3=cu.convlen(str_array)
        
    return s3

if __name__ == "__main__":
    print "getarray running"
#print getarray('2:2:8')
           
            
