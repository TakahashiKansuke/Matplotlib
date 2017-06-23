#!/usr/bin/python
# -*- coding: utf-8 -*-
#copyRight by heibanke 

import matplotlib.pyplot as plt

from homework2_3 import gen_circle_point

N=16

fig = plt.figure()

for p1,p2 in gen_circle_point(N):
    plt.plot(p1[0],p1[1],'b.')
    plt.plot(p2[0],p2[1],'r')

#plt.xlim([-N,N])
#plt.ylim([-N,N])

#plt.xlim([-N/2,N/2])
#plt.ylim([-N/2,N/2])
plt.show()