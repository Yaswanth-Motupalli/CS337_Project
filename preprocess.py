import pandas as pd

import numpy as np
import os
path = os.path.dirname(__file__)
path1 = os.path.join(path, 'dataset/processed.cleveland.data')
path3 = os.path.join(path, 'dataset/processed.switzerland.data')
path4 = os.path.join(path, 'dataset/processed.va.data')

df1 = pd.read_csv(path1)
df3 = pd.read_csv(path3)
df4 = pd.read_csv(path4)

df1 = df1.replace('?', np.nan)
df3 = df3.replace('?', np.nan)
df4 = df4.replace('?', np.nan)

col = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg',
       'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'num']
df1.columns = col
df3.columns = col
df4.columns = col

print("Cleveland data. Size={}\nNumber of missing values".format(df1.shape))
print(df1.isna().sum())

print("\nSwitzerland data. Size={}\nNumber of missing values".format(df3.shape))
print(df3.isna().sum())

print("\nV.A Long Beach data. Size={}\nNumber of missing values".format(df4.shape))
print(df4.isna().sum())

df = pd.concat([df1, df3, df4])
df=df.fillna(df.median())

#df=df.drop(['oldpeak', 'slope','ca', 'thal'], axis=1)
print("Concatanated dataset. Size={}\nNumber of missing values".format(df.shape))
print(df.isna().sum())

df.to_csv(os.path.join(path, 'dataset/heart-median.csv'), index=False)
