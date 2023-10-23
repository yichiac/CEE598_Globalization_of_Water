import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# random forest
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

def randomforest(data, target):
    Xtrain, Xtest, ytrain, ytest = train_test_split(data, target, random_state=5, test_size=0.25)
    rf = RandomForestRegressor(max_depth=5, random_state=0, n_estimators=1000)
    rf.fit(Xtrain, ytrain)
    # ypred = rf.predict(Xtest)
    score = rf.score(Xtest, ytest)
    return score

# for all clusters
# df = pd.read_csv('All_Regression_Data.csv')
# features = ['Pop_change_all', 'Income_change_all', 'Ag_change_all','Livstk_change_all', 'Avg_Rain_all', 'Avg_Temp_all', 'cluster_all']
# target = df['Water_change_all'].to_numpy()
# data = df[features].to_numpy()
# n_samples, n_features = data.shape
# score = randomforest(data, target)
# print('RF Score: ', score)

# for cluster 0
# df = pd.read_csv('Clust_0_Rgrsn_Data.csv')
# features = ['Pop_change_all', 'Income_change_all', 'Ag_change_all','Livstk_change_all', 'Avg_Rain_all', 'Avg_Temp_all']
# target = df['Water_change_all'].to_numpy()
# data = df[features].to_numpy()
# n_samples, n_features = data.shape
# score = randomforest(data, target)
# print('RF Score: ', score)


# for cluster 0 - 7, need to find the concrete params for running all clusters.
features = ['Pop_change_all', 'Income_change_all', 'Ag_change_all','Livstk_change_all', 'Avg_Rain_all', 'Avg_Temp_all']
for i in range(8):
    filename = 'Clust_' + str(i) + '_Rgrsn_Data.csv'
    df = pd.read_csv(filename)
    target = df['Water_change_all'].to_numpy()
    data = df[features].to_numpy()
    score = randomforest(data, target)
    print('Cluster ' + str(i) + ' RF Score: ' + str(score))

# ANN