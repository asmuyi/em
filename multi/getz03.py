# -*- coding: utf-8 -*-
"""
calculate ncos, y, z of each layer
media info from getneff
Created on Wed Jun 11 19:52:13 2014
Updated on Jul 2014

@author: asmuyi 
"""
import numpy as np
import myconst as mc
import getneff3 as gn3
import getmedia3 as gm3
from myconst import eps0,mu0,c0

def getncos(ri,pol,ia,rin):
    neff = rin * np.sin(ia/180.0*np.pi)
    if ri[0]==ri[2]:
        print 'isotropic'
        ncos2=ri[0]**2-neff**2
        if ncos2.real<0 and ncos2.imag==0:
            ncos = -np.sqrt(-ncos2)*1j
        else:
            ncos = np.sqrt(ncos2)
        if pol=='TM':
            y=mc.c0*ri[0]**2*mc.eps0/ncos
        else:
            y=ncos/mc.c0/mc.mu0
    else:
        print 'uniax'
        if pol=='TM':
            cos2=ri[0]**2*(ri[2]**2-neff**2)/ \
                ((neff*ri[2])**2+(ri[0]*ri[2])**2-(ri[0]*neff)**2)
            ne2=neff**2/(1-cos2)
        else:
            ne2=ri[1]**2
            cos2=1-neff**2/ne2
        ncos2=ne2*cos2
        if ncos2.real<0 and ncos2.imag==0:
            ncos = -np.sqrt(-ncos2)*1j
        else:
            ncos = np.sqrt(ncos2)
        if pol=='TM':
            y=mc.c0*ri[0]**2*mc.eps0/ncos
        else:
            y=ncos/mc.c0/mc.mu0
    z=1/y
#    print ncos
    return ncos,y,z
    
