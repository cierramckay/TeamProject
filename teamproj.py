""""
print("Hello!")
print("Eden was here!")
print("Lily was here!")
print("Chloe was here!!!!!!")
"""
import pandas as pd
from holoviews.ipython import display

file="final_data.csv"
data=pd.read_csv(file)
dose_col=data.loc[:,["Reporting_TimeFrame","Cumulative_Flu_Doses_Distributed"]]
display(dose_col)
