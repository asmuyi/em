# -*- coding: utf-8 -*-
"""
Created on Tue Jul 08 15:41:27 2014

@author: 498148
"""

import numpy as np 
import numpy.fft as fft 
import matplotlib.pyplot as plt
import pwefft as pf
import myconst as mc
import getmedia2 as gm2
import tmrefl2 as tr2
import reconwvg as rw
import getmode as gm
import reconwvg as rw
from scipy import integrate as it

def getovl1(fx,r,x,ita,pol):
    if pol=='TE':
        po=np.trapz(r*np.conj(fx)/(-ita),x)
        pi=np.trapz(fx*np.conj(fx)/-ita,x)
    else:
#        po=np.trapz((r*np.conj(fx)+np.conj(r)*fx)*0.5*ita,x)
#        po=np.trapz(r*np.conj(fx)*ita,x)
#        pi=np.trapz(fx*np.conj(fx)*ita,x)
        po=np.trapz(np.conj(r)*(fx)*ita,x)
        pi=np.trapz(np.conj(fx)*(fx)*ita,x)
    r2=np.abs(po/pi)**2
#    r2=(np.real(po)/np.real(pi))**2
    return po,pi,r2
    
def getall(fx,r,x,ita,ia):
    po=np.trapz(r*np.conj(r)*ita,x)
    pi=np.trapz(fx*np.conj(fx)*ita,x)
    r2=np.abs(po/pi)
    return po,pi,r2
    
def getovl2(r,r_cross,f,f_cross,x,pol):
    if pol=='TE':
        pin=0.5*np.trapz(f*np.conj(f_cross),x)
        pout=0.5*np.trapz(r*np.conj(r_cross),x)
#    pout2=0.25*np.trapz((r*np.conj(f_cross))-(r_cross*np.conj(f)),x)
        pout2=0.25*np.trapz((r*np.conj(f_cross))-(r_cross*np.conj(f)),x)
    else:
        pin=0.5*np.trapz(f_cross*np.conj(f),x)
        pout=0.5*np.trapz(r_cross*np.conj(r),x)
#        pout2=0.25*np.trapz((r_cross*np.conj(f))-(r*np.conj(f_cross)),x)
        pout2=0.25*np.trapz((r_cross*np.conj(f))-(r*np.conj(f_cross)),x)
    return np.real(pout)/np.real(pin),np.abs(pout2)/np.real(pin)
    