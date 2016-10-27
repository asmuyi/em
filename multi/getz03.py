"""Get Z0 impedance of multilayer
Use ncosine as the gauge to get neff and impedance z or reactance y.

"""
from __future__ import absolute_import

import sys
import numpy as np
from tools import myconst as mc

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
    Example::

        getncos(2.00,'TE',45,1.4)
    will return ncos, the impedance and admittance inside n=2.00 material, 
    given by a 'TE' incident light at 45 deg, from n=1.4 material.
    
    """
    neff = rin * np.sin(ia/180.0*np.pi)
    if ri[0]==ri[2]:
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
    #	anisotropic
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
    return ncos,y,z

def getzin(rin,pol,ia):
    """ Get the incident layer's impedance. Important for normalization.

    :param ri: refractive index
    :type ri: complex 
    :param pol: Polarization
    :type pol: str
    :param ia: incident angle
    :type ia: float in deg
    :return: impedance (z) 
    
    """
    neff = rin * np.sin(ia/180.0*np.pi)
    ncos2=rin**2-neff**2
    if ncos2.real<0 and ncos2.imag==0:
        ncos = -np.sqrt(-ncos2)*1j
    else:
        ncos = np.sqrt(ncos2)
    if pol=='TM':
        y=mc.c0*rin**2*mc.eps0/ncos
    else:
        y=ncos/mc.c0/mc.mu0
    return 1./y

if __name__ == "__main__":
    print "The impedance of the first layer is:"
    print "================"
    print getzin(float(sys.argv[1]),str(sys.argv[2]),
	float(sys.argv[3]))/mc.z0

