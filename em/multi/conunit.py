# -*- coding: utf-8 -*-
"""
convert string with unit to number
Created on Mon Jun  9 23:21:34 2014

@author: asmuyi
"""

import numpy as np
import myconst as mc
from myconst import m,nm,um

def convlen(length):
    """convert length ended with unit"""
    for unit in ['nm','um'] :
        if unit in length:
            s=length.split(unit)
            if unit=='nm':
                val=float(s[0])*mc.nm
            elif unit=='um':
                val=float(s[0])*mc.um
    return val
    
#length=convlen('2um')
