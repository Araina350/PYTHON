import pandas as pd
import numpy as np
exam_data = {'name':['Anastasia','Kevin','Jonas','Darsh','Purvi','Anam','Laura'],'score':[99,56,43,90,99,33,100],'qualify':['yes','no','no','yes','yes','no','yes']}
labels = ['a','b','c','d','e','f','g']
df = pd.DataFrame(exam_data, index=labels)
print(df)
print(df.info())