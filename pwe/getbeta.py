# -*- coding: utf-8 -*-
"""
Solve 2D wvg's eigen value based on EWA pg.405
"""

import numpy as np
import myconst as mc
import matplotlib.pyplot as plt

def getbeta(nc,nf,ns,wid,lam,pol):
    """From index thinkness wavelength and polarization obtain modes
    
    :param nc: core index
    :param nf: superstrate index
    :param ns: substrate index
    :param wid: width of core, can be unitless
    :param lam: wavelength, can be unitless
    :param pol: polarization, "TE" or "TM"
    :type pol: str 

    Examples::

	kf,gs,gc,beta,phi,M,ps,pc,pol=getbeta(1.,1.9627,1,0.75,0.8,'TE')
	
    """
    a=wid/2./lam  
    k=2*np.pi
    R=k*a*np.sqrt(nf**2-ns**2)
    dta=(ns**2-nc**2)/(nf**2-ns**2)
    
    if pol=='TE':
        ps=1
        pc=1
    else:
        ps=nf**2/ns**2
        pc=nf**2/nc**2
        
    M=int(np.floor((2*R-np.arctan(pc*np.sqrt(dta)))/np.pi))
#    print 'dta=',dta,'R=',R
#    print (2*R-np.arctan(pc*np.sqrt(dta)))/np.pi
    
#    print 'M=', M
    
    u=R*np.ones(M+1)
    v=np.zeros(M+1)
    w=R*np.sqrt(dta)*np.ones(M+1)
    kf=np.zeros(M+1)   
    gs=np.zeros(M+1)
    gc=np.zeros(M+1)
    beta=np.zeros(M+1)
    phi=np.zeros(M+1)
   
    r=0.3
    tol=1e-13
    for m in xrange(M+1):
        Nit=1
        while Nit<1000:
            unew=r*(m*np.pi/2.+np.arctan(ps*v[m]/u[m])/2.+np.arctan(pc*w[m]/u[m])/2.)+(1-r)*u[m]
            if abs(unew-u[m])**2<=tol:
                break
            Nit=Nit+1
            u[m]=unew
            v[m]=np.sqrt(R**2-u[m]**2)
            w[m]=np.sqrt(R**2*dta+v[m]**2)
#        print Nit,unew,m,u[m],v[m],w[m]
        kf[m]=u[m]/a
        gs[m]=v[m]/a
        gc[m]=w[m]/a
        beta[m]=np.sqrt(nf**2*k**2-kf[m]**2)
        phi[m]=0.5*m*np.pi+0.5*np.arctan(pc*gc[m]/kf[m])-0.5*np.arctan(ps*gs[m]/kf[m])
#        print m,ps,pc,kf[m],gs[m],gc[m],beta[m],phi[m]
    return kf,gs,gc,beta,phi,M,ps,pc,pol
    
def getmode(x,m,wid,nc,nf,ns,lam,pol):
    """Obtain field profile from mode solver

    :param x: lateral range that are unitless, will be normalized in code
    :type x: float array
    :param m: mode order in int
    :param nc,nf,ns: index of cladding and core
    :param lam: wavelength unitless
    :type lam: float
    :param pol: polarization in "TE" or "TM"
    :returns: length scale and E-field for either TE or TM

    Examples::

        x,fzx,fxx,fyx=getmode(np.linspace(-4,4,401),0,1,1,3.5,1.45,1.55,'TE')

    """
    k=2*np.pi
    a=wid/2./lam
    kf,gs,gc,beta,phi,M,ps,pc,pol=getbeta(nc,nf,ns,wid,lam,pol)
    
    x=x/lam  
    fzx=np.zeros(len(x),complex)
    fyx=np.zeros(len(x),complex)
    fxx=np.zeros(len(x),complex)
    nn=np.zeros(len(x),complex)
    ita=np.zeros(len(x),complex)
#    print x,a
     
    for ind in xrange(len(x)):
        if x[ind]<-a:
            fzx[ind]=-np.sin(kf[m]*a-phi[m])*np.exp(gs[m]*(x[ind]+a))
            fxx[ind]=1j*beta[m]/gs[m]*fzx[ind]
            nn[ind]=ns**2
#            print '1*'
        elif x[ind]<=a:            
            fzx[ind]=np.sin(kf[m]*x[ind]+phi[m])
            fxx[ind]=-1j*beta[m]/kf[m]*np.cos(kf[m]*x[ind]+phi[m])
            nn[ind]=nf**2
#            print '2*'
        else:
            fzx[ind]=np.sin(kf[m]*a+phi[m])*np.exp(-gc[m]*(x[ind]-a))
            fxx[ind]=-1j*beta[m]/gc[m]*fzx[ind]
            nn[ind]=nc**2
#            print '3*'
        if pol=='TE':
            ita[ind]=k/beta[m]*mc.c0*mc.mu0
            fyx[ind]=-ita[ind]*fxx[ind]
#            norm=max(np.imag(fyx))
#            fyx[ind]=fyx[ind]/norm
#            fzx[ind]=fzx[ind]/norm
#            fxx[ind]=fxx[ind]/norm
        else:
            ita[ind]=beta[m]/mc.eps0/nn[ind]/k/mc.c0
            fyx[ind]=fxx[ind]/ita[ind]
    
#    print 'width=',2*a*lam

    return x,ita,beta[m],fzx,fxx,fyx

if __name__ == "__main__":
    print "Get mode"
