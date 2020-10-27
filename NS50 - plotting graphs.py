#!/usr/bin/env python
# coding: utf-8

# In[136]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

NS50_data = pd.read_csv("NS50_Data.csv")
NS50_data.head()
NS50_data.describe()


# In[2]:


time = list(NS50_data["TIME (year.decimal fraction)"])
green = list(NS50_data["Greenland mass (Gt)"])
ant = list(NS50_data["Antarctica mass (Gt)"])

plt.plot(time , ant ,label= "Antarctica mass (Gt)")
plt.plot(time , green ,label= "Greenland mass (Gt)",color = "green")
plt.title("Land Ice Mass from NASA")
plt.ylabel("Annual land ice mass anomalies(Gt)")
plt.xlabel("Time(years.decimal fraction)")
plt.legend()
plt.show()
print("Figure 1: Annunal land ice mass anomalies over time period(2002 to 2014)")
print("There is a net decrease in the land ice mass anomalies in gigatons for both Greenland and Antarctica(two major ice lands)")
print("Reduction in land ice mass is evidence of increasing temperatures being experienced globally")


# Line graph
# Scatter plot (variable 1 vs. variable 2)
# Histogram (student decision on how to bin the data for a histogram)
# Each figure should be accompanied by a brief caption (~600 character narrative description). For example captions look at any scientific paper that has figures in it. The caption should include:
# 
# A figure title (see readings and figures in class or in scientific articles for examples),
# A 1 sentence description of the pattern seen in the visualization,
# A 1 sentence description of the conclusions you might draw,
# Other pertinent information.

# In[3]:


plt.scatter(green,ant, color = "green")
plt.xlabel("Greenland Land Ice mass Anomalies(Gt)")
plt.ylabel("Antarctica Land Ice mass Anomalies(Gt)")
plt.title("Land Ice Mass from NASA")
plt.show()
print("Figure 2: Land ice mass anomalies of Antacrica as a function of the land ice mass anomalies of Greenland over a time period(2002-2014)")
print("The land ice mass of Greenland and Antarctica have a positive correlation(as one decreased or increased so did the other)")
print("We can conclude that whatever is affecting their land ice mass is on a global scale as these two places are far apart on the world map")


# In[4]:


plt.hist(ant, bins = 10)
plt.xlabel("Antarctica Land Ice mass Anomalies(Gt)")
plt.ylabel("Frequency")
plt.title("Land Ice Mass from NASA")
plt.show()
print("Figure 3: Distribution of the land ice mass anomalies of Antarctica over a time period(2002-2014)")
print("The distribution shows that most of the anomalies are positive")
print("We cannot conclude much from this histogram as it only shows a distribution of measurements but not at which point the data was measured")


# In[63]:


import numpy as np

approx_time = time[:]
for num in range(len(approx_time)):
    approx_time[num] = int(approx_time[num])
#print(approx_time)

gmean_set = []
amean_set = []
g_sd = []
a_sd = []
for num in range(2,15):
    
    gmass02 = []
    amass02 = []
    for mass in range(len(ant)):
        if approx_time[mass] == 2000 + num:
            amass02 = amass02 + [ant[mass]]
            gmass02 = gmass02 + [green[mass]]
    #print(amass02)
    amean_set.append(np.mean(amass02))
    #print(gmass02)
    gmean_set.append(np.mean(gmass02))
    a_sd.append(np.std(amass02))
    g_sd.append(np.std(gmass02))
import matplotlib.pyplot as plt
years = ["2002","2003","2004","2005","2006","2007","2008","2009","2010","2011","2012","2013","2014"]
pos = list(range(len(years)))
width = 0.4
plt.bar(pos, amean_set, width, yerr = a_sd, capsize = 3,label = "Land ice mass anomalies for Antarctica(Gt)")
plt.bar([p + width for p in pos],gmean_set, width, yerr = g_sd, capsize = 3, label = "Land ice mass anomalies for Greenland(Gt)")
plt.xlabel("Time in years after 2002")
plt.ylabel("Land Ice Mass Anomalies(Gt)")
plt.title("Yearly Land ice mass anomalies for Antarctica and Greenland in Gt")
plt.legend()
plt.show()


# In[2]:


import pandas as pd
df = pd.read_csv("NS50_Sci_Proposal.csv")
depth = list(df["depth"])
ice = list(df["ice_age"])
gas = list(df["gas_age"])
CO2 = list(df["CO2"])
temp = list(df["Temperature (calculated)"])
for _ in range(len(gas)):
    gas[_] = 0 - (gas[_])

for _ in range(len(ice)):
    ice[_] = 0 - (ice[_])
#m,ka,ka,ppmv,(deg C)
df.head()
#print(df)


# In[7]:


import matplotlib.pyplot as plt

plt.figure(figsize = (8,5))
ax = plt.gca()
ax2 = ax.twinx() 
#ax2.plot(gas,temp,label= "temp vs gas")
ax2.plot(ice,temp,label = "Calculated Temperature")
#ax.plot(gas,CO2,"r",label= "CO2 gas")
ax.plot(ice,CO2,"g",label = "CO2 concentration")
ax.set_xlabel("Age of Ice core(ka)")
ax.set_xticklabels(["180","160","140","120","100","80","60","40","20","0"])
ax.set_ylabel("CO2 Concentration(ppmv)")
ax2.set_ylabel("Calculated temperature(degrees Celsius)")
ax.legend(loc = 9)
ax2.legend()
plt.title("CO2 concentration and Calculated Temperature Against Icecore age")
plt.show()


# In[6]:


import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize = (8,5))
plt.scatter(CO2,temp)
plt.plot(np.unique(CO2), np.poly1d(np.polyfit(CO2, temp, 1))(np.unique(CO2)), "r", linewidth = 3)
plt.xlabel("CO2 Concentration(ppmv)")
plt.ylabel("Calculated Temperature(Degrees Celsuis)")
plt.title("Correlation between CO2 concentration and Calculated Temperature")
plt.show()
print("Correlation:",np.corrcoef(CO2,temp)[0][1])


# In[38]:


plt.plot(depth,ice)
plt.xlabel("Depth(m)")
plt.ylabel("Age of Ice core(ka)")
plt.show()


# In[ ]:




