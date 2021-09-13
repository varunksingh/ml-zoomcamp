import numpy as np
import pandas as pd
np.__version__
pd.__version__
data = pd.read_csv('data.csv')
new_data = data.loc[data['Make'] == 'BMW']
new_data.MSRP.mean()
data_4 = data.loc[data['Year'] >= 2015]
data_4.isna().sum()
data.isna().sum()
mean_hp_before = data['Engine HP'].mean()
print(round(mean_hp_before))
data[['Enginer HP']] = data[['Engine HP']].fillna(value=mean_hp_before)
mean_hp_after = data['Engine HP'].mean()
print(round(mean_hp_after))
new_data = data.loc[data['Make'] == 'Rolls-Royce']
new_data_sub = new_data[["Engine HP", "Engine Cylinders", "highway MPG"]]
new_data_sub_1 = new_data_sub.drop_duplicates()
X = new_data_sub_1.to_numpy()
XTX = X.T.dot(X)
from numpy.linalg import inv
result = inv(XTX)
result.sum()
y = np.array([1000, 1100, 900, 1200, 1000, 850, 1300])
w = result.dot(X.T).dot(y)
