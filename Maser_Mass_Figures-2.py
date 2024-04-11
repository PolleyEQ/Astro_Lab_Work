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
alpha = 8.13 # +/- .06
beta = 4.02 # +/- .43

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


def exp_value(data):
    """
    This function is used to calculate the expectation value of a 
    data set.

    Parameters
    ----------
    data : list
        A list of values.

    Returns
    -------
    value : float
        The expectation value of the dataset.

    """
    x = 0
    for i in data:
        x += i
    
    y = len(data)
    value = x / y
    return value


#%% 3arcseconds

"""#Import the data, Home computer
pr, w1, w2, w3, w4, v_disp = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/GitHub/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_corrected.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/Github/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_NM.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
"""
#Import the data, Lab computer
pr, w1, w2, w3, w4, v_disp = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_3arcsec_corrected_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_3arcsec_NM_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)


#Exclude velocity dispersions zero & below
pr, w1, w2, w3, w4, v_disp = list(pr), list(w1), list(w2), list(w3), list(w4), list(v_disp)
for i in v_disp:
    if i <= 0:
        zero = v_disp.index(i)
        v_disp.remove(i)
        pr.pop(zero)
        w1.pop(zero)
        w2.pop(zero)
        w3.pop(zero)
        w4.pop(zero)

pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = list(pr_nm), list(w1_nm), list(w2_nm), list(w3_nm), list(w4_nm), list(v_disp_nm)
for i in v_disp_nm:
    if i <= 0:
        zero = v_disp_nm.index(i)
        v_disp_nm.remove(i)
        pr_nm.pop(zero)
        w1_nm.pop(zero)
        w2_nm.pop(zero)
        w3_nm.pop(zero)
        w4_nm.pop(zero)

#Iterate through the objects to creeate a list of masses
masses_m = []
masses_nm = []
for n in range(len(v_disp)): #Iterate over all velocities for masers
    masses_m.append(Mass(v_disp[n])) #Added each mass to the maser list
for n in range(len(v_disp_nm)): #Iterate over all velocities for non-masers
    masses_nm.append(Mass(v_disp_nm[n])) #Add each mass to the non-maser list

w12 = []
w12_nm = []
for i in range(len(v_disp)):
    w12.append(w1[i]-w2[i])
for i in range(len(v_disp_nm)):
    w12_nm.append(w1_nm[i] - w2_nm[i])

plt.figure(num = None)
fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize = (12, 6), sharey = True)

ax1.scatter(pr_nm, masses_nm, color = 'grey')
ax1.scatter(pr, masses_m, color = 'blue')
ax1.set_ylabel('Mass (in solar masses)')
ax1.set_xlabel('PR')
ax2.scatter(w1_nm, masses_nm, color = 'grey')
ax2.scatter(w1, masses_m, color = 'blue')
ax2.set_xlabel('W1')
ax3.scatter(w2_nm, masses_nm, color = 'grey')
ax3.scatter(w2, masses_m, color = 'blue')
ax3.set_xlabel('W2')
ax4.scatter(w12_nm, masses_nm, color = 'grey')
ax4.scatter(w12, masses_m, color = 'blue')
ax4.set_xlabel('W1 - W2')
ax1.legend(['Masers', 'Non-masers'])
plt.tight_layout()
plt.show()


#%% 4arcseconds

"""#Import the data, Home computer
pr, w1, w2, w3, w4, v_disp = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/GitHub/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_corrected.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/Github/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_NM.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
"""
#Import the data, Lab computer
pr, w1, w2, w3, w4, v_disp = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_4arcsec_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_4arcsec_NM_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)


#Exclude velocity dispersions zero & below
pr, w1, w2, w3, w4, v_disp = list(pr), list(w1), list(w2), list(w3), list(w4), list(v_disp)
for i in v_disp:
    if i <= 0:
        zero = v_disp.index(i)
        v_disp.remove(i)
        pr.pop(zero)
        w1.pop(zero)
        w2.pop(zero)
        w3.pop(zero)
        w4.pop(zero)

pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = list(pr_nm), list(w1_nm), list(w2_nm), list(w3_nm), list(w4_nm), list(v_disp_nm)
for i in v_disp_nm:
    if i <= 0:
        zero = v_disp_nm.index(i)
        v_disp_nm.remove(i)
        pr_nm.pop(zero)
        w1_nm.pop(zero)
        w2_nm.pop(zero)
        w3_nm.pop(zero)
        w4_nm.pop(zero)

#Iterate through the objects to creeate a list of masses
masses_m = []
masses_nm = []
for n in range(len(v_disp)): #Iterate over all velocities for masers
    masses_m.append(Mass(v_disp[n])) #Added each mass to the maser list
for n in range(len(v_disp_nm)): #Iterate over all velocities for non-masers
    masses_nm.append(Mass(v_disp_nm[n])) #Add each mass to the non-maser list

w12 = []
w12_nm = []
for i in range(len(v_disp)):
    w12.append(w1[i]-w2[i])
for i in range(len(v_disp_nm)):
    w12_nm.append(w1_nm[i] - w2_nm[i])

plt.figure(num = None)
fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize = (12, 6), sharey = True)

ax1.scatter(pr_nm, masses_nm, color = 'grey')
ax1.scatter(pr, masses_m, color = 'blue')
ax1.set_ylabel('Mass (in solar masses)')
ax1.set_xlabel('PR')
ax2.scatter(w1_nm, masses_nm, color = 'grey')
ax2.scatter(w1, masses_m, color = 'blue')
ax2.set_xlabel('W1')
ax3.scatter(w2_nm, masses_nm, color = 'grey')
ax3.scatter(w2, masses_m, color = 'blue')
ax3.set_xlabel('W2')
ax4.scatter(w12_nm, masses_nm, color = 'grey')
ax4.scatter(w12, masses_m, color = 'blue')
ax4.set_xlabel('W1 - W2')
ax1.legend(['Masers', 'Non-masers'])
plt.tight_layout()
plt.show()


#%% 5arcseconds

"""#Import the data, Home computer
pr, w1, w2, w3, w4, v_disp = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/GitHub/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_corrected.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/Github/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_NM.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
"""
#Import the data, Lab computer
pr, w1, w2, w3, w4, v_disp = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_5arcsec_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_5arcsec_NM_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)


#Exclude velocity dispersions zero & below
pr, w1, w2, w3, w4, v_disp = list(pr), list(w1), list(w2), list(w3), list(w4), list(v_disp)
for i in v_disp:
    if i <= 0:
        zero = v_disp.index(i)
        v_disp.remove(i)
        pr.pop(zero)
        w1.pop(zero)
        w2.pop(zero)
        w3.pop(zero)
        w4.pop(zero)

pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = list(pr_nm), list(w1_nm), list(w2_nm), list(w3_nm), list(w4_nm), list(v_disp_nm)
for i in v_disp_nm:
    if i <= 0:
        zero = v_disp_nm.index(i)
        v_disp_nm.remove(i)
        pr_nm.pop(zero)
        w1_nm.pop(zero)
        w2_nm.pop(zero)
        w3_nm.pop(zero)
        w4_nm.pop(zero)

#Iterate through the objects to creeate a list of masses
masses_m = []
masses_nm = []
for n in range(len(v_disp)): #Iterate over all velocities for masers
    masses_m.append(Mass(v_disp[n])) #Added each mass to the maser list
for n in range(len(v_disp_nm)): #Iterate over all velocities for non-masers
    masses_nm.append(Mass(v_disp_nm[n])) #Add each mass to the non-maser list

w12 = []
w12_nm = []
for i in range(len(v_disp)):
    w12.append(w1[i]-w2[i])
