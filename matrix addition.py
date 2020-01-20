# -*- coding: utf-8 -*-
"""
Created on Mon Jan 20 18:30:33 2020

@author: maosun
"""
import numpy as np;
a = np.eye(3);
b = np.eye(3);

AB = np.vstack((b, a));
print (AB);