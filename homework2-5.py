#!/usr/bin/python
# -*- coding: utf-8 -*-
#copyRight by heibanke 

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('OutOrder.csv',encoding='gb2312')

a = data[u'方式'].values

#获取类型
type_name=[]
for i in a:
    if i not in type_name:
        type_name.append(i)

print type_name

#对不同类型求和        
type_num = []
for i in type_name:
    type_num.append(sum(a==i))

print type_num

plt.axis('equal')
plt.pie(type_num,labels=type_name,shadow=True,
        labeldistance=1.1,autopct='%3.1f%%',
            startangle=0,pctdistance=0.8)
plt.legend()

plt.show()