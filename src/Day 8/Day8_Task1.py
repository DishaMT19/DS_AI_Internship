# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 11:56:49 2026

@author: disha
"""

import numpy as np


import numpy as np
data=np.arange(24)
reshaped=data.reshape(4,3,2)
transposed=reshaped.transpose(1,0,2)
print("Final shape:\n",transposed.shape)
print("Final array:\n",transposed)
