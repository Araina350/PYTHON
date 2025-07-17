import pandas as pd
import numpy as np
employee_data = {'Name':['Pankaj','Meghna','David','Lisa'],'Role':['CEO',' ',' ',' '],'Salary':[150000000,200000000,' ',' ']}
df = pd.DataFrame(employee_data)
print(df)
new_df = df.dropna()
print(new_df.to_string())
print(new_df.info())
