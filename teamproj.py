# Import libraries
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

# All Data
file="final_data.csv"
data=pd.read_csv(file)


month_means = []
months = ["Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar"]

for x in range(len(months)):
    v = []
    s = 0

    for i in data["End_Date"]:
        if months[x] in str(i):
            current = float(data["Cumulative_Flu_Doses_Distributed"][s])

            # August has no previous month, so keep original value
            if x == 0:
                v.append(current)

            else:
                prev_month = months[x - 1]

                # find previous month's cumulative value
                prev_value = None
                t = 0
                for j in data["End_Date"]:
                    if prev_month in str(j):
                        prev_value = float(data["Cumulative_Flu_Doses_Distributed"][t])

                # subtract previous month cumulative total
                        if t < s:
                            prev_value = float(data["Cumulative_Flu_Doses_Distributed"][t])
                    t += 1

                if prev_value is not None:
                    v.append(current - prev_value)

        s += 1

    new = np.mean(v)
    month_means.append(float(new))
plt.figure()
plt.bar(months, month_means)
plt.ylabel("Mean Flu Doses Distributed (Millions)")
plt.title("Mean Flu Doses Distributed From August to March: 2018–2026")
plt.grid()
plt.show()

# Cumulative Flu Doses Distributed Every Week
dT=data["Cumulative_Flu_Doses_Distributed"]
weeks=np.linspace(0,258,258)
plt.scatter(weeks,dT)
plt.title("Cumulative Flu Doses Distributed Every Week August to March (2018-2026)")
plt.xlabel("Weeks (32 per year)")
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
plt.figure()
plt.scatter(weeks,year1,label="Flu Doses" )
plt.plot(weeks,sum,color="green",label="Summer Mean")
plt.plot(weeks,fall,color="red",label="Fall Mean")
plt.plot(weeks,win,color="black",label="Winter Mean")
plt.xlabel("Weeks: August to March")
plt.ylabel("Flu Doses (Millions)")
plt.title("Cumulative Flu Doses 2018/2019: August through March")
plt.legend()
plt.grid()
plt.show()

# Replace every use of:
# data["Cumulative_Flu_Doses_Distributed"]

# with this new column first:

data["Weekly_Doses"] = 0.0

b = 0
for x in data["Week_Sort_Order"]:
    current = float(data["Cumulative_Flu_Doses_Distributed"][b])

    # first week of each flu season stays the same
    if x == 1:
        data.loc[b, "Weekly_Doses"] = current

    else:
        prev_value = float(data["Cumulative_Flu_Doses_Distributed"][b - 1])
        data.loc[b, "Weekly_Doses"] = current - prev_value

    b += 1


# =========================================================
# Mean for each week from 2018–2026 (NON-CUMULATIVE)
# =========================================================

m = 1
me = []

while m <= 32:
    b = 0
    h = []

    for x in data["Week_Sort_Order"]:
        if x == m:
            h.append(float(data["Weekly_Doses"][b]))
        b += 1

    z = np.mean(h)
    me.append(float(z))
    m += 1


# =========================================================
# PRE COVID (2018–2020)
# =========================================================

m = 1
pre_mean = []

while m <= 32:
    b = 0
    h = []

    for x in data["Week_Sort_Order"]:
        if b > 64:
            break

        elif x == m:
            h.append(float(data["Weekly_Doses"][b]))

        b += 1

    z = np.mean(h)
    pre_mean.append(float(z))
    m += 1


# =========================================================
# DURING COVID (2020–2023)
# =========================================================

m = 1
during_mean = []

while m <= 32:
    b = 0
    h = []

    for x in data["Week_Sort_Order"]:
        if b <= 64 or b > 160:
            b += 1
            continue

        elif x == m:
            h.append(float(data["Weekly_Doses"][b]))

        b += 1

    z = np.mean(h)
    during_mean.append(float(z))
    m += 1


# =========================================================
# POST COVID (2023–2026)
# =========================================================

m = 1
post_mean = []

while m <= 32:
    b = 0
    h = []

    for x in data["Week_Sort_Order"]:
        if b <= 160:
            b += 1
            continue

        elif x == m:
            h.append(float(data["Weekly_Doses"][b]))

        b += 1

    z = np.mean(h)
    post_mean.append(float(z))
    m += 1


# =========================================================
# SEASONAL MEANS
# =========================================================

summer = []
fall = []
winter = []

