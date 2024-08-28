from sklearn.cluster import KMeans
from sklearn.model_selection import train_test_split
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import plotting

# set explain parameter.
df = pd.read_csv('train.csv')
df = df[['MedInc','AveRooms']]

# set number of group divieded
n=4
model=KMeans(n_clusters=n)
df['cluster']=model.fit_predict(df)
print(df['cluster'])

# show data
plt.figure(figsize=(8, 6))
colors = ['r', 'g','b','y']
for i in range(4):
    cluster_data = df[df['cluster'] == i]
    plt.scatter(cluster_data['MedInc'], cluster_data['AveRooms'], c=colors[i], label=f'Cluster {i+1}')

# plot center point
centers = model.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='k', marker='x', s=100, label='Cluster Centers')

plt.xlabel='MedInc'
plt.ylabel='AveRooms'
plt.title("Classify by Income and Rooms")
plt.legend()
plt.show()


