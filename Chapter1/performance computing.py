#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 15:20:03 2020

@author: jacksonturnbull
"""

"""
# run in the console
#IPython Magic commands
loops = 25000000
from math import *

#first loop calculation
a = range(1,loops)
def f(x):
    return 3* log(x) + cos(x)**2
%timeit r = [f(x) for x in a]

#second loop calculation
import numpy as np
b = np.arange(1, loops)
%timeit r = 3*np.log(b)+np.cos(b)**2

#third loop calculation
import numexpr as ne
ne.set_num_threads(1)
f = '3 * log(b) + cos(b)**2'
%timeit r = ne.evaluate(f)

#fourth, parallelization
#uses numexpr
#8 cores detected but my computer is quadcore, so 4 are used
ne.set_num_threads(4)
%timeit r = ne.evalutate(f)
"""
