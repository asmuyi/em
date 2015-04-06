# -*- coding: utf-8 -*-
"""Calculate the reflection coeff using TMM theory

"""

import numpy as np
import getneff3 as gn3
import tools.myconst as mc
import getz03 as gz3


def getr(ri,tn,n,lam,ia,pol):
    """ Get reflection.

    Example
    -------
    It takes the effective index (possibly anisotropic) from getneff3,
    such as::

        rin,neff = getneff3.getneff(ri,tn,n,lam,ia) 
        r,rr,fi,z=getr(ri,tn,n,lam,ia,pol)
    
    :param ri: refractive index in complex
    :param tn: thickness in m
    :param n: layer number in int
    :param lam: wavelength in m
    :param ia: incident angle in deg
    :param pol: polarization in str

    """
    rin,neff=gn3.getneff(ri,tn,n,lam,ia)
    print rin,neff
    k=2*np.pi/lam
    ncos,y,z,zl,rr,r,fi=(np.zeros(n,np.complex) for _ in xrange(7)) 
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
            rr[-ind-1]=(zl[-ind]-z[-ind-1])/(zl[-ind]+z[-ind-1])
            r[-ind-1]=rr[-ind-1]*np.exp(-1j*2*fi[-ind-1])
            zl[-ind-1]=z[-ind-1]*(zl[-ind]*np.cos(fi[-ind-1])+1j*z[-ind-1]*np.sin(fi[-ind-1])) \
                        /(z[-ind-1]*np.cos(fi[-ind-1])+1j*zl[-ind]*np.sin(fi[-ind-1]))
    return r,rr,fi,z
    
def getrefl(ri,tn,n,lam,ia,pol):
    r,rr,fi,z=getr(ri,tn,n,lam,ia,pol)
    return np.absolute(rr[0])**2
#    return rr[0]
    
def getreflc(ri,tn,n,lam,ia,pol):
    r,rr,fi,z=getr(ri,tn,n,lam,ia,pol)
    return rr[0]
     
def getv(ri,tn,n,lam,ia,pol):
    """ get the v or field value on boundary"""
    r,rr,fi,z=getr(ri,tn,n,lam,ia,pol)
    v,vin = ((np.zeros(len(r),np.complex)) for _ in xrange(2))
    vin[0]=1.0
    for ind in xrange(len(r)):
        v[ind]=vin[ind]*(1+rr[ind])*np.exp(-1j*fi[ind])
        if ind==len(r)-1:
            break            
        else:
            vin[ind+1]=v[ind]/(1+r[ind+1])
    tran=np.absolute(vin[-1])**2/np.absolute(vin[0])**2/np.conj(z[-1])*np.conj(z[0])
    return tran,vin,v,z
    
def gettran(ri,tn,n,lam,ia,pol):
    tran,vin,v,z=getv(ri,tn,n,lam,ia,pol)
    return tran
    

