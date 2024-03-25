# -*- coding: utf-8 -*-
"""
Author: Ethan Polley
Version: 3/21/24

To run computation on Garching data & create figures
for the Mass vs. Pr and magnitudes.
"""

import matplotlib.pyplot as plt
import numpy as np

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
    #The mass equation left in solar mass
    mass = 10 ** alpha + (v/v_constant) ** beta
    
    return mass

#Import the data, Home computer
#pr, w1, w2, w3, w4, v_disp = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/GitHub/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_corrected.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
#pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/Github/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_NM.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
#Import the data, Lab computer
pr, w1, w2, w3, w4, v_disp = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_3arcsec_corrected_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_3arcsec_NM_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)

#Iterate through the objects to creeate a list of masses
masses_3m = []
masses_3nm = []
n = 0
for n in range(len(v_disp)):
    masses_3m.append(Mass(v_disp[n])) #Added each mass to the list
    masses_3nm.append(Mass(v_disp_nm[n]))


