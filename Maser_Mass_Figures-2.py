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
pr, w1, w2, w3, w4, v_disp, lum, ob_class = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_3arcsec_POLLEYEQ_0.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7,-3,-2,-1), unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_3arcsec_NM_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)


#Exclude velocity dispersions zero & below
pr, w1, w2, w3, w4, v_disp, lum, ob_class = list(pr), list(w1), list(w2), list(w3), list(w4), list(v_disp), list(lum), list(ob_class)
for i in v_disp:
    if i <= 0:
        zero = v_disp.index(i)
        v_disp.remove(i)
        pr.pop(zero)
        w1.pop(zero)
        w2.pop(zero)
        w3.pop(zero)
        w4.pop(zero)
        lum.pop(zero)
        ob_class.pop(zero)

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
        
#Megamasers
mega_masers = []
v_disp_mega_masers = []
pr_mega_masers = []
w1_mega_masers = []
w2_mega_masers = []
w3_mega_masers = []
w4_mega_masers = []
for i in lum:
    if i >= 10:
        index = lum.index(i)
        mega_masers.append(Mass(v_disp[index]))
        pr_mega_masers.append(pr[index])
        v_disp_mega_masers.append(v_disp[index])
        w1_mega_masers.append(w1[index])
        w2_mega_masers.append(w2[index])
        w3_mega_masers.append(w3[index])
        w4_mega_masers.append(w4[index])
        
        
#Disk Masers
disk_masers = []
pr_disk_masers = []
v_disp_disk_masers = []
w1_disk_masers = []
w2_disk_masers = []
w3_disk_masers = []
w4_disk_masers = []
for i in ob_class:
    if i == 1:
        index = ob_class.index(i)
        disk_masers.append(Mass(v_disp[index]))
        pr_disk_masers.append(pr[index])
        v_disp_disk_masers.append(v_disp[index])
        w1_disk_masers.append(w1[index])
        w2_disk_masers.append(w2[index])
        w3_disk_masers.append(w3[index])
        w4_disk_masers.append(w4[index])
        

#Iterate through the objects to creeate a list of masses
masses_m = []
masses_nm = []
for n in range(len(v_disp)): #Iterate over all velocities for masers
    masses_m.append(Mass(v_disp[n])) #Added each mass to the maser list
for n in range(len(v_disp_nm)): #Iterate over all velocities for non-masers
    masses_nm.append(Mass(v_disp_nm[n])) #Add each mass to the non-maser list

#Create a new list for the magnitudes minus one another (w1-w2)
w12 = []
w12_nm = []
w12_mega_masers = []
w12_disk_masers = []
for i in range(len(v_disp)):
    w12.append(w1[i]-w2[i])
for i in range(len(v_disp_nm)):
    w12_nm.append(w1_nm[i] - w2_nm[i])
for i in range(len(w1_mega_masers)):
    w12_mega_masers.append(w1_mega_masers[i] - w2_mega_masers[i])
for i in range(len(w1_disk_masers)):
    w12_disk_masers.append(w1_disk_masers[i] - w2_disk_masers[i])

#Plot the scatter plot with non-masers, masers, mega and disk masers
plt.figure(num = None)
fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize = (12, 6), sharey = True)

ax1.scatter(pr_nm, masses_nm, color = 'grey') #Against pr
ax1.scatter(pr, masses_m, color = 'blue')
ax1.scatter(pr_mega_masers, mega_masers, color = 'green')
ax1.scatter(pr_disk_masers, disk_masers, color = 'purple')
ax1.set_ylabel('Mass (in solar masses)')
ax1.set_xlabel('PR')
ax2.scatter(w1_nm, masses_nm, color = 'grey') #Against maginitudes
ax2.scatter(w1, masses_m, color = 'blue')
ax2.scatter(w1_mega_masers, mega_masers, color = 'green')
ax2.scatter(w1_disk_masers, disk_masers, color = 'purple')
ax2.set_xlabel('W1')
ax3.scatter(w2_nm, masses_nm, color = 'grey')
ax3.scatter(w2, masses_m, color = 'blue')
ax3.scatter(w2_mega_masers, mega_masers, color = 'green')
ax3.scatter(w2_disk_masers, disk_masers, color = 'purple')
ax3.set_xlabel('W2')
ax4.scatter(w12_nm, masses_nm, color = 'grey')
ax4.scatter(w12, masses_m, color = 'blue')
ax4.scatter(w12_mega_masers, mega_masers, color = 'green')
ax4.scatter(w12_disk_masers, disk_masers, color = 'purple')
ax4.set_xlabel('W1 - W2') #Against compared magnitudes
ax1.legend(['Masers', 'Non-masers', 'Mega masers', 'Disk masers'])
plt.tight_layout()
plt.show()


#%% 4arcseconds

"""#Import the data, Home computer
pr, w1, w2, w3, w4, v_disp = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/GitHub/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_corrected.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/Github/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_NM.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
"""
#Import the data, Lab computer
pr, w1, w2, w3, w4, v_disp, lum, ob_class = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_4arcsec_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7,-3,-2,-1), unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_4arcsec_NM_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)


