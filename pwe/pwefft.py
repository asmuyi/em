# -*- coding: utf-8 -*-
"""
Expand mode based on mode profile
"""

import numpy as np 
import numpy.fft as fft 
import multi.myconst as mc
  
def getxs(dx,N):
    """Convert from x-space def. to s-space

    :param dx: space between x-space grid
    :param N: number of x-space points
    :return x: x array
    :return s: s array

    Example ::
	        

    """
    x=np.arange(0,dx*(N),dx,float) 
    s=2*np.pi*fft.fftshift(fft.fftfreq(N,dx))
    return x,s
    
def gets(x):
    """Convert from x-space to s-space

    :param x: x array
    :returns: s,dx,N 

    """
    N=len(x)    
    dx=np.abs(x[1]-x[0])
    s=2*np.pi*fft.fftshift(fft.fftfreq(N,dx))
#    s=2*np.pi*(fft.fftfreq(N,dx))
    return s,dx,N

def getfft(fx,N):
    fft_fx=fft.fftshift(fft.fft(fx)/N)
    return fft_fx
    
def getifft(fx,x):
    s,dx,N=gets(x)
    fft_fx=getfft(fx,N)
    ifx=np.zeros(N,complex)
    x=x-x[0]
    for ind in np.arange(N):
        ifx[ind]=np.sum(fft_fx*np.exp(1j*s*x[ind]))
    return ifx
    
def getifftr(fx,x,refl,pol): # Transverse field reflected
    s,dx,N=gets(x)    
    fft_fx=getfft(fx,N)
    ifx2=np.zeros(N,complex)
    x=x-x[0]
    for ind in np.arange(N):
        if pol=='TE':
            ifx2[ind]=np.sum(fft_fx*np.exp(1j*s*x[ind])*refl)
        else:
            ifx2[ind]=np.sum(fft_fx*np.exp(1j*s*x[ind])*-refl)
    return ifx2

def getifftrc(fx,x,refl,ne,tin,pol): #Cross refl field in x direction, normal to fx
    tin=tin/180.*np.pi
    s,dx,N=gets(x)
    fft_fx=getfft(fx,N)
    ifxc=np.zeros(N,complex)
    x=x-x[0]
    ita2=np.sqrt(mc.mu0/mc.eps0)/ne #plane wave impedance
    for ind in np.arange(N):
        if pol=='TE':
            ifxc[ind]=np.sum(fft_fx*np.exp(1j*s*x[ind])*refl/ita2*np.cos(tin))
        else:
            ifxc[ind]=np.sum(fft_fx*np.exp(1j*s*x[ind])*-refl*-ita2*np.cos(tin))
    return ifxc

