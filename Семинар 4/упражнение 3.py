import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv('iris_data-2.csv')
print(df)
m = df['Species'].unique()
plt.pie([list(df['Species']).count(i) for i in m], labels = m)
plt.show()

