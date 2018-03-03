# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 13:57:29 2017

@author: Joshua
"""

import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append(r'C:/Users/Joshua/Documents/Code/toolbox/')
from datareader import *
import xrdmlRead as xr
savehere = r'C:/Users/Joshua/Desktop/'




data, filenames = dataReader().getOutput()
try:
    if isinstance(data, list):
        activate(data[0])
    else:
        activate(data)
except AttributeError:
    print('No file generated')
except IndexError:
    print('Data just ain\'t there')
from datareader import *