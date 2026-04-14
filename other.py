

summer=[]
fall=[]
winter=[]
n=0
for x in data["Reporting_TimeFrame"]:
    x=x.split("-")
    t=int(x[2])
    e=int(x[5])
    if x[1]==x[4]=="09":
        if 22 in range(t,e):
            summer.append(int(data["Week_Sort_Order"][n]))
            n+=1
        else:
            n+=1
            continue

    else:
        n+=1
        continue
print(n)
print(summer)






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
