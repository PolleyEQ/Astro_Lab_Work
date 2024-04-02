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
    log_mass = alpha + beta * np.log10(v/v_constant)
    
    return log_mass


#%% 3arcseconds

"""#Import the data, Home computer
pr, w1, w2, w3, w4, v_disp = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/GitHub/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_corrected.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/Github/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_NM.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
"""
#Import the data, Lab computer
pr, w1, w2, w3, w4, v_disp = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_3arcsec_corrected_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_3arcsec_NM_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)


"""#Exclude velocity dispersions zero & below
for n in range(len(v_disp)):
    if v_disp[n] <= 0:
        v_disp.remove(n)"""

#Iterate through the objects to creeate a list of masses
masses_m = []
masses_nm = []
for n in range(len(v_disp)): #Iterate over all velocities for masers
    masses_m.append(Mass(v_disp[n])) #Added each mass to the maser list
for n in range(len(v_disp_nm)): #Iterate over all velocities for non-masers
    masses_nm.append(Mass(v_disp_nm[n])) #Add each mass to the non-maser list

plt.figure(num = None)
"""fig, (ax1, ax2) = plt.subplots(1, 2, sharey = True)

ax1.plot(pr, masses_3m, fmt = '*', color = 'blue')
ax1.plot(pr_nm, masses_3nm, fmt = 'o', color = 'red')
ax1.set_ylabel('Mass (in solar masses)')
ax1.set_xlabel('PR')
ax2.plot(w1, masses_3m, fmt = '*', color = 'blue')
ax2.plot(w1_nm, masses_3nm, fmt = 'o', color = 'red')
ax2.set_xlabel('W1')
plt.legend(['Masers', 'Non-masers'])
plt.yscale('Log')
plt.show()
"""

plt.errorbar(pr_nm, masses_nm, fmt = 'o', color = 'grey')
plt.errorbar(pr, masses_m, fmt = '*', color = 'blue')
plt.ylabel('Log of Black Hole Mass (in solar masses)')
plt.xlabel('PR')
plt.legend(['Non-Masers', 'Masers'])

#%% 4arcseconds

"""#Import the data, Home computer
pr, w1, w2, w3, w4, v_disp = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/GitHub/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_corrected.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/Github/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_NM.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
"""
#Import the data, Lab computer
pr, w1, w2, w3, w4, v_disp = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_4arcsec_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_4arcsec_NM_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)

#Iterate through the objects to creeate a list of masses
masses_m = []
masses_nm = []
for n in range(len(v_disp)): #Iterate over all velocities for masers
    masses_m.append(Mass(v_disp[n])) #Added each mass to the maser list
for n in range(len(v_disp_nm)): #Iterate over all velocities for non-masers
    masses_nm.append(Mass(v_disp_nm[n])) #Add each mass to the non-maser list

plt.figure(num = None)

plt.errorbar(pr_nm, masses_nm, fmt = 'o', color = 'grey')
plt.errorbar(pr, masses_m, fmt = '*', color = 'blue')
plt.ylabel('Log of Black Hole Mass (in solar masses)')
plt.xlabel('PR')
plt.legend(['Non-Masers', 'Masers'])


#%% 5arcseconds

"""#Import the data, Home computer
pr, w1, w2, w3, w4, v_disp = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/GitHub/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_corrected.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/Github/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_NM.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
"""
#Import the data, Lab computer
pr, w1, w2, w3, w4, v_disp = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_5arcsec_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_5arcsec_NM_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)

#Iterate through the objects to creeate a list of masses
masses_m = []
masses_nm = []
for n in range(len(v_disp)): #Iterate over all velocities for masers
    masses_m.append(Mass(v_disp[n])) #Added each mass to the maser list
for n in range(len(v_disp_nm)): #Iterate over all velocities for non-masers
    masses_nm.append(Mass(v_disp_nm[n])) #Add each mass to the non-maser list

plt.figure(num = None)

plt.errorbar(pr_nm, masses_nm, fmt = 'o', color = 'grey')
plt.errorbar(pr, masses_m, fmt = '*', color = 'blue')
plt.ylabel('Log of Black Hole Mass (in solar masses)')
plt.xlabel('PR')
plt.legend(['Non-Masers', 'Masers'])


