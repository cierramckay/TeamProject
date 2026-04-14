import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# All Important Data
file="final_data.csv"
data=pd.read_csv(file)

# Year 1 Data
print("Year 1:")
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
print("Summer mean",mean_sum)
mean_fall=np.mean(fall)
fall=[]
d=0
while d<32:
    fall.append(mean_fall)
    d+=1
print("Fall mean",mean_fall)
mean_win=np.mean(winter)
win=[]
e=0
while e<32:
    win.append(mean_win)
    e+=1
print("Winter mean",mean_win)

plt.scatter(weeks,year1,label="Flue Doses" )
plt.plot(weeks,sum,color="green",label="Summer Mean")
plt.plot(weeks,fall,color="red",label="Fall Mean")
plt.plot(weeks,win,color="black",label="Winter Mean")
plt.xlabel("Weeks")
plt.ylabel("Flu Doses (Millions)")
plt.title("Cumulative Flu Doses 2018/2019: July through March")
plt.legend()
plt.grid()
plt.show()


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

