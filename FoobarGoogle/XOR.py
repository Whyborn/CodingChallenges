#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 22:46:51 2021

@author: lachlan
"""

def XOR(n,m):
    checksum = 0
    for num in range(n, m+1):
        checksum ^= num
        
    return checksum

#n,m n%4=0 [1, m+1, 0, m]
#n,m n%4=1 [m+1, 0, m, 1]
#n,m n%4=2 [1, m+1, 0, m]