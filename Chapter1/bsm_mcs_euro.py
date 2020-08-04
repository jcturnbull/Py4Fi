#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 10:19:28 2020

@author: jacksonturnbull
"""


#
# Monte Carlo Valuation of European call option in Black-Scholes-Merton
#bsm-mcs-euro.py

import numpy as np

#Parameter values
S0 = 100.
K = 105.
T = 1.0
r = 0.05
sigma = 0.2

I = 100000

#Valuation Algorithm
z = np.random.standard_normal(I)
ST = S0*np.exp((r-0.5*sigma**2)*T + sigma*np.sqrt(T)*z)
hT = np.maximum(ST-K,0)
C0 = np.exp(-r*T)*np.sum(hT)/I #MC estimator

# Result Output
print("Value of the Euro Call Option %5.3f" % C0)


