import matplotlib.pyplot as plt
import pandas as pd
import seaborn as se
se.set(color_codes=True)
df = pd.read_csv(r'/Users/aishwaryaagarwal/Desktop/PYTHON/USA_Housing.csv')
se.barplot(x='Avg. Area Income', y='Area Population', data=df, ci=None)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()