# -*- coding: utf-8 -*-
"""
Example with sp-lu

@author: asmuyi
"""

import numpy as np
import getmedia3 as gm3
import myconst as mc
import tmrefl3 as tr3
import matplotlib.pyplot as plt
#from matplotlib.backends.backend_pdf import PdfPages

""" Change media name and specify the inc angle range and polarization"""
media='sp-lu'
tin=np.linspace(0,90,901)
t0=tin
pol='TM'
""""""""""""""""""""""""""""""""""""""""""""""""""""""""

refl,tran,v=(np.zeros(len(tin),dtype=complex) for _ in xrange(3))
ri,tn,n,lam=gm3.getmedia(media)
for ind in xrange(len(tin)):
    refl[ind]=tr3.getrefl(ri,tn,n,lam,tin[ind],pol)
    tran[ind]=tr3.gettran(ri,tn,n,lam,tin[ind],pol)
x=t0
ytm = refl;

fig=plt.figure()
plt.plot(x,ytm,'-*')
plt.xlabel('angle',fontsize=12)
plt.ylabel('refl',fontsize=12)
plt.legend(['model (tmm)'],loc='upper left')
plt.ylim(0.0,1.0)
plt.grid(color='r',linestyle='-.')
plt.title('sp-lumerical')
fig.set_size_inches(5,4)
plt.savefig('plw.png')
