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

file="final_data.csv"
data=pd.read_csv(file)
key_col=data.loc[:,["Reporting_TimeFrame","Week_Sort_Order","Cumulative_Flu_Doses_Distributed"]]
display(key_col)
year1=[]
b=0
for x in data["Week_Sort_Order"]:
    year1.append(float(data["Cumulative_Flu_Doses_Distributed"][b]))
    if x==32:
        break
    b+=1
weeks=np.linspace(0,32,32)
plt.scatter(weeks,year1)
plt.xlabel("Weeks")
plt.ylabel("Flu Doses (Millions)")
plt.title("Cumulative Flu Doses 2018/2019: July through March")
plt.grid()
plt.show()