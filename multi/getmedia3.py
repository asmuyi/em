# -*- coding: utf-8 -*-
"""
getmedia3.py, obtain the media n and d from stack.dat
Created on Mon Jun  9 21:34:41 2014
Revised on Sat Jun 14 2014
Add transverse anisotropy on July 1 2014

@author: asmuyi
"""
import numpy as np
import tools.conunit as cu
#import getuser as gu
import tools.genarray as ga


def findmdc(media):
    with open('stack.dat') as fp:
        for num,line in enumerate(fp,1):
            if media in line:
                lam_str = next(fp)
                ri_str = next(fp)
                tn_str = next(fp)
#                print ri_str,tn_str
                return ri_str,tn_str,lam_str
                
def getn(ri_str):
    ri_arr=ri_str.split(' ')
    temp_array=np.zeros([len(ri_arr),3],dtype=np.complex)
    for ind in xrange(len(ri_arr)):
        if '[' in ri_arr[ind]:
            arr_comp=ri_arr[ind].split(')(')
            for i3 in np.arange(len(arr_comp)):
                re=float(arr_comp[i3].strip('[').strip(']').strip('(').strip(')').split(',')[0])
                im=float(arr_comp[i3].strip('[').strip(']').strip('(').strip(')').split(',')[1])
                temp_array[ind][i3]=complex(float(re),-float(im))
            
        elif '(' in ri_arr[ind]:
            arr_comp=ri_arr[ind].split(',')
            re=arr_comp[0].strip('(')
            im=arr_comp[1].strip(')')
            temp_array[ind]=complex(float(re),-float(im))
        else:    
            temp_array[ind]=float(ri_arr[ind])
#            print temp_array[ind]
    return temp_array
    
def getd(tn_str,lam_str):
    lam=cu.convlen(lam_str)
    tn_arr=tn_str.split(' ')
    d_array=np.zeros(len(tn_arr),dtype=np.float)     
#    print tn_arr
    for ind in xrange(len(tn_arr)):
#        print tn_arr[ind]
        if tn_arr[ind].strip('\n')=='inf':
            d_array[ind]=lam*10
#            print 'inf=2lam'
        else:
            d_array[ind]=cu.convlen(tn_arr[ind])
#            print 'num=num'
    return d_array,lam
#    return lam
            
def getmedia(media):
    if 'user' not in media:
        ri_str,tn_str,lam_str=findmdc(media)
        ri=getn(ri_str)
        tn,lam=getd(tn_str,lam_str)
    #    lam=getd(tn_str,lam_str)
        n=len(ri)
    #    print tn_str,lam_str       
    elif media=='user':
        ri,tn,lam,n=gu.getuser()
    else:
        ms=media.split(' ')
        med,par,val=ms[1],ms[2],ms[3]
        gu.getsweep(med,par,val)
        
    return ri,tn,n,lam
    
#print getmedia('sp-lu')   
#rr,tt,ln,nn=getmedia('sp-lu')