#Exclude velocity dispersions zero & below
pr, w1, w2, w3, w4, v_disp, lum, ob_class = list(pr), list(w1), list(w2), list(w3), list(w4), list(v_disp), list(lum), list(ob_class)
for i in v_disp:
    if i <= 0:
        zero = v_disp.index(i)
        v_disp.remove(i)
        pr.pop(zero)
        w1.pop(zero)
        w2.pop(zero)
        w3.pop(zero)
        w4.pop(zero)
        lum.pop(zero)
        ob_class.pop(zero)

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
        
#Megamasers
mega_masers = []
v_disp_mega_masers = []
pr_mega_masers = []
w1_mega_masers = []
w2_mega_masers = []
w3_mega_masers = []
w4_mega_masers = []
for i in lum:
    if i >= 10:
        index = lum.index(i)
        mega_masers.append(Mass(v_disp[index]))
        pr_mega_masers.append(pr[index])
        v_disp_mega_masers.append(v_disp[index])
        w1_mega_masers.append(w1[index])
        w2_mega_masers.append(w2[index])
        w3_mega_masers.append(w3[index])
        w4_mega_masers.append(w4[index])
        
        
#Disk Masers
disk_masers = []
pr_disk_masers = []
v_disp_disk_masers = []
w1_disk_masers = []
w2_disk_masers = []
w3_disk_masers = []
w4_disk_masers = []
for i in ob_class:
    if i == 1:
        index = ob_class.index(i)
        disk_masers.append(Mass(v_disp[index]))
        pr_disk_masers.append(pr[index])
        v_disp_disk_masers.append(v_disp[index])
        w1_disk_masers.append(w1[index])
        w2_disk_masers.append(w2[index])
        w3_disk_masers.append(w3[index])
        w4_disk_masers.append(w4[index])
        

#Iterate through the objects to creeate a list of masses
masses_m = []
masses_nm = []
for n in range(len(v_disp)): #Iterate over all velocities for masers
    masses_m.append(Mass(v_disp[n])) #Added each mass to the maser list
for n in range(len(v_disp_nm)): #Iterate over all velocities for non-masers
    masses_nm.append(Mass(v_disp_nm[n])) #Add each mass to the non-maser list

#Create a new list for the magnitudes minus one another (w1-w2)
w12 = []
w12_nm = []
w12_mega_masers = []
w12_disk_masers = []
for i in range(len(v_disp)):
    w12.append(w1[i]-w2[i])
for i in range(len(v_disp_nm)):
    w12_nm.append(w1_nm[i] - w2_nm[i])
for i in range(len(w1_mega_masers)):
    w12_mega_masers.append(w1_mega_masers[i] - w2_mega_masers[i])
for i in range(len(w1_disk_masers)):
    w12_disk_masers.append(w1_disk_masers[i] - w2_disk_masers[i])

#Plot the scatter plot with non-masers, masers, mega and disk masers
plt.figure(num = None)
fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize = (12, 6), sharey = True)

ax1.scatter(pr_nm, masses_nm, color = 'grey') #Against pr
ax1.scatter(pr, masses_m, color = 'blue')
ax1.scatter(pr_mega_masers, mega_masers, color = 'green')
ax1.scatter(pr_disk_masers, disk_masers, color = 'purple')
ax1.set_ylabel('Mass (in solar masses)')
ax1.set_xlabel('PR')
ax2.scatter(w1_nm, masses_nm, color = 'grey') #Against maginitudes
ax2.scatter(w1, masses_m, color = 'blue')
ax2.scatter(w1_mega_masers, mega_masers, color = 'green')
ax2.scatter(w1_disk_masers, disk_masers, color = 'purple')
ax2.set_xlabel('W1')
ax3.scatter(w2_nm, masses_nm, color = 'grey')
ax3.scatter(w2, masses_m, color = 'blue')
ax3.scatter(w2_mega_masers, mega_masers, color = 'green')
ax3.scatter(w2_disk_masers, disk_masers, color = 'purple')
ax3.set_xlabel('W2')
ax4.scatter(w12_nm, masses_nm, color = 'grey')
ax4.scatter(w12, masses_m, color = 'blue')
ax4.scatter(w12_mega_masers, mega_masers, color = 'green')
ax4.scatter(w12_disk_masers, disk_masers, color = 'purple')
ax4.set_xlabel('W1 - W2') #Against compared magnitudes
ax1.legend(['Masers', 'Non-masers', 'Mega masers', 'Disk masers'])
plt.tight_layout()
plt.show()


#%% 5arcseconds

"""#Import the data, Home computer
pr, w1, w2, w3, w4, v_disp = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/GitHub/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_corrected.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/Github/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_NM.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
"""
#Import the data, Lab computer
pr, w1, w2, w3, w4, v_disp, lum, ob_class = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_5arcsec_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7,-3,-2,-1), unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_5arcsec_NM_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)


