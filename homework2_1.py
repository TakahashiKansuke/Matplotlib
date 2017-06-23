#!/usr/bin/python
# -*- coding: utf-8 -*-
#copyRight by heibanke 


from matplotlib import pyplot as plt
import numpy as np

p=np.array([[1,2,3,1],[1,3,0,1]])

theta=np.pi/6
H=np.eye(2)

H=np.array([[np.cos(theta),-np.sin(theta)],
    [np.sin(theta),np.cos(theta)]])

p1 = H.dot(p)
p2 = p-1

p3 = H.dot(p2)
p4 = p3+1

plt.plot(p[0,:],p[1,:],label=u'原始')
plt.plot(p1[0,:],p1[1,:],'r',label=u'旋转by原点')
plt.plot(p2[0,:],p2[1,:],'y',label=u'移位一次')
plt.plot(p4[0,:],p4[1,:],'g',label=u'旋转by顶点')

plt.xlim([-2,4])
plt.ylim([-2,4])

plt.grid(True)
plt.legend()
plt.show()