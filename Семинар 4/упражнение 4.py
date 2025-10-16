import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


df = pd.read_csv('iris_data-2.csv')

d = {'PetalLength <= 1.2':0, '1.2 < PetalLength <= 1.5' : 0, 'PetalLength >1.5' : 0}

for i in list(df['PetalLengthCm']):
    if i <= 1.2:
        d['PetalLength <= 1.2'] += 1
    elif i > 1.5:
        d['PetalLength >1.5'] += 1
    else:
        d['1.2 < PetalLength <= 1.5'] += 1
plt.pie(list(d.values()), labels = list(d.keys()))
plt.show()