#Exclude velocity dispersions zero & below
pr, w1, w2, w3, w4, v_disp, lum, ob_class = list(pr), list(w1), list(w2), list(w3), list(w4), list(v_disp), list(lum), list(ob_class)
for i in v_disp:
    if i <= 0:
        zero = v_disp.index(i)
        v_disp.remove(i)
        pr.pop(zero)
        w1.pop(zero)
        w2.pop(zero)
        w3.pop(zero)
        w4.pop(zero)
        lum.pop(zero)
        ob_class.pop(zero)

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
        
#Megamasers
mega_masers = []
v_disp_mega_masers = []
pr_mega_masers = []
w1_mega_masers = []
w2_mega_masers = []
w3_mega_masers = []
w4_mega_masers = []
for i in lum:
    if i >= 10:
        index = lum.index(i)
        mega_masers.append(Mass(v_disp[index]))
        pr_mega_masers.append(pr[index])
        v_disp_mega_masers.append(v_disp[index])
        w1_mega_masers.append(w1[index])
        w2_mega_masers.append(w2[index])
        w3_mega_masers.append(w3[index])
        w4_mega_masers.append(w4[index])
        
        
#Disk Masers
disk_masers = []
pr_disk_masers = []
v_disp_disk_masers = []
w1_disk_masers = []
w2_disk_masers = []
w3_disk_masers = []
w4_disk_masers = []
for i in ob_class:
    if i == 1:
        index = ob_class.index(i)
        disk_masers.append(Mass(v_disp[index]))
        pr_disk_masers.append(pr[index])
        v_disp_disk_masers.append(v_disp[index])
        w1_disk_masers.append(w1[index])
        w2_disk_masers.append(w2[index])
        w3_disk_masers.append(w3[index])
        w4_disk_masers.append(w4[index])
        

#Iterate through the objects to creeate a list of masses
masses_m = []
masses_nm = []
for n in range(len(v_disp)): #Iterate over all velocities for masers
    masses_m.append(Mass(v_disp[n])) #Added each mass to the maser list
for n in range(len(v_disp_nm)): #Iterate over all velocities for non-masers
    masses_nm.append(Mass(v_disp_nm[n])) #Add each mass to the non-maser list

#Create a new list for the magnitudes minus one another (w1-w2)
w12 = []
w12_nm = []
w12_mega_masers = []
w12_disk_masers = []
for i in range(len(v_disp)):
    w12.append(w1[i]-w2[i])
for i in range(len(v_disp_nm)):
    w12_nm.append(w1_nm[i] - w2_nm[i])
for i in range(len(w1_mega_masers)):
    w12_mega_masers.append(w1_mega_masers[i] - w2_mega_masers[i])
for i in range(len(w1_disk_masers)):
    w12_disk_masers.append(w1_disk_masers[i] - w2_disk_masers[i])

#Plot the scatter plot with non-masers, masers, mega and disk masers
plt.figure(num = None)
fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize = (12, 6), sharey = True)

ax1.scatter(pr_nm, masses_nm, color = 'grey') #Against pr
ax1.scatter(pr, masses_m, color = 'blue')
ax1.scatter(pr_mega_masers, mega_masers, color = 'green')
ax1.scatter(pr_disk_masers, disk_masers, color = 'purple')
ax1.set_ylabel('Mass (in solar masses)')
ax1.set_xlabel('PR')
ax2.scatter(w1_nm, masses_nm, color = 'grey') #Against maginitudes
ax2.scatter(w1, masses_m, color = 'blue')
ax2.scatter(w1_mega_masers, mega_masers, color = 'green')
ax2.scatter(w1_disk_masers, disk_masers, color = 'purple')
ax2.set_xlabel('W1')
ax3.scatter(w2_nm, masses_nm, color = 'grey')
ax3.scatter(w2, masses_m, color = 'blue')
ax3.scatter(w2_mega_masers, mega_masers, color = 'green')
ax3.scatter(w2_disk_masers, disk_masers, color = 'purple')
ax3.set_xlabel('W2')
ax4.scatter(w12_nm, masses_nm, color = 'grey')
ax4.scatter(w12, masses_m, color = 'blue')
ax4.scatter(w12_mega_masers, mega_masers, color = 'green')
ax4.scatter(w12_disk_masers, disk_masers, color = 'purple')
ax4.set_xlabel('W1 - W2') #Against compared magnitudes
ax1.legend(['Masers', 'Non-masers', 'Mega masers', 'Disk masers'])
plt.tight_layout()
plt.show()


#%% 6arcseconds

"""#Import the data, Home computer
pr, w1, w2, w3, w4, v_disp = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/GitHub/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_corrected.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/Github/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_NM.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
"""
#Import the data, Lab computer
pr, w1, w2, w3, w4, v_disp, lum, ob_class = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_6arcsec_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7,-3,-2,-1), unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_6arcsec_NM_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)


#Exclude velocity dispersions zero & below
pr, w1, w2, w3, w4, v_disp, lum, ob_class = list(pr), list(w1), list(w2), list(w3), list(w4), list(v_disp), list(lum), list(ob_class)
for i in v_disp:
    if i <= 0:
        zero = v_disp.index(i)
        v_disp.remove(i)
        pr.pop(zero)
        w1.pop(zero)
        w2.pop(zero)
        w3.pop(zero)
        w4.pop(zero)
        lum.pop(zero)
        ob_class.pop(zero)

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
        
