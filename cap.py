import matplotlib.pyplot as plt
import pandas as pd
import seaborn as se
import numpy as mp
df = pd.read_csv(r'/Users/aishwaryaagarwal/Desktop/PYTHON/penguins_size.csv')
print(df)
ds = se.get_dataset_names()
print(ds)
dfe = se.load_dataset('penguins')
print(df.head(25))
print(df.tail())
res = dfe.isnull().sum()
print(res)
deee = dfe.describe()
print(deee)