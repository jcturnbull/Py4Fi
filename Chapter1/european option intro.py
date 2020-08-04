#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 10:12:39 2020

@author: jacksonturnbull
"""

#Finance and Python Syntax p14
## MC for EUR Options
S0 = 100.
K = 105.
T = 1.0
r = 0.05
sigma = 0.2

from numpy import *

I = 100000

z = random.standard_normal(I)
ST = S0*exp((r - 0.5*sigma**2)*T+sigma*sqrt(T)*z)
hT = maximum(ST-K,0) #MC estimator fxn, end time payoff
C0 = exp(-r*T)*sum(hT)/I

print("Value of the European Call Option %5.3f" % C0)