#Megamasers
mega_masers = []
v_disp_mega_masers = []
pr_mega_masers = []
w1_mega_masers = []
w2_mega_masers = []
w3_mega_masers = []
w4_mega_masers = []
for i in lum:
    if i >= 10:
        index = lum.index(i)
        mega_masers.append(Mass(v_disp[index]))
        pr_mega_masers.append(pr[index])
        v_disp_mega_masers.append(v_disp[index])
        w1_mega_masers.append(w1[index])
        w2_mega_masers.append(w2[index])
        w3_mega_masers.append(w3[index])
        w4_mega_masers.append(w4[index])
        
        
#Disk Masers
disk_masers = []
pr_disk_masers = []
v_disp_disk_masers = []
w1_disk_masers = []
w2_disk_masers = []
w3_disk_masers = []
w4_disk_masers = []
for i in ob_class:
    if i == 1:
        index = ob_class.index(i)
        disk_masers.append(Mass(v_disp[index]))
        pr_disk_masers.append(pr[index])
        v_disp_disk_masers.append(v_disp[index])
        w1_disk_masers.append(w1[index])
        w2_disk_masers.append(w2[index])
        w3_disk_masers.append(w3[index])
        w4_disk_masers.append(w4[index])
        

#Iterate through the objects to creeate a list of masses
masses_m = []
masses_nm = []
for n in range(len(v_disp)): #Iterate over all velocities for masers
    masses_m.append(Mass(v_disp[n])) #Added each mass to the maser list
for n in range(len(v_disp_nm)): #Iterate over all velocities for non-masers
    masses_nm.append(Mass(v_disp_nm[n])) #Add each mass to the non-maser list

#Create a new list for the magnitudes minus one another (w1-w2)
w12 = []
w12_nm = []
w12_mega_masers = []
w12_disk_masers = []
for i in range(len(v_disp)):
    w12.append(w1[i]-w2[i])
for i in range(len(v_disp_nm)):
    w12_nm.append(w1_nm[i] - w2_nm[i])
for i in range(len(w1_mega_masers)):
    w12_mega_masers.append(w1_mega_masers[i] - w2_mega_masers[i])
for i in range(len(w1_disk_masers)):
    w12_disk_masers.append(w1_disk_masers[i] - w2_disk_masers[i])

#Plot the scatter plot with non-masers, masers, mega and disk masers
plt.figure(num = None)
fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize = (12, 6), sharey = True)

ax1.scatter(pr_nm, masses_nm, color = 'grey') #Against pr
ax1.scatter(pr, masses_m, color = 'blue')
ax1.scatter(pr_mega_masers, mega_masers, color = 'green')
ax1.scatter(pr_disk_masers, disk_masers, color = 'purple')
ax1.set_ylabel('Mass (in solar masses)')
ax1.set_xlabel('PR')
ax2.scatter(w1_nm, masses_nm, color = 'grey') #Against maginitudes
ax2.scatter(w1, masses_m, color = 'blue')
ax2.scatter(w1_mega_masers, mega_masers, color = 'green')
ax2.scatter(w1_disk_masers, disk_masers, color = 'purple')
ax2.set_xlabel('W1')
ax3.scatter(w2_nm, masses_nm, color = 'grey')
ax3.scatter(w2, masses_m, color = 'blue')
ax3.scatter(w2_mega_masers, mega_masers, color = 'green')
ax3.scatter(w2_disk_masers, disk_masers, color = 'purple')
ax3.set_xlabel('W2')
ax4.scatter(w12_nm, masses_nm, color = 'grey')
ax4.scatter(w12, masses_m, color = 'blue')
ax4.scatter(w12_mega_masers, mega_masers, color = 'green')
ax4.scatter(w12_disk_masers, disk_masers, color = 'purple')
ax4.set_xlabel('W1 - W2') #Against compared magnitudes
ax1.legend(['Masers', 'Non-masers', 'Mega masers', 'Disk masers'])
plt.tight_layout()
plt.show()


#%% 7arcseconds

"""#Import the data, Home computer
pr, w1, w2, w3, w4, v_disp = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/GitHub/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_corrected.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/Github/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_NM.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
"""
#Import the data, Lab computer
pr, w1, w2, w3, w4, v_disp, lum, ob_class = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_7arcsec_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7,-3,-2,-1), unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_7arcsec_NM_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)


#Exclude velocity dispersions zero & below
pr, w1, w2, w3, w4, v_disp, lum, ob_class = list(pr), list(w1), list(w2), list(w3), list(w4), list(v_disp), list(lum), list(ob_class)
for i in v_disp:
    if i <= 0:
        zero = v_disp.index(i)
        v_disp.remove(i)
        pr.pop(zero)
        w1.pop(zero)
        w2.pop(zero)
        w3.pop(zero)
        w4.pop(zero)
        lum.pop(zero)
        ob_class.pop(zero)

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
        
