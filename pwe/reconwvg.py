# -*- coding: utf-8 -*-
"""
reconstruct the wvg field profile

"""

import myconst as mc
import numpy as np 
import matplotlib.pyplot as plt 
import numpy.fft as fft
import pwefft as pf
import getbeta as gb
from matplotlib import rc

 
def getfxyz(x,be,fzx,fxx,fyx):
    if np.isreal(fyx[0]):
        fx=-fyx
    else:
        fx=-np.imag(fyx)
    phi=fx/fyx
    s,dx,N=pf.gets(x)
    fft_fx=pf.getfft(fx,N)
    ifx=pf.getifft(fx,x)
    fx_cross=phi*fxx
    return x,s,fx,fft_fx,ifx,fx_cross
    
def getfxyz2(x,be,fzx,fxx,fyx):
    s,dx,N=pf.gets(x)
#    dx=x[1]-x[0]
#    N=len(x)
#    x,s=pf.getxs(dx,N)
    fx=fyx
    fft_fx=pf.getfft(fx,N)
    ifx=pf.getifft(fx,x)
    fx_cross=fxx
    return x,s,fx,fft_fx,ifx,fx_cross

#def getfy(x,be,fzx,fxx,fyx):
#    fx=np.imag(fyx)
#    s,dx,N=pf.gets(x)
##    dx=x[1]-x[0]
##    N=len(x)
##    x,s=pf.getxs(dx,N)
#    fft_fx=pf.getfft(fx,N)
#    ifx=pf.getifft(fx,x)
#    return x,s,fx,fft_fx,ifx
#    
#def getfz(x,be,fzx,fxx,fyx):
#    fx=np.real(fzx)
#    s,dx,N=pf.gets(x)
##    dx=x[1]-x[0]
##    N=len(x)
##    x,s=pf.getxs(dx,N)
#    fft_fx=pf.getfft(fx,N)
#    ifx=pf.getifft(fx,x)
#    return x,s,fx,fft_fx,ifx
##    return fx
#    
#def getfx(x,be,fzx,fxx,fyx):
#    fx=np.imag(fxx)
#    s,dx,N=pf.gets(x)
##    dx=x[1]-x[0]
##    N=len(x)
##    x,s=pf.getxs(dx,N)
#    fft_fx=pf.getfft(fx,N)
#    ifx=pf.getifft(fx,x)
##    return x,s,fx,fft_fx,ifx
#    return fx
    
def getne(s,be):
    k=2*np.pi    
    nxe=s/k
    nzg=be/k
    ne=np.sqrt(nxe**2+nzg**2)
    tin=np.arctan(nxe/nzg)*180.0/np.pi
    return ne,tin
    
#def getfy2(fy,s,be,pol): # Get the normal of the transverse field
#    ne=getne(s,be)
#    ita=np.sqrt(mc.mu0/mc.eps0)/ne
#    if pol=='TE':
#        fy2=-fy/ita
#    else:
#        fy2=fy*ita
#    return fy2
    
 
#x=np.linspace(-4,4,200)
#[wid,lam]=[1,1.55]
#[nc,nf,ns]=[1.0,3.5,1.45]
#pol='TE'
#m=0
#
#k=2*np.pi
#x,ita,be,fzx,fxx,fyx=gb.getmode(x,m,wid,nc,nf,ns,lam,pol)
#x,s,fx,fft_fx,ifx=getfy(x,be,fzx,fxx,fyx)

#plt.rc('text',usetex=True)
#plt.rc('font',family='serif')
#plt.figure(1) 
#plt.subplot(211) 
#plt.plot(x*lam,fx,x*lam,ifx,'s',markerfacecolor='none')
#plt.legend(['$f_x$', 'inv-fft'])
#plt.ylabel('${\phi}_y=f_x$')
#plt.subplot(212)
#plt.plot(s/k,np.real(fft_fx),'-*',s/k,np.imag(fft_fx),'--o')
#plt.xlabel('$k/k_0$')
#plt.ylabel('$FFT(f_x)$')
#plt.legend(['real','imag']) 
#plt.xlim(-10, 10)
