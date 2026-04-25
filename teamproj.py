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

plt.axhline(float(mean_sum), label="Summer Mean",color="yellow")
plt.axhline(float(mean_fall), label="Fall Mean",color="orange")
plt.axhline(float(mean_win), label="Winter Mean",color="red")

plt.xlabel("Weeks: August to March")
plt.ylabel("Flu Doses Distributed (Millions)")
plt.title("Weekly Flu Doses Distributed (2018–2026)")
plt.legend()
plt.grid()
plt.show()


# LAYERED PRE / DURING / POST
plt.figure()
plt.scatter(weeks, pre_mean, label="Pre COVID",color="green")
plt.scatter(weeks, during_mean, label="During COVID",color="blue")
plt.scatter(weeks, post_mean, label="Post COVID",color="purple")
plt.plot(weeks, pre_mean,color="green")
plt.plot(weeks, during_mean,color="blue")
plt.plot(weeks, post_mean,color="purple")

plt.xlabel("Weeks")
plt.ylabel("Flu Doses Distributed (Millions)")
plt.title("Pre vs During vs Post COVID")
plt.legend()
plt.grid()
plt.show()

# PRE
plt.figure()
plt.scatter(weeks, pre_mean, label="Pre COVID",color="green")
plt.plot(weeks, pre_mean,color="green")

plt.xlabel("Weeks")
plt.ylabel("Flu Doses Distributed (Millions)")
plt.title("Pre COVID")
plt.legend()
plt.grid()
plt.show()

# DURING

plt.figure()
plt.scatter(weeks, during_mean, label="During COVID",color="blue")
plt.plot(weeks, during_mean,color="blue")

plt.xlabel("Weeks")
plt.ylabel("Flu Doses Distributed (Millions)")
plt.title("During COVID")
plt.legend()
plt.grid()
plt.show()

# POST

plt.figure()
plt.scatter(weeks, post_mean, label="Post COVID",color="purple")
plt.plot(weeks, post_mean,color="purple")

plt.xlabel("Weeks")
plt.ylabel("Flu Doses Distributed (Millions)")
plt.title("Post COVID")
plt.legend()
plt.grid()
plt.show()

# SEASONAL BAR CHARTS

time = ["Pre", "During", "Post"]
colors=["green","blue","purple"]
plt.figure()
plt.bar(time, [mean_sumPRE, mean_sumDUR, mean_sumPOST],color=colors)
plt.title("Summer Mean Weekly Doses")
plt.ylabel("Millions")
plt.show()
plt.figure()
plt.bar(time, [mean_fallPRE, mean_fallDUR, mean_fallPOST],color=colors)
plt.title("Fall Mean Weekly Doses")
plt.ylabel("Millions")
plt.show()

plt.figure()
plt.bar(time, [mean_winPRE, mean_winDUR, mean_winPOST],color=colors)
plt.title("Winter Mean Weekly Doses")
plt.ylabel("Millions")
plt.show()

from scipy.stats import ttest_ind
peak_months = []
other_months = []
for x in range(len(months)):
    v = []
    s = 0
    for i in data["End_Date"]:
        if months[x] in str(i):
            current = float(data["Cumulative_Flu_Doses_Distributed"][s])
            if x == 0:
                monthly_dose = current
            else:
                prev_month = months[x-1]
                prev_value = None
                t = 0
                for j in data["End_Date"]:
                    if prev_month in str(j):
                        if t < s:
                            prev_value = float(
                                data["Cumulative_Flu_Doses_Distributed"][t]
                            )
                    t += 1
                if prev_value is not None:
                    monthly_dose = current - prev_value
                else:
                    s += 1
                    continue
            if months[x] in ["Sep","Oct","Nov"]:
                peak_months.append(monthly_dose)
            else:
                other_months.append(monthly_dose)
        s += 1

# Independent t-test
t_stat, p_value = ttest_ind(peak_months, other_months, equal_var=False)
print("t =", t_stat)
print("p =", p_value)
if p_value < 0.05:
    print("September to November is significantly higher.")
else:
    print("No significant difference.")
