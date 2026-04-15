# Import libraries
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# All Data
file="final_data.csv"
data=pd.read_csv(file)

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

# Cumulative Flu Doses Distributed Every Week
dT=data["Cumulative_Flu_Doses_Distributed"]
weeks=np.linspace(0,258,258)
plt.scatter(weeks,dT)
plt.title("Cumulative Flu Doses Distributed Every Week August to March (2018-2026)")
plt.xlabel("Weeks")
plt.ylabel("Flu Doses Distributed (Millions)")
plt.grid()
plt.show()

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

plt.scatter(weeks,year1,label="Flue Doses" )
plt.plot(weeks,sum,color="green",label="Summer Mean")
plt.plot(weeks,fall,color="red",label="Fall Mean")
plt.plot(weeks,win,color="black",label="Winter Mean")
plt.xlabel("Weeks")
plt.ylabel("Flu Doses (Millions)")
plt.title("Cumulative Flu Doses 2018/2019: August through March")
plt.legend()
plt.grid()
plt.show()

# Mean for each week from 2018-2026
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

# Separating data by season for each year
summer=[]
fall=[]
n=0
for x in data["Reporting_TimeFrame"]:
    x=x.split("-")
    t=int(x[2])
    e=int(x[5])
    if x[1]==x[4]=="09":
        if 22 in range(t,e+1):
            summer.append(int(data["Week_Sort_Order"][n]))
            n+=1
        else:
            n+=1
            continue
    elif x[1]==x[4]=="12":
        if 21 in range(t,e+1):
            fall.append(int(data["Week_Sort_Order"][n]))
            n+=1
        else:
            n+=1
            continue
    else:
        n+=1
        continue

# Finding the mean of each season over all years
summ=[]
falll=[]
winn=[]
k=0
b=0
for x in data["Week_Sort_Order"]:
    if x in range(0,summer[k]+1):
        summ.append(float(data["Cumulative_Flu_Doses_Distributed"][b]))
    elif x in range(summer[k]+1,fall[k]+1):
        falll.append(float(data["Cumulative_Flu_Doses_Distributed"][b]))
    else:
        winn.append(float(data["Cumulative_Flu_Doses_Distributed"][b]))
    if x==32:
        k+=1
    b+=1

# Making data fit to graph
mean_sum=np.mean(summ)
sum=[]
c=0
while c<32:
    sum.append(mean_sum)
    c+=1
mean_fall=np.mean(falll)
fall=[]
d=0
while d<32:
    fall.append(mean_fall)
    d+=1
mean_win=np.mean(winn)
win=[]
e=0
while e<32:
    win.append(mean_win)
    e+=1

# Graphing mean by week and labeling mean by season over all years
weeks=np.linspace(0,32,32)
plt.scatter(weeks,me,label="Weekly Mean")
plt.plot(weeks,sum,color="green",label="Summer Mean")
plt.plot(weeks,fall,color="red",label="Fall Mean")
plt.plot(weeks,win,color="black",label="Winter Mean")
plt.xlabel("Weeks")
plt.ylabel("Flu Doses Distributed (Millions)")
plt.title("Mean Flu Doses Distributed Each Week From July to March (2018-2026)")
plt.legend()
plt.grid()
plt.show()

# August 2018 through March 2020
m=1
me=[]
while m<=32:
    b=0
    h=[]
    for x in data["Week_Sort_Order"]:
        if b>64:
            break
        elif x==m:
            h.append(float(data["Cumulative_Flu_Doses_Distributed"][b]))
        b+=1
    z=np.mean(h)
    me.append(float(z))
    m+=1

# August 2020 through March 2023
l=1
mee=[]
while l<=32:
    b=0
    h=[]
    for x in data["Week_Sort_Order"]:
        if b<=64 or b>160:
            continue
        elif x==l:
            h.append(float(data["Cumulative_Flu_Doses_Distributed"][b]))
            print(1)
        b+=1
    z=np.mean(h)
    mee.append(float(z))
    l+=1


# August 2023 through March 2026
m=1
meee=[]
while m<=32:
    b=0
    h=[]
    for x in data["Week_Sort_Order"]:
        if b<=160:
            break
        if x==m:
            h.append(float(data["Cumulative_Flu_Doses_Distributed"][b]))
        b+=1
    z=np.mean(h)
    meee.append(float(z))
    m+=1
print(me)
print(mee)
print(meee)


plt.scatter(weeks,me)
plt.xlabel("Weeks")
plt.ylabel("Flu Doses Distributed (Millions)")
plt.title("Mean Flu Doses Distributed Each Week From July to March (2018-2020)")
plt.grid()
plt.show()