#%% 6arcseconds

"""#Import the data, Home computer
pr, w1, w2, w3, w4, v_disp = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/GitHub/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_corrected.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/Github/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_NM.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
"""
#Import the data, Lab computer
pr, w1, w2, w3, w4, v_disp = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_6arcsec_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_6arcsec_NM_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)

#Iterate through the objects to creeate a list of masses
masses_m = []
masses_nm = []
for n in range(len(v_disp)): #Iterate over all velocities for masers
    masses_m.append(Mass(v_disp[n])) #Added each mass to the maser list
for n in range(len(v_disp_nm)): #Iterate over all velocities for non-masers
    masses_nm.append(Mass(v_disp_nm[n])) #Add each mass to the non-maser list

plt.figure(num = None)

plt.errorbar(pr_nm, masses_nm, fmt = 'o', color = 'grey')
plt.errorbar(pr, masses_m, fmt = '*', color = 'blue')
plt.ylabel('Log of Black Hole Mass (in solar masses)')
plt.xlabel('PR')
plt.legend(['Non-Masers', 'Masers'])


#%% 7arcseconds

"""#Import the data, Home computer
pr, w1, w2, w3, w4, v_disp = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/GitHub/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_corrected.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/Github/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_NM.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
"""
#Import the data, Lab computer
pr, w1, w2, w3, w4, v_disp = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_7arcsec_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_7arcsec_NM_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)

#Iterate through the objects to creeate a list of masses
masses_m = []
masses_nm = []
for n in range(len(v_disp)): #Iterate over all velocities for masers
    masses_m.append(Mass(v_disp[n])) #Added each mass to the maser list
for n in range(len(v_disp_nm)): #Iterate over all velocities for non-masers
    masses_nm.append(Mass(v_disp_nm[n])) #Add each mass to the non-maser list

plt.figure(num = None)

plt.errorbar(pr_nm, masses_nm, fmt = 'o', color = 'grey')
plt.errorbar(pr, masses_m, fmt = '*', color = 'blue')
plt.ylabel('Log of Black Hole Mass (in solar masses)')
plt.xlabel('PR')
plt.legend(['Non-Masers', 'Masers'])


#%% 8arcseconds

"""#Import the data, Home computer
pr, w1, w2, w3, w4, v_disp = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/GitHub/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_corrected.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/Github/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_NM.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
"""
#Import the data, Lab computer
pr, w1, w2, w3, w4, v_disp = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_8arcsec_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_8arcsec_NM_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)

#Iterate through the objects to creeate a list of masses
masses_m = []
masses_nm = []
for n in range(len(v_disp)): #Iterate over all velocities for masers
    masses_m.append(Mass(v_disp[n])) #Added each mass to the maser list
for n in range(len(v_disp_nm)): #Iterate over all velocities for non-masers
    masses_nm.append(Mass(v_disp_nm[n])) #Add each mass to the non-maser list

plt.figure(num = None)

plt.errorbar(pr_nm, masses_nm, fmt = 'o', color = 'grey')
plt.errorbar(pr, masses_m, fmt = '*', color = 'blue')
plt.ylabel('Log of Black Hole Mass (in solar masses)')
plt.xlabel('PR')
plt.legend(['Non-Masers', 'Masers'])

#%% Histogram of velocity dispersion (sigma *)

plt.figure()
fig, ax = plt.subplots(figsize = (10, 10))

ax.hist(v_disp['your_column_here'],
        #bins = np.linspace(v_disp['your_column_here'].min(), v_disp['your_column_here'].max(), num = 35, endpoint = False),
        color = "green",
        edgecolor = 'white',
        density = True,
        alpha = 0.6,
        linewidth = 1,
        label = 'masers'
           ) 
ax.hist(v_disp_nm['your_column_here'],
        #bins = np.linspace(v_disp_nm['your_column_here'].min(), v_disp_nm['your_column_here'].max(), num = 35, endpoint = False),
        color = "blue",
        edgecolor = 'white',
        density = True,
        alpha = 0.6,
        linewidth = 1,
        label = 'non-masers'
           )
plt.show()




