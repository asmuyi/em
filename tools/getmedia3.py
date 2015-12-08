"""Obtain the media n and d from a text style such as stack.dat
Add transverse anisotropy on July 1 2014

"""
import sys
import numpy as np
import tools.conunit as cu
#import getuser as gu
import tools.genarray as ga


def findmdc(mediatable,medianame):
    """ Find multilayer property from text file.
    
    The text file "stack.dat" has the style of::

    mdc media_code
    800nm
    1.0 (2.1,0.3) 1.5
    inf 50nm inf

    or for anisotropic::

    800nm
    1.0 [(3,1)(2.1,0.3)(2.1,0.3)] 1.5
    inf 50nm inf

    This function simply reads in the wavelength, refractive index and
    thickness and stores them in string form.

    :param mediatable: mediatable in string
    :param medianame: media name in string
    :return:  ri_str,tn_str,lam_str in string
    :rtype: string tuple

    """
    with open(mediatable) as fp:
        for num,line in enumerate(fp,1):
            if medianame in line:
                lam_str = next(fp)
                ri_str = next(fp)
                tn_str = next(fp)
                return ri_str,tn_str,lam_str
                
def getn(ri_str):
    """ Get refractive index
    
    :param ri_str: refractive index string from findmdc
    :return ri_float: refractive index in float
    :rtype: float 
    """
    ri_arr=ri_str.split(' ')
    ri_float=np.zeros([len(ri_arr),3],dtype=np.complex)
    for ind in xrange(len(ri_arr)):
        if '[' in ri_arr[ind]:
            arr_comp=ri_arr[ind].split(')(')
            for i3 in xrange(len(arr_comp)):
                re=float(arr_comp[i3].strip('[').strip(']').
		    strip('(').strip(')').split(',')[0])
                im=float(arr_comp[i3].strip('[').strip(']').
		    strip('(').strip(')').split(',')[1])
                ri_float[ind][i3]=complex(float(re),-float(im))
            
        elif '(' in ri_arr[ind]:
            arr_comp=ri_arr[ind].split(',')
            re=arr_comp[0].strip('(')
            im=arr_comp[1].strip(')')
            ri_float[ind]=complex(float(re),-float(im))
        else:    
            ri_float[ind]=float(ri_arr[ind])
#            print temp_array[ind]
    return ri_float
    
def getd(tn_str,lam_str):
    """ Get thickness.
    
    :param tn_str: thickness in string
    :param lam_str: wavelength in string
    :return: thickness list, wavelength
    :rtype: float
    """
    lam=cu.convlen(lam_str)
    tn_arr=tn_str.split(' ')
    tn_float=np.zeros(len(tn_arr),dtype=np.float)     
    for ind in xrange(len(tn_arr)):
        if tn_arr[ind].strip('\n')=='inf':
            tn_float[ind]=lam*10
        else:
            tn_float[ind]=cu.convlen(tn_arr[ind])
    return tn_float,lam
            
def getmedia(mediatable,medianame):
    if 'user' not in medianame:
        ri_str,tn_str,lam_str=findmdc(mediatable,medianame)
        ri=getn(ri_str)
        tn,lam=getd(tn_str,lam_str)
        n=len(ri)
    """
    elif media=='user':
        ri,tn,lam,n=gu.getuser()
    else:
        ms=media.split(' ')
        med,par,val=ms[1],ms[2],ms[3]
        gu.getsweep(med,par,val)
    """     
    return ri,tn,n,lam
    
def getindex(mediatable,medianame):
    """Get index of multilayer.
    
    """
    media=getmedia(mediatable,medianame)
    return media[0]

def getthickness(mediatable,medianame):
    """Get thickness of multilayer.
    
    """
    media=getmedia(mediatable,medianame)
    return media[1]

def getnlayer(mediatable,medianame):
    """Get layer number  of multilayer.
    
    """
    media=getmedia(mediatable,medianame)
    return media[2]

def getwavelength(mediatable,medianame):
    """Get wavelength (single value).
    
    """
    media=getmedia(mediatable,medianame)
    return media[3]

if __name__ == "__main__":
    print "This script run needs a valid stack.dat file"
    print "==================="
    print "Layer count: ", getnlayer(sys.argv[1],sys.argv[2])
    print "index: ", getindex(sys.argv[1],sys.argv[2]) 
    print "thickness: ", getthickness(sys.argv[1],sys.argv[2])
    print "wavelength: ", getwavelength(sys.argv[1],sys.argv[2]) 
