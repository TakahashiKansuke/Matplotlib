#!/usr/bin/python
# -*- coding: utf-8 -*-
#copyRight by heibanke 

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import datetime

data = pd.read_csv('OutOrder.csv',encoding='gb2312')

def toDT(a):
    return datetime.datetime.strptime(a,'%m/%d/%Y %H:%M')

# 转换str成datetime格式
a = data[u'时间'].apply(toDT)  #pd.to_datetime(data[u'时间'])

# X用来存月份，Y用来存金额，Z用来存人数
X=[];Y=[];Z=[]

for i in xrange(12):
    start_day = datetime.datetime(2015,i+1,01)
    if i+2>12:
        end_day = datetime.datetime(2016,01,01)
    else:
        end_day = datetime.datetime(2015,i+2,01)
        
    idx = np.where((a>start_day)&(a<end_day))
    if len(idx[0])>0:
        X.append(i+1)
        Y.append(sum(data[u'金额'].values[idx[0]]))
        Z.append(len(idx[0]))

width = 0.25

fig, ax1 = plt.subplots()
ax1.bar(np.array(X)-width, Y, width, facecolor='#9999ff', edgecolor='white')
ax1.set_ylabel('money', color='b')
ax1.set_xlabel('month')

ax2 = ax1.twinx()
ax2.bar(X, Z, width, facecolor='#ff9999', edgecolor='white')
ax2.set_ylabel('people num', color='r')
plt.grid(True)
plt.show()