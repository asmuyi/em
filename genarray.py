# -*- coding: utf-8 -*-
"""
Created on Sat Jun 14 21:06:21 2014

@author: asmuyi 
"""

import numpy as np
import conunit as cu

def getarray(str_array):
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

#print getarray('2:2:8')
           
            
