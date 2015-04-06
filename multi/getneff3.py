# -*- coding: utf-8 -*-
"""
Effective index calculation for bi-axial in z

"""

import numpy as np
import tools.myconst as mc
#import getuser as gu
import getmedia3 as gm3
from tools.myconst import eps0,mu0,c0


def getneff(ri,tn,n,lam,ia):
    """ri=refractive index, ia=incident angle"""
#    if media != 'user':   
#    rin,tn,lam,n=gm.getmedia(media)  
#    else:
#        rin,tn,lam,n=test2.getuser()  
#    ri=rin[0]
    rin=ri[0][0]
    neff = rin * np.sin(ia/180.0*np.pi)
    return rin,neff
    
#print getneff('sp-lu',45)
#ri,tn,n,lam=gm3.getmedia('sp-lu')
#print getneff(ri,tn,n,lam,0)