for i in range(len(me)):
    week = i + 1

    if week <= 8:
        summer.append(me[i])

    elif week <= 20:
        fall.append(me[i])

    else:
        winter.append(me[i])

mean_sum = np.mean(summer)
mean_fall = np.mean(fall)
mean_win = np.mean(winter)


# PRE seasonal means

summer_pre = pre_mean[:8]
fall_pre = pre_mean[8:20]
winter_pre = pre_mean[20:]

mean_sumPRE = np.mean(summer_pre)
mean_fallPRE = np.mean(fall_pre)
mean_winPRE = np.mean(winter_pre)


# DURING seasonal means

summer_dur = during_mean[:8]
fall_dur = during_mean[8:20]
winter_dur = during_mean[20:]

mean_sumDUR = np.mean(summer_dur)
mean_fallDUR = np.mean(fall_dur)
mean_winDUR = np.mean(winter_dur)


# POST seasonal means

summer_post = post_mean[:8]
fall_post = post_mean[8:20]
winter_post = post_mean[20:]

mean_sumPOST = np.mean(summer_post)
mean_fallPOST = np.mean(fall_post)
mean_winPOST = np.mean(winter_post)


# =========================================================
# GRAPHS
# =========================================================

weeks = np.linspace(1, 32, 32)


# ALL YEARS
plt.figure()
plt.scatter(weeks, me, label="Weekly Mean")

plt.axhline(float(mean_sum), label="Summer Mean")
plt.axhline(float(mean_fall), label="Fall Mean")
plt.axhline(float(mean_win), label="Winter Mean")

plt.xlabel("Weeks: August to March")
plt.ylabel("Flu Doses Distributed (Millions)")
plt.title("Weekly Flu Doses Distributed (2018–2026)")
plt.legend()
plt.grid()
plt.show()


# LAYERED PRE / DURING / POST
plt.figure()
plt.scatter(weeks, pre_mean, label="Pre COVID")
plt.scatter(weeks, during_mean, label="During COVID")
plt.scatter(weeks, post_mean, label="Post COVID")

plt.xlabel("Weeks")
plt.ylabel("Flu Doses Distributed (Millions)")
plt.title("Pre vs During vs Post COVID")
plt.legend()
plt.grid()
plt.show()


# SEASONAL BAR CHARTS

time = ["Pre", "During", "Post"]
plt.figure()
plt.bar(time, [mean_sumPRE, mean_sumDUR, mean_sumPOST])
plt.title("Summer Mean Weekly Doses")
plt.ylabel("Millions")
plt.show()
plt.figure()
plt.bar(time, [mean_fallPRE, mean_fallDUR, mean_fallPOST])
plt.title("Fall Mean Weekly Doses")
plt.ylabel("Millions")
plt.show()

plt.figure()
plt.bar(time, [mean_winPRE, mean_winDUR, mean_winPOST])
plt.title("Winter Mean Weekly Doses")
plt.ylabel("Millions")
plt.show()







#below is the original code before we tried to change it

# Mean for each week from 2018-2026 (weekly doses only, not cumulative)

m = 1
me = []

while m <= 32:
    b = 0
    h = []

    for x in data["Week_Sort_Order"]:
        if x == m:
            current = float(data["Cumulative_Flu_Doses_Distributed"][b])

            # Week 1 stays the same since there is no previous week
            if m == 1:
                h.append(current)

            else:
                prev_value = None
                t = 0

                # find previous week's cumulative value
                for y in data["Week_Sort_Order"]:
                    if y == m - 1:
                        if t < b:
                            prev_value = float(data["Cumulative_Flu_Doses_Distributed"][t])
                    t += 1

                # subtract previous week's cumulative total
                if prev_value is not None:
                    h.append(current - prev_value)

        b += 1

    z = np.mean(h)
    me.append(float(z))
    m += 1


# Separating data by season for each year
summer = []
fall = []
n = 0

for x in data["Reporting_TimeFrame"]:
    x = x.split("-")
    t = int(x[2])
    e = int(x[5])

    if x[1] == x[4] == "09":
        if 22 in range(t, e + 1):
            summer.append(int(data["Week_Sort_Order"][n]))
            n += 1
        else:
            n += 1
            continue

    elif x[1] == x[4] == "12":
        if 21 in range(t, e + 1):
            fall.append(int(data["Week_Sort_Order"][n]))
            n += 1
        else:
            n += 1
            continue

    else:
        n += 1
        continue


# Finding the mean of each season over all years (non-cumulative weekly values)