#Megamasers
mega_masers = []
v_disp_mega_masers = []
pr_mega_masers = []
w1_mega_masers = []
w2_mega_masers = []
w3_mega_masers = []
w4_mega_masers = []
for i in lum:
    if i >= 10:
        index = lum.index(i)
        mega_masers.append(Mass(v_disp[index]))
        pr_mega_masers.append(pr[index])
        v_disp_mega_masers.append(v_disp[index])
        w1_mega_masers.append(w1[index])
        w2_mega_masers.append(w2[index])
        w3_mega_masers.append(w3[index])
        w4_mega_masers.append(w4[index])
        
        
#Disk Masers
disk_masers = []
pr_disk_masers = []
v_disp_disk_masers = []
w1_disk_masers = []
w2_disk_masers = []
w3_disk_masers = []
w4_disk_masers = []
for i in ob_class:
    if i == 1:
        index = ob_class.index(i)
        disk_masers.append(Mass(v_disp[index]))
        pr_disk_masers.append(pr[index])
        v_disp_disk_masers.append(v_disp[index])
        w1_disk_masers.append(w1[index])
        w2_disk_masers.append(w2[index])
        w3_disk_masers.append(w3[index])
        w4_disk_masers.append(w4[index])
        

#Iterate through the objects to creeate a list of masses
masses_m = []
masses_nm = []
for n in range(len(v_disp)): #Iterate over all velocities for masers
    masses_m.append(Mass(v_disp[n])) #Added each mass to the maser list
for n in range(len(v_disp_nm)): #Iterate over all velocities for non-masers
    masses_nm.append(Mass(v_disp_nm[n])) #Add each mass to the non-maser list

#Create a new list for the magnitudes minus one another (w1-w2)
w12 = []
w12_nm = []
w12_mega_masers = []
w12_disk_masers = []
for i in range(len(v_disp)):
    w12.append(w1[i]-w2[i])
for i in range(len(v_disp_nm)):
    w12_nm.append(w1_nm[i] - w2_nm[i])
for i in range(len(w1_mega_masers)):
    w12_mega_masers.append(w1_mega_masers[i] - w2_mega_masers[i])
for i in range(len(w1_disk_masers)):
    w12_disk_masers.append(w1_disk_masers[i] - w2_disk_masers[i])

#Plot the scatter plot with non-masers, masers, mega and disk masers
plt.figure(num = None)
fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize = (12, 6), sharey = True)

ax1.scatter(pr_nm, masses_nm, color = 'grey') #Against pr
ax1.scatter(pr, masses_m, color = 'blue')
ax1.scatter(pr_mega_masers, mega_masers, color = 'green')
ax1.scatter(pr_disk_masers, disk_masers, color = 'purple')
ax1.set_ylabel('Mass (in solar masses)')
ax1.set_xlabel('PR')
ax2.scatter(w1_nm, masses_nm, color = 'grey') #Against maginitudes
ax2.scatter(w1, masses_m, color = 'blue')
ax2.scatter(w1_mega_masers, mega_masers, color = 'green')
ax2.scatter(w1_disk_masers, disk_masers, color = 'purple')
ax2.set_xlabel('W1')
ax3.scatter(w2_nm, masses_nm, color = 'grey')
ax3.scatter(w2, masses_m, color = 'blue')
ax3.scatter(w2_mega_masers, mega_masers, color = 'green')
ax3.scatter(w2_disk_masers, disk_masers, color = 'purple')
ax3.set_xlabel('W2')
ax4.scatter(w12_nm, masses_nm, color = 'grey')
ax4.scatter(w12, masses_m, color = 'blue')
ax4.scatter(w12_mega_masers, mega_masers, color = 'green')
ax4.scatter(w12_disk_masers, disk_masers, color = 'purple')
ax4.set_xlabel('W1 - W2') #Against compared magnitudes
ax1.legend(['Masers', 'Non-masers', 'Mega masers', 'Disk masers'])
plt.tight_layout()
plt.show()


#%% 8arcseconds

"""#Import the data, Home computer
pr, w1, w2, w3, w4, v_disp = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/GitHub/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_corrected.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('C:/Users/eqpol/OneDrive/Documents/Class Work/Github/Astro_Lab_Work/MyTable_CrossDiffCoords_3arcsec_NM.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
"""
#Import the data, Lab computer
pr, w1, w2, w3, w4, v_disp, lum, ob_class = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_8arcsec_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7,-3,-2,-1), unpack=True)
masers = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_8arcsec_POLLEYEQ.csv', delimiter=',', unpack=True)
pr_nm, w1_nm, w2_nm, w3_nm, w4_nm, v_disp_nm = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_8arcsec_NM_POLLEYEQ.csv', delimiter=',', skip_header=1, usecols=(1,4,5,6,7, -1), unpack=True)
non_masers = np.genfromtxt('/Users/ethanpolley/Downloads/MyTable_CrossDiffCoords_8arcsec_NM_POLLEYEQ.csv', delimiter=',', unpack=True)

#Sample sizes
ss_nm = len(v_disp_nm)
ss_m = len(v_disp)

