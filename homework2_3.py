#!/usr/bin/python
# -*- coding: utf-8 -*-
#copyRight by heibanke 

import numpy as np

def gen_circle_point(N):
    """
    return p=(p1,p2)
    """
    if N<3:
        assert False,"N is too small"
    
    t = np.linspace(0, np.pi*2, N,endpoint=False)
    x = np.sin(t)
    y = np.cos(t)

    
    #找到外切圆半径 l和第一个点 A
    theta = np.pi*2/N
    
    #决定旋转角度，非常重要的参数
    #r_th = theta*(N/2-1)
    r_th = theta
    
    l = 1/np.cos(r_th/2)
    A=np.array([l*np.sin(r_th/2),1])
    
    p=[]
    
    # 构造旋转矩阵
    rotate_M = np.array([[np.cos(r_th),np.sin(r_th)],[-np.sin(r_th),np.cos(r_th)]])
    
    for i in xrange(len(x)):
        #依次旋转找其他i个点
        B=rotate_M.dot(A)
        p.append(([x[i],y[i]],([A[0],B[0]],[A[1],B[1]])))
        A=B
   
    return p
    
    
if __name__=="__main__":
    for p1,p2 in gen_circle_point(4):
        print p1
        print p2
        print "==================="