sumT = []
fallT = []
winT = []

k = 0
b = 0

for x in data["Week_Sort_Order"]:
    current = float(data["Cumulative_Flu_Doses_Distributed"][b])

    # convert cumulative → weekly-only
    if x == 1:
        weekly_value = current
    else:
        prev_value = None
        t = 0

        for y in data["Week_Sort_Order"]:
            if y == x - 1:
                if t < b:
                    prev_value = float(data["Cumulative_Flu_Doses_Distributed"][t])
            t += 1

        if prev_value is not None:
            weekly_value = current - prev_value
        else:
            weekly_value = current

    if x in range(0, summer[k] + 1):
        sumT.append(weekly_value)

    elif x in range(summer[k] + 1, fall[k] + 1):
        fallT.append(weekly_value)

    else:
        winT.append(weekly_value)

    if x == 32:
        k += 1

    b += 1


# Mean of seasons relating to COVID (non-cumulative weekly values)

sumPRE = []
fallPRE = []
winPRE = []

sumDUR = []
fallDUR = []
winDUR = []

sumPOST = []
fallPOST = []
winPOST = []

k = 0
b = 0

for x in data["Week_Sort_Order"]:
    current = float(data["Cumulative_Flu_Doses_Distributed"][b])

    # convert cumulative → weekly-only
    if x == 1:
        weekly_value = current
    else:
        prev_value = None
        t = 0

        for y in data["Week_Sort_Order"]:
            if y == x - 1:
                if t < b:
                    prev_value = float(data["Cumulative_Flu_Doses_Distributed"][t])
            t += 1

        if prev_value is not None:
            weekly_value = current - prev_value
        else:
            weekly_value = current

    if k < 2:
        if x in range(0, summer[k] + 1):
            sumPRE.append(weekly_value)
        elif x in range(summer[k] + 1, fall[k] + 1):
            fallPRE.append(weekly_value)
        else:
            winPRE.append(weekly_value)

    elif k < 5:
        if x in range(0, summer[k] + 1):
            sumDUR.append(weekly_value)
        elif x in range(summer[k] + 1, fall[k] + 1):
            fallDUR.append(weekly_value)
        else:
            winDUR.append(weekly_value)

    else:
        if x in range(0, summer[k] + 1):
            sumPOST.append(weekly_value)
        elif x in range(summer[k] + 1, fall[k] + 1):
            fallPOST.append(weekly_value)
        else:
            winPOST.append(weekly_value)

    if x == 32:
        k += 1

    b += 1

# Making data (ALL) fit to graph
mean_sum=np.mean(sumT)
sum=[]
c=0
while c<32:
    sum.append(mean_sum)
    c+=1
mean_fall=np.mean(fallT)
fall=[]
d=0
while d<32:
    fall.append(mean_fall)
    d+=1
mean_win=np.mean(winT)
win=[]
e=0
while e<32:
    win.append(mean_win)
    e+=1

# Making PRE data fit to graph
mean_sumPRE=np.mean(sumPRE)
sumPR=[]
c=0
while c<32:
    sumPR.append(mean_sumPRE)
    c+=1
mean_fallPRE=np.mean(fallPRE)
fallPR=[]
d=0
while d<32:
    fallPR.append(mean_fallPRE)
    d+=1
mean_winPRE=np.mean(winPRE)
winPR=[]
e=0
while e<32:
    winPR.append(mean_winPRE)
    e+=1

# Making DUR data fit to graph
mean_sumDUR=np.mean(sumDUR)
sumD=[]
c=0
while c<32:
    sumD.append(mean_sumDUR)
    c+=1
mean_fallDUR=np.mean(fallDUR)
fallD=[]
d=0
while d<32:
    fallD.append(mean_fallDUR)
    d+=1
mean_winDUR=np.mean(winDUR)
winD=[]
e=0
while e<32:
    winD.append(mean_winDUR)
    e+=1

# Making POST data fit to graph
mean_sumPOST=np.mean(sumPOST)
sumPO=[]
c=0
while c<32:
    sumPO.append(mean_sumPOST)
    c+=1
mean_fallPOST=np.mean(fallPOST)
fallPO=[]
d=0
while d<32:
    fallPO.append(mean_fallPOST)
    d+=1
mean_winPOST=np.mean(winPOST)
winPO=[]
e=0
while e<32:
    winPO.append(mean_winPOST)
    e+=1

