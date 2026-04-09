""""
print("Hello!")
print("Eden was here!")
print("Lily was here!")
print("Chloe was here!!!!!!")
"""
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from holoviews.ipython import display

# All Important Data
file="final_data.csv"
data=pd.read_csv(file)
key_col=data.loc[:,["Reporting_TimeFrame","Week_Sort_Order","Cumulative_Flu_Doses_Distributed"]]
display(key_col)

# Year 1 Data
year1=[]
b=0
for x in data["Week_Sort_Order"]:
    year1.append(float(data["Cumulative_Flu_Doses_Distributed"][b]))
    if x==32:
        break
    b+=1
weeks=np.linspace(0,32,32)

summer=year1[:9]
fall=year1[9:22]
winter=year1[22:]

mean_sum=np.mean(summer)
sum=[]
c=0
while c<32:
    sum.append(mean_sum)
    c+=1
mean_fall=np.mean(fall)
fall=[]
d=0
while d<32:
    fall.append(mean_fall)
    d+=1
mean_win=np.mean(winter)
win=[]
e=0
while e<32:
    win.append(mean_win)
    e+=1

plt.scatter(weeks,year1)
plt.plot(weeks,sum,color="green")
plt.plot(weeks,fall,color="red")
plt.plot(weeks,win,color="black")
plt.xlabel("Weeks")
plt.ylabel("Flu Doses (Millions)")
plt.title("Cumulative Flu Doses 2018/2019: July through March")
plt.grid()
plt.show()



