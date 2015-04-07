# -*- coding: utf-8 -*-
"""
Created on Fri Jun 27 09:25:52 2014

@author: Josh

Expand mode based on mode profile
"""

import numpy as np 
import numpy.fft as fft 
import matplotlib.pyplot as plt
import pwe.pwefft as pf
import multi.myconst as mc
import multi.getmedia3 as gm3
import multi.tmrefl3 as tr3
import pwe.reconwvg as rw
import pwe.getbeta as gb
import pwe.getoverlap as go
from matplotlib.backends.backend_pdf import PdfPages

#x=np.linspace(-4,4,512)
#wid_sweep=np.linspace(0.4,1,10)
wid_sweep=np.linspace(0.1,0.9,5)
lam=.86
[nc,nf,ns]=[3.24,3.6,3.24]
xm=max(8*lam,10*max(wid_sweep))
# use at least 15*lam and 1024 for TM
#xm=max([8*lam,20*max(wid_sweep),10])
x512=np.linspace(-xm,xm,1024)
pol='TE'
m=1

k=2*np.pi
#mlist=range(4)
#for mind in xrange(3):


#for wind in xrange(len(wid_sweep)):
x=x512
r2_ovl=np.zeros(len(wid_sweep))
for ind_p in np.arange(len(wid_sweep)):
#    wid=0.26
    #wid=wid_sweep[wind]
    #    print wid
    wid=wid_sweep[ind_p]
    x=x512
    lam=0.86
    m=0
#    print 'x=',max(x)
    x,ita,be,fzx,fxx,fyx=gb.getmode(x,m,wid,nc,nf,ns,lam,pol)
#    print 'x=',max(x)
    x,s,fx,fft_fx,ifx,fx_cross=rw.getfxyz2(x,be,fzx,fxx,fyx)   
#    print 'x=',max(x)
    ri,tn,n,lam=gm3.getmedia('air');
    ne,tin=rw.getne(s,be)
    #    tin=tin*180/np.pi
    """"""""""""""""""""""""""""""""""""""""""""""""""""""""
    lam=0.86*1e-6
    refl,tran,r,v=(np.zeros(len(tin),dtype=complex) for _ in xrange(4))
    for ind in xrange(len(tin)):
        ri[0]=ne[ind]
        refl[ind]=tr3.getrefl(ri,tn,n,lam,tin[ind],pol)
        tran[ind]=tr3.gettran(ri,tn,n,lam,tin[ind],pol)
    r=pf.getifftr(fx,x,refl,pol)
    r_cross=pf.getifftrc(fx,x,refl,ne,tin,pol)
    po,pi,r2_ovl1=go.getovl1(fx,r,x,ita,tin)
    #print 'mark'
    po_all,pi_all,r_all1=go.getall(fx,r,x,ita,tin)
    r2_all2,r2_ovl2=go.getovl2(r,r_cross,fx,fx_cross,x,pol)
    #print po,pi,r2_ovl,po_all,pi_all,r_all,pout,pin,r_all2
    print r_all1,r2_ovl1,r2_all2,r2_ovl2**2,wid,be/2/np.pi
    r2_ovl[ind_p]=r2_ovl2**2
    

#plt.plot(x,np.imag(fx),x,np.imag(ifx),'--r')

#plt.figure(1)
##plt.subplot(411)
#plt.plot(x,fx,x,ifx,'<')
#plt.subplot(211)
#plt.plot(x,fx,'-.',x,ifx,x,np.real(r),'-r',x,np.imag(r),
#         '--r',x,abs(r),'b') 
#plt.legend(['fx','inv_fx','inv_r_real','inv_r_imag','inv_r'])
#plt.xlim([-5,8])
#plt.subplot(212)
#plt.plot(x,np.real(r_cross),'-.r',x,np.imag(r_cross),'--r',x,abs(r_cross),'r',
#         x,np.real(fx_cross),'-.b',x,np.imag(fx_cross),'--b',x,abs(fx_cross),'b') 
#plt.legend(['rc_real','rc_imag','rc','fc_real','fc_imag','fc_abs'],loc='right')
#plt.xlim([-1,4])
##
##
#plt.figure(2)
#plt.subplot(211)
#plt.title('$FFT_{fx}$')
#plt.plot(tin,np.abs(fft_fx))
#plt.xlabel('Incident Angle (deg)')
#plt.subplot(212)
#plt.plot(s/k,np.abs(fft_fx))
#plt.xlabel('Spatial Frequency')
#plt.xlim([-10,10])
#plt.tight_layout()
##
#plt.figure(3)
##plt.subplot(414)
#plt.plot(tin,np.real(refl),'-->',tin,np.imag(refl),'--<',tin,np.abs(refl),'r')
#plt.legend(['Re(refl)','Im(refl)','ABS(refl)'],loc='best') 

#plt.figure(4)
#plt.plot(x,np.imag(fxx)/fx)
#plt.legend(['Re(refl)','Im(refl)'],loc='best') 
#plt.xlim([-3,3])

fig=plt.figure(1)
plt.rc('text',usetex=True)
plt.plot(wid_sweep,r2_ovl,'-*')
#plt.legend(['Re(refl)','Im(refl)'],loc='best') 
plt.title('TE')
plt.xlabel('Core Width (${\mu}m$)')
plt.ylabel('OVL Reflection to Src')
plt.xlim([0,1])
#plt.ylim([0.28,0.42])
plt.ylim([0.0,0.99])
plt.grid(color='r',linestyle='-.')
fig.set_size_inches(5,4)
plt.savefig('te.png',bbox_inches='tight',pad_inches=0.1,dpi=600)
#pp=PdfPages('fig/te.pdf')
#pp.savefig(bbox_inches='tight',pad_inches=0.1,dpi=600)
#plt.close()
#pp.close()


