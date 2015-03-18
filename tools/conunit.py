# -*- coding: utf-8 -*-
"""
Convert string with unit to number.
"""

import numpy as np
import myconst as mc
from myconst import m,nm,um

def convlen(length):
    """Convert length ended with unit

    :param length: length in string
    :type length: str
    :returns: length in floating num
    :rtype: float
    
    Examples::

	convlen('2um')

    """
    for unit in ['nm','um'] :
        if unit in length:
            s=length.split(unit)
            if unit=='nm':
                val=float(s[0])*mc.nm
            elif unit=='um':
                val=float(s[0])*mc.um
    return val
    
if __name__ == "__main__":
    print "convert 2um"