#Exclude velocity dispersions zero & below
pr, w1, w2, w3, w4, v_disp, lum, ob_class = list(pr), list(w1), list(w2), list(w3), list(w4), list(v_disp), list(lum), list(ob_class)
for i in v_disp:
    if i <= 0:
        zero = v_disp.index(i)
        v_disp.remove(i)
        pr.pop(zero)
        w1.pop(zero)
        w2.pop(zero)
        w3.pop(zero)
        w4.pop(zero)
        lum.pop(zero)
        ob_class.pop(zero)

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
        
#Megamasers
mega_masers = []
v_disp_mega_masers = []
pr_mega_masers = []
w1_mega_masers = []
w2_mega_masers = []
w3_mega_masers = []
w4_mega_masers = []
for i in lum:
    if i >= 10:
        index = lum.index(i)
        mega_masers.append(Mass(v_disp[index]))
        pr_mega_masers.append(pr[index])
        v_disp_mega_masers.append(v_disp[index])
        w1_mega_masers.append(w1[index])
        w2_mega_masers.append(w2[index])
        w3_mega_masers.append(w3[index])
        w4_mega_masers.append(w4[index])
        
        
#Disk Masers
disk_masers = []
pr_disk_masers = []
v_disp_disk_masers = []
w1_disk_masers = []
w2_disk_masers = []
w3_disk_masers = []
w4_disk_masers = []
for i in ob_class:
    if i == 1:
        index = ob_class.index(i)
        disk_masers.append(Mass(v_disp[index]))
        pr_disk_masers.append(pr[index])
        v_disp_disk_masers.append(v_disp[index])
        w1_disk_masers.append(w1[index])
        w2_disk_masers.append(w2[index])
        w3_disk_masers.append(w3[index])
        w4_disk_masers.append(w4[index])
        

#Iterate through the objects to creeate a list of masses
masses_m = []
masses_nm = []
masses_mega_masers = []
masses_disk_masers = []
for n in range(len(v_disp)): #Iterate over all velocities for masers
    masses_m.append(Mass(v_disp[n])) #Added each mass to the maser list
for n in range(len(v_disp_nm)): #Iterate over all velocities for non-masers
    masses_nm.append(Mass(v_disp_nm[n])) #Add each mass to the non-maser list
for n in range(len(v_disp_mega_masers)):
    masses_mega_masers.append(Mass(v_disp_mega_masers[n]))
for n in range(len(v_disp_disk_masers)):
    masses_disk_masers.append(Mass(v_disp_disk_masers[n]))

for i in masses_nm:
    if i < 0:
        index = masses_nm.index(i)
        masses_nm.remove(i)
        pr_nm.pop(index)
        w1_nm.pop(index)
        w2_nm.pop(index)
        w3_nm.pop(index)
        w4_nm.pop(index)
        v_disp_nm.pop(index)

#Create a new list for the magnitudes minus one another (w1-w2)
w12 = []
w12_nm = []
w12_mega_masers = []
w12_disk_masers = []
for i in range(len(v_disp)):
    w12.append(w1[i]-w2[i])
for i in range(len(v_disp_nm)):
    w12_nm.append(w1_nm[i] - w2_nm[i])
for i in range(len(w1_mega_masers)):
    w12_mega_masers.append(w1_mega_masers[i] - w2_mega_masers[i])
for i in range(len(w1_disk_masers)):
    w12_disk_masers.append(w1_disk_masers[i] - w2_disk_masers[i])

#Plot the scatter plot with non-masers, masers, mega and disk masers
plt.figure(num = None)
fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize = (12, 6), sharey = True)

ax1.scatter(pr_nm, masses_nm, color = 'grey') #Against pr
ax1.scatter(pr, masses_m, color = 'blue')
ax1.scatter(pr_mega_masers, mega_masers, color = 'green')
ax1.scatter(pr_disk_masers, disk_masers, color = 'purple')
ax1.set_ylabel('Mass (in solar masses)')
ax1.set_xlabel('PR')
ax2.scatter(w1_nm, masses_nm, color = 'grey') #Against maginitudes
ax2.scatter(w1, masses_m, color = 'blue')
ax2.scatter(w1_mega_masers, mega_masers, color = 'green')
ax2.scatter(w1_disk_masers, disk_masers, color = 'purple')
ax2.set_xlabel('W1')
ax3.scatter(w2_nm, masses_nm, color = 'grey')
ax3.scatter(w2, masses_m, color = 'blue')
ax3.scatter(w2_mega_masers, mega_masers, color = 'green')
ax3.scatter(w2_disk_masers, disk_masers, color = 'purple')
ax3.set_xlabel('W2')
ax4.scatter(w12_nm, masses_nm, color = 'grey')
ax4.scatter(w12, masses_m, color = 'blue')
ax4.scatter(w12_mega_masers, mega_masers, color = 'green')
ax4.scatter(w12_disk_masers, disk_masers, color = 'purple')
ax4.set_xlabel('W1 - W2') #Against compared magnitudes
ax1.legend(['Masers', 'Non-masers', 'Mega masers', 'Disk masers'])
plt.tight_layout()
plt.show()



#%% Histogram of velocity dispersion (sigma *)

