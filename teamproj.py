import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# All Important Data
file="final_data.csv"
data=pd.read_csv(file)

""""

# Using all data: Dose mean for each month

month_means=[]
months=["Aug","Sep","Oct","Nov","Dec","Jan","Feb","Mar"]
for x in months:
    v=[]
    s=0
    for i in data["End_Date"]:
        if x in i:
            v.append(float(data["Cumulative_Flu_Doses_Distributed"][s]))
        s+=1
    new=np.mean(v)
    month_means.append(float(new))
plt.bar(months,month_means)
plt.ylabel("Mean Flu Doses Distributed (Millions)")
plt.title("Mean Flu Doses Distributed From August to March: 2018-2026")
plt.grid()
plt.show()

# All Data
dT=data["Cumulative_Flu_Doses_Distributed"]
weeks=np.linspace(0,258,258)
plt.scatter(weeks,dT)
plt.title("All Data")
plt.xlabel("Weeks")
plt.ylabel("Flu Doses Distributed (Millions)")
plt.grid()
plt.show()
"""
m=1
me=[]
while m<=32:
    b=0
    h=[]
    for x in data["Week_Sort_Order"]:
        if x==m:
            h.append(float(data["Cumulative_Flu_Doses_Distributed"][b]))
        b+=1
    z=np.mean(h)
    me.append(float(z))
    m+=1

weeks=np.linspace(0,32,32)

plt.scatter(weeks,me)
plt.xlabel("Weeks")
plt.ylabel("Flu Doses Distributed (Millions)")
plt.title("Mean of Each Week (2018-2026)")
plt.grid()
plt.show()