for i in range(len(v_disp_nm)):
    w12_nm.append(w1_nm[i] - w2_nm[i])

plt.figure(num = None)
fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize = (12, 6), sharey = True)

ax1.scatter(pr_nm, masses_nm, color = 'grey')
ax1.scatter(pr, masses_m, color = 'blue')
ax1.set_ylabel('Mass (in solar masses)')
ax1.set_xlabel('PR')
ax2.scatter(w1_nm, masses_nm, color = 'grey')
ax2.scatter(w1, masses_m, color = 'blue')
ax2.set_xlabel('W1')
ax3.scatter(w2_nm, masses_nm, color = 'grey')
ax3.scatter(w2, masses_m, color = 'blue')
ax3.set_xlabel('W2')
ax4.scatter(w12_nm, masses_nm, color = 'grey')
ax4.scatter(w12, masses_m, color = 'blue')
ax4.set_xlabel('W1 - W2')
ax1.legend(['Masers', 'Non-masers'])
plt.tight_layout()
plt.show()


#%% 6arcseconds

"""#Import the data, Home computer
pr, w1, w2, w3, w4, v_disp = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/GitHub/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_corrected.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/Github/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_NM.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
"""
#Import the data, Lab computer
pr, w1, w2, w3, w4, v_disp = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_6arcsec_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_6arcsec_NM_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)


#Exclude velocity dispersions zero & below
pr, w1, w2, w3, w4, v_disp = list(pr), list(w1), list(w2), list(w3), list(w4), list(v_disp)
for i in v_disp:
    if i <= 0:
        zero = v_disp.index(i)
        v_disp.remove(i)
        pr.pop(zero)
        w1.pop(zero)
        w2.pop(zero)
        w3.pop(zero)
        w4.pop(zero)

pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = list(pr_nm), list(w1_nm), list(w2_nm), list(w3_nm), list(w4_nm), list(v_disp_nm)
for i in v_disp_nm:
    if i <= 0:
        zero = v_disp_nm.index(i)
        v_disp_nm.remove(i)
        pr_nm.pop(zero)
        w1_nm.pop(zero)
        w2_nm.pop(zero)
        w3_nm.pop(zero)
        w4_nm.pop(zero)

#Iterate through the objects to creeate a list of masses
masses_m = []
masses_nm = []
for n in range(len(v_disp)): #Iterate over all velocities for masers
    masses_m.append(Mass(v_disp[n])) #Added each mass to the maser list
for n in range(len(v_disp_nm)): #Iterate over all velocities for non-masers
    masses_nm.append(Mass(v_disp_nm[n])) #Add each mass to the non-maser list

w12 = []
w12_nm = []
for i in range(len(v_disp)):
    w12.append(w1[i]-w2[i])
for i in range(len(v_disp_nm)):
    w12_nm.append(w1_nm[i] - w2_nm[i])

plt.figure(num = None)
fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize = (12, 6), sharey = True)

ax1.scatter(pr_nm, masses_nm, color = 'grey')
ax1.scatter(pr, masses_m, color = 'blue')
ax1.set_ylabel('Mass (in solar masses)')
ax1.set_xlabel('PR')
ax2.scatter(w1_nm, masses_nm, color = 'grey')
ax2.scatter(w1, masses_m, color = 'blue')
ax2.set_xlabel('W1')
ax3.scatter(w2_nm, masses_nm, color = 'grey')
ax3.scatter(w2, masses_m, color = 'blue')
ax3.set_xlabel('W2')
ax4.scatter(w12_nm, masses_nm, color = 'grey')
ax4.scatter(w12, masses_m, color = 'blue')
ax4.set_xlabel('W1 - W2')
ax1.legend(['Masers', 'Non-masers'])
plt.tight_layout()
plt.show()


#%% 7arcseconds

"""#Import the data, Home computer
pr, w1, w2, w3, w4, v_disp = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/GitHub/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_corrected.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/Github/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_NM.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
"""
#Import the data, Lab computer
pr, w1, w2, w3, w4, v_disp = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_7arcsec_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_7arcsec_NM_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)


#Exclude velocity dispersions zero & below
pr, w1, w2, w3, w4, v_disp = list(pr), list(w1), list(w2), list(w3), list(w4), list(v_disp)
for i in v_disp:
    if i <= 0:
        zero = v_disp.index(i)
        v_disp.remove(i)
        pr.pop(zero)
        w1.pop(zero)
        w2.pop(zero)
        w3.pop(zero)
        w4.pop(zero)

pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = list(pr_nm), list(w1_nm), list(w2_nm), list(w3_nm), list(w4_nm), list(v_disp_nm)
for i in v_disp_nm:
    if i <= 0:
        zero = v_disp_nm.index(i)
        v_disp_nm.remove(i)
        pr_nm.pop(zero)
        w1_nm.pop(zero)
        w2_nm.pop(zero)
        w3_nm.pop(zero)
        w4_nm.pop(zero)

#Iterate through the objects to creeate a list of masses
masses_m = []
masses_nm = []
for n in range(len(v_disp)): #Iterate over all velocities for masers
    masses_m.append(Mass(v_disp[n])) #Added each mass to the maser list
for n in range(len(v_disp_nm)): #Iterate over all velocities for non-masers
    masses_nm.append(Mass(v_disp_nm[n])) #Add each mass to the non-maser list

w12 = []
w12_nm = []
for i in range(len(v_disp)):
    w12.append(w1[i]-w2[i])
for i in range(len(v_disp_nm)):
    w12_nm.append(w1_nm[i] - w2_nm[i])

plt.figure(num = None)
fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize = (12, 6), sharey = True)

ax1.scatter(pr_nm, masses_nm, color = 'grey')
ax1.scatter(pr, masses_m, color = 'blue')
ax1.set_ylabel('Mass (in solar masses)')
ax1.set_xlabel('PR')
ax2.scatter(w1_nm, masses_nm, color = 'grey')
ax2.scatter(w1, masses_m, color = 'blue')
ax2.set_xlabel('W1')
ax3.scatter(w2_nm, masses_nm, color = 'grey')
ax3.scatter(w2, masses_m, color = 'blue')
ax3.set_xlabel('W2')
ax4.scatter(w12_nm, masses_nm, color = 'grey')
ax4.scatter(w12, masses_m, color = 'blue')
ax4.set_xlabel('W1 - W2')
ax1.legend(['Non-masers', 'Masers'])
plt.tight_layout()
plt.show()


#%% 8arcseconds

"""#Import the data, Home computer
pr, w1, w2, w3, w4, v_disp = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/GitHub/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_corrected.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/Github/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_NM.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
"""
#Import the data, Lab computer
pr, w1, w2, w3, w4, v_disp = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_8arcsec_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
masers = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_8arcsec_POLLEYEQ.csv', delimiter=',', unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_8arcsec_NM_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
non_masers = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_8arcsec_NM_POLLEYEQ.csv', delimiter=',', unpack=True)

#Sample sizes
ss_nm = len(v_disp_nm)
ss_m = len(v_disp)

#Exclude velocity dispersions zero & below
pr, w1, w2, w3, w4, v_disp = list(pr), list(w1), list(w2), list(w3), list(w4), list(v_disp)
for i in v_disp:
    if i <= 0:
        zero = v_disp.index(i)
        v_disp.remove(i)
        pr.pop(zero)
        w1.pop(zero)
        w2.pop(zero)
        w3.pop(zero)
        w4.pop(zero)

pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = list(pr_nm), list(w1_nm), list(w2_nm), list(w3_nm), list(w4_nm), list(v_disp_nm)
for i in v_disp_nm:
    if i <= 0:
        zero = v_disp_nm.index(i)
        v_disp_nm.remove(i)
        pr_nm.pop(zero)
        w1_nm.pop(zero)
        w2_nm.pop(zero)
        w3_nm.pop(zero)
        w4_nm.pop(zero)