#Creating new list that contain values of pr > .75
v_disp_pr = []
v_disp_pr_nm = []
v_disp_pr_mega_masers = []
v_disp_pr_disk_masers = []
for i in pr:
    if i > .75:
        index = pr.index(i)
        x = v_disp[index]
        v_disp_pr.append(x)
        for n in lum:
            if n >= 10:
                index = lum.index(n)
                v_disp_pr_mega_masers.append(v_disp[index])
        for m in ob_class:
            if m == 1:
                index = ob_class.index(m)
                v_disp_pr_disk_masers.append(v_disp[index])      
for i in pr_nm:
    if i > .75:
        index = pr_nm.index(i)
        x = v_disp_nm[index]
        v_disp_pr_nm.append(x)

masses_m_pr = []
masses_nm_pr = []
masses_mega_masers_pr = []
masses_disk_masers_pr = []
for i in pr:
    if i > .75:
        index = pr.index(i)
        masses_m_pr.append(masses_m[index])
for i in pr_nm:
    if i > .75:
        index = pr_nm.index(i)
        masses_nm_pr.append(masses_nm[index])
for i in pr_mega_masers:
    if i > .75:
        index = pr_mega_masers.index(i)
        masses_mega_masers_pr.append(masses_mega_masers[index])
for i in pr_disk_masers:
    if i > .75:
        index = pr_disk_masers.index(i)
        masses_disk_masers_pr.append(masses_disk_masers[index])


#Convert lists into arrays for graphing in histogram
v_disp = np.array(v_disp)
v_disp_nm = np.array(v_disp_nm)
v_disp_mega_masers = np.array(v_disp_mega_masers)
v_disp_disk_masers = np.array(v_disp_disk_masers)
v_disp_pr = np.array(v_disp_pr)
v_disp_pr_nm = np.array(v_disp_pr_nm)
v_disp_pr_mega_masers = np.array(v_disp_pr_mega_masers)
v_disp_pr_disk_masers = np.array(v_disp_pr_disk_masers)
masses_m = np.array(masses_m)
masses_nm = np.array(masses_nm)
masses_mega_masers = np.array(masses_mega_masers)
masses_disk_masers = np.array(masses_disk_masers)
masses_m_pr = np.array(masses_m_pr)
masses_nm_pr = np.array(masses_nm_pr)
masses_mega_masers_pr = np.array(masses_mega_masers_pr)
masses_disk_masers_pr = np.array(masses_disk_masers_pr)

#Histogram graph
plt.figure()
fig, ax = plt.subplots(figsize = (10, 10))

ax.hist(v_disp_nm,
        bins = np.linspace(v_disp_nm.min(), v_disp_nm.max(), num = 35, endpoint = False),
        color = "gray",
        edgecolor = 'white',
        density = True,
        alpha = 0.6,
        linewidth = 1,
        label = 'non-masers'
           )
ax.hist(v_disp,
        bins = np.linspace(v_disp.min(), v_disp.max(), num = 35, endpoint = False),
        color = "blue",
        edgecolor = 'white',
        density = True,
        alpha = 0.6,
        linewidth = 1,
        label = 'masers'
           ) 
ax.hist(v_disp_mega_masers,
        bins = np.linspace(v_disp_mega_masers.min(), v_disp_mega_masers.max(), num = 35, endpoint = False),
        color = "green",
        edgecolor = 'white',
        density = True,
        alpha = 0.6,
        linewidth = 1,
        label = 'mega masers'
           ) 
ax.hist(v_disp_disk_masers,
        bins = np.linspace(v_disp_disk_masers.min(), v_disp_disk_masers.max(), num = 35, endpoint = False),
        color = "purple",
        edgecolor = 'white',
        density = True,
        alpha = 0.6,
        linewidth = 1,
        label = 'disk masers'
           ) 

plt.legend(['Non-masers', 'Masers', 'Mega-masers', 'Disk masers'])

plt.show()

plt.figure()
fig, ax = plt.subplots(figsize = (10, 10))

ax.hist(v_disp_pr_nm,
        bins = np.linspace(v_disp_pr_nm.min(), v_disp_pr_nm.max(), num = 35, endpoint = False),
        color = "gray",
        edgecolor = 'white',
        density = True,
        alpha = 0.6,
        linewidth = 1,
        label = 'non-masers'
           ) 
ax.hist(v_disp_pr,
        bins = np.linspace(v_disp_pr.min(), v_disp_pr.max(), num = 35, endpoint = False),
        color = "blue",
        edgecolor = 'white',
        density = True,
        alpha = 0.6,
        linewidth = 1,
        label = 'masers'
           )
ax.hist(v_disp_pr_mega_masers,
        bins = np.linspace(v_disp_pr_mega_masers.min(), v_disp_pr_mega_masers.max(), num = 35, endpoint = False),
        color = "green",
        edgecolor = 'white',
        density = True,
        alpha = 0.6,
        linewidth = 1,
        label = 'mega-masers'
           )
