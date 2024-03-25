# -*- coding: utf-8 -*-
"""
Author: Ethan Polley
Version: 3/21/24

To run computation on Garching data & create figures
for the Mass vs. Pr and magnitudes.
"""

import matplotlib.pyplot as plt
import numpy as np
import math

#The velocity dispersion used as a constant to compare other velocity distributions
v_constant = 200 # km/s
#Alpha and Beta are the fit and slope respectively, set to current model use
alpha = 8.22 # +/- .06
beta = 4.86 # +/- .43

def Mass(v):
    """
    This function is used to calculate the mass of all objects in
    the dataset. This is done using the velocity dispersion and
    the relationshiop between the two.

    Parameters
    ----------
    v : float
        The velocity dispersion of the object being measured.

    Returns
    -------
    mass : float
        The mass of the object based on velocity dispersion (in solar mass).

    """
    #This variable is just an unecessary extra step to simply the mass equation
    dummy_variable = alpha + beta * math.log(v/v_constant)
    #The mass equation
    mass = 10 ** dummy_variable # In solar mass
    return mass


pr, w1, w2, w3, w4, v_disp = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/GitHub/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_corrected.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)


masses = []
n = 0
while n < len(v_disp):
    masses.append(Mass(v_disp[n]))
    n += 1

print(len(v_disp), len(masses))
