"""Calculate the reflection coeff using TMM theory

"""

from __future__ import absolute_import

import sys
import numpy as np
from tools import myconst as mc
from tools import getmedia3 as gm3
import getz03 as gz3

def getneff(ri,tn,n,lam,ia):
    """ Get effective index. ri needs to be tensor style.
    
    """
    rin=ri[0][0]
    neff = rin * np.sin(ia/180.*np.pi)
    return rin,neff

def getr(ri,tn,n,lam,ia,pol):
    """ Get reflection.

    Example
    -------
    It takes the effective index (possibly anisotropic) from getneff3,
    such as::

        rin,neff = getneff(ri,tn,n,lam,ia) 
        r,rr,fi,z=getr(ri,tn,n,lam,ia,pol)
    
    :param ri: refractive index in complex
    :param tn: thickness in m
    :param n: layer number in int
    :param lam: wavelength in m
    :param ia: incident angle in deg
    :param pol: polarization in str

    """
    rin,neff=getneff(ri,tn,n,lam,ia)
    k=2*np.pi/lam
    ncos,y,z,zl,rr,r,heat,fi=(np.zeros(n,np.complex) for _ in xrange(8)) 
    """ zl is impedance on the left boundary
    rr is refl coeff on the right boundary
    """
    for ind in xrange(n):
        ncos[ind],y[ind],z[ind]=gz3.getncos(ri[ind],pol,ia,rin)
        fi[ind]=k*ncos[ind]*tn[ind]
#    print ncos    
    for ind in xrange(n):
        if ind==0:
            rr[-ind-1]=0
            r[-ind-1]=0
            zl[-ind-1]=z[-ind-1]
        else:
            rr[-ind-1] = (zl[-ind]-z[-ind-1])/(zl[-ind]+z[-ind-1])
            r[-ind-1] = rr[-ind-1]*np.exp(-1j*2*fi[-ind-1])
            zl[-ind-1] = z[-ind-1]*(zl[-ind]*np.cos(fi[-ind-1])+ \
                            1j*z[-ind-1]*np.sin(fi[-ind-1])) \
                            /(z[-ind-1]*np.cos(fi[-ind-1])+ \
                            1j*zl[-ind]*np.sin(fi[-ind-1]))
    return r,rr,fi,z
    
def getrefl(ri,tn,n,lam,ia,pol):
    r,rr,fi,z=getr(ri,tn,n,lam,ia,pol)
    return np.absolute(rr[0])**2
    
def getreflc(ri,tn,n,lam,ia,pol):
    r,rr,fi,z=getr(ri,tn,n,lam,ia,pol)
    return rr[0]
     
def getv(ri,tn,n,lam,ia,pol):
    """ get the v or field value on boundary"""
    r,rr,fi,z=getr(ri,tn,n,lam,ia,pol)
    v,vin,u1,i1,u2,i2,heat = ((np.zeros(len(r),np.complex)) for _ in xrange(7))
    vin[0]=1.0
    for ind in xrange(len(r)):
        v[ind]=vin[ind]*(1+rr[ind])*np.exp(-1j*fi[ind])
        if ind==len(r)-1:
            break            
        else:
            vin[ind+1]=v[ind]/(1+r[ind+1])
    tran=np.absolute(vin[-1])**2/np.absolute(vin[0])**2/ \
            np.conj(z[-1])*np.conj(z[0])
    for ind in xrange(n):
        u1[ind] = vin[ind]*(1+r[ind])
        u2[ind] = v[ind]
        i1[ind] = vin[ind]*(1-r[ind])/z[ind]
        i2[ind] = v[ind]/(1+rr[ind])*(1-rr[ind])/z[ind]
    for ind in xrannge(n):
        if ind == n-1:
            heat[ind] = 0
            break
        else:
            heat[ind] = (np.real(u1[ind]*np.conj(i1[ind])) - \
                        np.real(u2[ind]*np.conj(i2[ind]))) \
                            /np.real(vin[0]*np.conj(vin[0]/z[0]))
    return tran,vin,v,z,heat
    
def gettran(ri,tn,n,lam,ia,pol):
    tran,vin,v,z,heat=getv(ri,tn,n,lam,ia,pol)
    return tran
    
def getheat(ri,tn,n,lam,ia,pol):
    tran,vin,v,z,heat=getv(ri,tn,n,lam,ia,pol)
    return np.sum(heat)

def getheatn(ri,tn,n,lam,ia,pol,heatn):
    tran,vin,v,z,heat = getv(ri,tn,n,lam,ia,pol)
    return heat[heatn]

if __name__ == "__main__":
    ri,tn,n,lam = gm3.getmedia(str(sys.argv[1]),str(sys.argv[2]))
    print getrefl(ri,tn,n,lam,45,"TE")