print("Pre COVID:")
print("Summer:",mean_sumPRE)
print("Fall:",mean_fallPRE)
print("Winter:",mean_winPRE)

print("During COVID:")
print("Summer:",mean_sumDUR)
print("Fall:",mean_fallDUR)
print("Winter:",mean_winDUR)

print("Post COVID:")
print("Summer:",mean_sumPOST)
print("Fall:",mean_fallPOST)
print("Winter:",mean_winPOST)


# Graphing mean by week and labeling mean by season over all years
weeks=np.linspace(0,32,32)
plt.scatter(weeks,me,label="Weekly Mean")
plt.plot(weeks,sum,color="green",label="Summer Mean")
plt.plot(weeks,fall,color="red",label="Fall Mean")
plt.plot(weeks,win,color="black",label="Winter Mean")
plt.xlabel("Weeks: August to March")
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
            b+=1
            continue
        elif x==l:
            h.append(float(data["Cumulative_Flu_Doses_Distributed"][b]))
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
            b+=1
            continue
        if x==m:
            h.append(float(data["Cumulative_Flu_Doses_Distributed"][b]))
        b+=1
    z=np.mean(h)
    meee.append(float(z))
    m+=1

# All data
plt.scatter(weeks,me,color="blue",label="Pre Covid")
plt.scatter(weeks,mee,color="green",label="During Covid")
plt.scatter(weeks,meee,color="orange",label="Post Covid")
plt.xlabel("Weeks: August to March")
plt.ylabel("Flu Doses Distributed (Millions)")
plt.title("Flu Doses Distributed Pre, Post, and During Peak COVID-19")
plt.legend()
plt.grid()
plt.show()

# Pre COVID
plt.scatter(weeks,me,color="blue")
plt.plot(weeks,sumPR,color="green",label="Summer Mean")
plt.plot(weeks,fallPR,color="red",label="Fall Mean")
plt.plot(weeks,winPR,color="black",label="Winter Mean")
plt.xlabel("Weeks: August to March")
plt.ylabel("Flu Doses Distributed (Millions)")
plt.title("Flu Doses Distributed Pre Peak COVID-19 (2018-2020)")
plt.legend()
plt.grid()
plt.show()

# During COVID
plt.scatter(weeks,mee,color="green")
plt.plot(weeks,sumD,color="green",label="Summer Mean")
plt.plot(weeks,fallD,color="red",label="Fall Mean")
plt.plot(weeks,winD,color="black",label="Winter Mean")
plt.xlabel("Weeks: August to March")
plt.ylabel("Flu Doses Distributed (Millions)")
plt.title("Flu Doses Distributed During Peak COVID-19 (2020-2023)")
plt.legend()
plt.grid()
plt.show()

# Post COVID
plt.scatter(weeks,meee,color="orange")
plt.plot(weeks,sumPO,color="green",label="Summer Mean")
plt.plot(weeks,fallPO,color="red",label="Fall Mean")
plt.plot(weeks,winPO,color="black",label="Winter Mean")
plt.xlabel("Weeks: August to March")
plt.ylabel("Flu Doses Distributed (Millions)")
plt.title("Flu Doses Distributed Post Peak COVID-19 (2023-2026)")
plt.legend()
plt.grid()
plt.show()

# Summer doses relating to COVID
time=["Pre","During","Post"]
colors=["blue","green","orange"]
summer=[mean_sumPRE,mean_sumDUR,mean_sumPOST]
plt.bar(time,summer,color=colors,edgecolor="blue")
plt.ylabel("Mean Flu Doses Per Week (Millions)")
plt.xlabel("COVID-19")
plt.title("Mean Flu Doses Distributed in Summer Pre, During, and Post COVID")
plt.show()

# Fall doses relating to COVID
fall=[mean_fallPRE,mean_fallDUR,mean_fallPOST]
plt.bar(time,fall,color=colors,edgecolor="red")
plt.ylabel("Mean Flu Doses Per Week (Millions)")
plt.xlabel("COVID-19")
plt.title("Mean Flu Doses Distributed in Fall Pre, During, and Post COVID")
plt.show()

# Winter doses relating to COVID
winter=[mean_winPRE,mean_winDUR,mean_winPOST]
plt.bar(time,winter,color=colors,edgecolor="black")
plt.ylabel("Mean Flu Doses Per Week (Millions)")
plt.xlabel("COVID-19")
plt.title("Mean Flu Doses Distributed in Winter Pre, During, and Post COVID")
plt.show()