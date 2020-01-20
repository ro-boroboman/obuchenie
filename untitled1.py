# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 17:15:40 2020

@author: maosun
"""
import numpy as np
x = np.random.normal(loc=1, scale=10, size=(10,3));
m = np.mean(x, axis=0);
std = np.std(x, axis=0);
X_norm =((x-m)/std);
"print (X_norm);"
Z = np.array([[4, 5, 0],[1, 9, 3],              
             [5, 1, 1],
             [3, 3, 3], 
             [9, 9, 9], 
             [4, 7, 1]]);
r = np.sum(Z, axis=1);
print (np.nonzero(r>10));
k = np.count_nonzero(Z, axis=1);
print(k);