ax.hist(v_disp_pr_disk_masers,
        bins = np.linspace(v_disp_pr_disk_masers.min(), v_disp_pr_disk_masers.max(), num = 35, endpoint = False),
        color = "purple",
        edgecolor = 'white',
        density = True,
        alpha = 0.6,
        linewidth = 1,
        label = 'disk-masers'
           )

plt.legend(['Non-masers', 'Masers', 'Mega-masers', 'Disk masers'])

plt.show()

plt.figure()
fig, ax = plt.subplots(figsize = (10, 10))

ax.hist(masses_nm,
        bins = np.linspace(masses_nm.min(), masses_nm.max(), num = 35, endpoint = False),
        color = "gray",
        edgecolor = 'white',
        density = True,
        alpha = 0.6,
        linewidth = 1,
        label = 'non-masers'
           ) 
ax.hist(masses_m,
        bins = np.linspace(masses_m.min(), masses_m.max(), num = 35, endpoint = False),
        color = "blue",
        edgecolor = 'white',
        density = True,
        alpha = 0.6,
        linewidth = 1,
        label = 'masers'
           )
ax.hist(masses_mega_masers,
        bins = np.linspace(masses_mega_masers.min(), masses_mega_masers.max(), num = 35, endpoint = False),
        color = "green",
        edgecolor = 'white',
        density = True,
        alpha = 0.6,
        linewidth = 1,
        label = 'mega-masers'
           )
ax.hist(masses_disk_masers,
        bins = np.linspace(masses_disk_masers.min(), masses_disk_masers.max(), num = 35, endpoint = False),
        color = "purple",
        edgecolor = 'white',
        density = True,
        alpha = 0.6,
        linewidth = 1,
        label = 'disk-masers'
           )

plt.legend(['Non-masers', 'Masers', 'Mega-masers', 'Disk masers'])

plt.show()

plt.figure()
fig, ax = plt.subplots(figsize = (10, 10))

ax.hist(masses_nm_pr,
        bins = np.linspace(masses_nm_pr.min(), masses_nm_pr.max(), num = 35, endpoint = False),
        color = "gray",
        edgecolor = 'white',
        density = True,
        alpha = 0.6,
        linewidth = 1,
        label = 'non-masers'
           ) 
ax.hist(masses_m_pr,
        bins = np.linspace(masses_m_pr.min(), masses_m_pr.max(), num = 35, endpoint = False),
        color = "blue",
        edgecolor = 'white',
        density = True,
        alpha = 0.6,
        linewidth = 1,
        label = 'masers'
           )
ax.hist(masses_mega_masers_pr,
        bins = np.linspace(masses_mega_masers_pr.min(), masses_mega_masers_pr.max(), num = 35, endpoint = False),
        color = "green",
        edgecolor = 'white',
        density = True,
        alpha = 0.6,
        linewidth = 1,
        label = 'mega-masers'
           )
ax.hist(masses_disk_masers_pr,
        bins = np.linspace(masses_disk_masers_pr.min(), masses_disk_masers_pr.max(), num = 35, endpoint = False),
        color = "purple",
        edgecolor = 'white',
        density = True,
        alpha = 0.6,
        linewidth = 1,
        label = 'disk-masers'
           )

plt.legend(['Non-masers', 'Masers', 'Mega-masers', 'Disk masers'])

plt.show()

#%% Values for slide show

print('Sample size for non-masers is', ss_nm,
      '\nSample size for masers is', ss_m,
      '\nSample size for mega masers is', len(mega_masers),
      '\nSample size for disk masers', len(disk_masers),
      '\nSamples with veloctiy dispersions for non-masers is', len(v_disp_nm),
      '\nSamples with velocity dispersions for masers is', len(v_disp),
      '\nSamples with velocity dispersions for megamasers is', len(v_disp_mega_masers),
      '\nSamples with velocity dispersions for disk masers is', len(v_disp_disk_masers)
      )

#Expectation value of velocity dispersion
print('The expected value of velocity dispersion for non-masers is', exp_value(v_disp_nm),
      '\nThe expected value of velocity dispersion for masers is', exp_value(v_disp),
      '\nThe expected value of velocity dispersion for mega masers is', exp_value(v_disp_mega_masers),
      '\nThe expected value of velocity dispersion for disk masers is', exp_value(v_disp_disk_masers)
      )

#Expectation value of mass of black hole
print('The expected value of the mass of black hole for non-masers is', exp_value(masses_nm),
      '\nThe expected value of the mass of black hole for masers is', exp_value(masses_m),
      '\nThe expected value of the mass of black hole for mega masers is', exp_value(masses_mega_masers),
      '\nThe expected value of the mass of black hole for disk masers is', exp_value(masses_disk_masers)
      )

#Expectation value of mass of black hole, with pr > .75        
print('The expected value of the mass of black hole, with PR > .75, for non-masers is', exp_value(masses_nm_pr),
      '\nThe expected value of the mass of black hole, with PR > .75, for masers is', exp_value(masses_m_pr),
      '\nThe expected value of the mass of black hole, with PR > .75, for mega masers is', exp_value(masses_mega_masers_pr),
      '\nThe expected value of the mass of black hole, with PR > .75, for disk masers is', exp_value(masses_disk_masers_pr)
      )
