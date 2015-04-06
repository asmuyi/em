# -*- coding: utf-8 -*-
"""
Calculate ncos, y, z of each layer.
Media info from getneff3.

"""
import numpy as np
import tools.myconst as mc
import getneff3 as gn3
import getmedia3 as gm3
from tools.myconst import eps0,mu0,c0

def getncos(ri,pol,ia,rin):
    """ Obtain index*cos(beam_angle) and return impedance of each layer.

    :param ri: refractive index
    :type ri: complex 
    :param pol: Polarization
    :type pol: str
    :param ia: incident angle
    :type ia: float in deg
    :param rin: refractive index of input material
    :type rin: complex
    :return: ncos, impedance (z) and admittance (y)
    
    """
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
    
    if __name__ == "__main__":
        print "Running getz03"
