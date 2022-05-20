# -*- coding: utf-8 -*-
"""
Created on Thu May 19 15:04:47 2022

@author: jirap
"""
import math 
import numpy

def findpi(n):
    a = 45
    x = math.sqrt(2)*0.5
    e = 4.0
    for i in range(n):
        a /= 2
        x = x/(2*math.cos(numpy.deg2rad(a)))
        e *= 2
        d = x*e
        
    
    return d

print(findpi(500))