#Iterate through the objects to creeate a list of masses
masses_m = []
masses_nm = []
for n in range(len(v_disp)): #Iterate over all velocities for masers
    masses_m.append(Mass(v_disp[n])) #Added each mass to the maser list
for n in range(len(v_disp_nm)): #Iterate over all velocities for non-masers
    masses_nm.append(Mass(v_disp_nm[n])) #Add each mass to the non-maser list

w12 = []
w12_nm = []
for i in range(len(v_disp)):
    w12.append(w1[i]-w2[i])
for i in range(len(v_disp_nm)):
    w12_nm.append(w1_nm[i] - w2_nm[i])

plt.figure(num = None)
fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize = (12, 6), sharey = True)

ax1.scatter(pr_nm, masses_nm, color = 'grey')
ax1.scatter(pr, masses_m, color = 'blue')
ax1.set_ylabel('Mass (in solar masses)')
ax1.set_xlabel('PR')
ax2.scatter(w1_nm, masses_nm, color = 'grey')
ax2.scatter(w1, masses_m, color = 'blue')
ax2.set_xlabel('W1')
ax3.scatter(w2_nm, masses_nm, color = 'grey')
ax3.scatter(w2, masses_m, color = 'blue')
ax3.set_xlabel('W2')
ax4.scatter(w12_nm, masses_nm, color = 'grey')
ax4.scatter(w12, masses_m, color = 'blue')
ax4.set_xlabel('W1 - W2')
ax1.legend(['Masers', 'Non-masers'])
plt.tight_layout()
plt.show()



#%% Histogram of velocity dispersion (sigma *)

v_disp = np.array(v_disp)
v_disp_nm = np.array(v_disp_nm)

plt.figure()
fig, ax = plt.subplots(figsize = (10, 10))

ax.hist(v_disp,
        bins = np.linspace(v_disp.min(), v_disp.max(), num = 35, endpoint = False),
        color = "green",
        edgecolor = 'white',
        density = True,
        alpha = 0.6,
        linewidth = 1,
        label = 'masers'
           ) 
ax.hist(v_disp_nm,
        bins = np.linspace(v_disp_nm.min(), v_disp_nm.max(), num = 35, endpoint = False),
        color = "blue",
        edgecolor = 'white',
        density = True,
        alpha = 0.6,
        linewidth = 1,
        label = 'non-masers'
           )

plt.legend(['Masers', 'Non-masers'])

plt.show()


#%% Values for slide show

print('Sample size for non-masers is', ss_nm,
      '\nSample size for masers is', ss_m,
      '\nSamples with veloctiy dispersions for non-masers is', len(v_disp_nm),
      '\nSamples with velocity dispersions for masers is', len(v_disp))

#Expectation value of velocity dispersion
print('The expected value of velocity dispersion for non-masers is', exp_value(v_disp_nm),
      '\nThe expected value of velocity dispersion for masers is', exp_value(v_disp))

#Expectation value of mass of black hole
print('The expected value of the mass of black hole for non-masers is', exp_value(masses_nm),
      '\nThe expected value of the mass of black hole for masers is', exp_value(masses_m))

#Expectation value of mass of black hole, with pr > .75

pr_masses_m = []
pr_masses_nm = []
for i in pr:
    if i > .75:
        index = pr.index(i)
        pr_masses_m.append(masses_m[index])
for i in pr_nm:
    if i > .75:
        index = pr_nm.index(i)
        pr_masses_nm.append(masses_nm[index])
        
print('The expected value of the mass of black hole, with PR > .75, for non-masers is', exp_value(pr_masses_m),
      '\nThe expected value of the mass of black hole, with PR > .75, for masers is', exp_value(pr_masses_nm))


