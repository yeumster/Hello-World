##import numpy as np
##import pandas as pd
##import matplotlib.pyplot as plt
##from sklearn.cluster import KMeans
##from sklearn import datasets
##
##
### Loading the iris data
##iris = datasets.load_iris()
##X = iris.data    # Data
##y = iris.target  # Target i.e., true clusters
##varNames = iris.feature_names  # variable names
##targetNames = iris.target_names  # names of irises
##nVar = X.shape[1]  # number of features
##
##
##
### combining features as a dataframe
##featureData = pd.DataFrame(X, columns=varNames)
##
### creating a list of colors
##yColor = []
##colorVector = 'rgb'
##for iClass in range(3):
##    yColor = yColor + ([colorVector[iClass]] * len(y[y==iClass]))
##
### plotting the scatter plot matrix
##pd.plotting.scatter_matrix(featureData, figsize=[9,9], color=yColor)
##plt.show()
##
##
##
##
### K-means clustering
##numClus = 3  # number of clusters
##km = KMeans(n_clusters=numClus)  # defining the clustering object
##km.fit(X)  # actually fitting the data
##y_clus = km.labels_   # clustering info resulting from K-means
##y_cent = km.cluster_centers_  # centroid coordinates
##
##### plotting the clusters
##plt.figure(figsize=[8,4])
### First, results from K-means
##plt.subplot(121)
##plt.scatter(X[:,3],X[:,0],c=y_clus,marker='+')
##plt.plot(y_cent[:,3],y_cent[:,0],'r^')  # Ploting centroids
##plt.xlabel('Petal width')
##plt.ylabel('Sepal length')
##plt.title('Clusters from K-means')
##
### As a comparison, the true clusters
##plt.subplot(122)
##plt.scatter(X[:,3],X[:,0],c=yColor,marker='+')
##plt.xlabel('Petal width')
##plt.ylabel('Sepal length')
##plt.title('True clusters')
##
##plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, adjusted_mutual_info_score

# loadin the data
seedData = pd.read_csv('seeds_dataset.txt', sep='\t', header=None)
seedFeatures = np.array(seedData.iloc[:,:7])
seedTargets = np.array(seedData.iloc[:,7])
targetNames = ['Kama','Rosa','Canadian']

# feature names
featureNames = ['area',
                'perimeter',
                'compactness',
                'length of kernel',
                'width of kernel',
                'asymmetry coefficient',
                'length of kernel groove',
                'class']
seedData.columns = featureNames


# creating a list of colors
yColor = []
colorVector = 'rgb'
for iClass in range(1,4):
    yColor = yColor + ([colorVector[iClass-1]] * len(seedTargets[seedTargets==iClass]))

### plotting the scatter plot matrix
##pd.plotting.scatter_matrix(seedData.iloc[:,:7], figsize=[9,9], color=yColor)
##plt.show()



# K-means clustering
numClus = 3  # number of clusters
km = KMeans(n_clusters=numClus)  # defining the clustering object
km.fit(seedFeatures)  # actually fitting the data
y_clus = km.labels_   # clustering info resulting from K-means

# ARI
print('ARI =  %7.4f' % adjusted_rand_score(seedTargets, y_clus))
# AMI
print('AMI =  %7.4f' % adjusted_mutual_info_score(seedTargets, y_clus))

### plotting the clusters
##plt.figure(figsize=[8,4])
##xFeature = 6
##yFeature = 5
### First, results from K-means
##plt.subplot(121)
##plt.scatter(seedFeatures[:,xFeature],
##            seedFeatures[:,yFeature], c=y_clus, marker='+')
##plt.xlabel(featureNames[xFeature])
##plt.ylabel(featureNames[yFeature])
##plt.title('Clusters from K-means')
##
### As a comparison, the true clusters
##plt.subplot(122)
##plt.scatter(seedFeatures[:,xFeature],
##            seedFeatures[:,yFeature], c=yColor, marker='+')
##plt.xlabel(featureNames[xFeature])
##plt.ylabel(featureNames[yFeature])
##plt.title('True clusters')
##
##plt.show()


##import numpy as np
##import matplotlib.pyplot as plt
##from sklearn.cluster import KMeans
##from sklearn import datasets
##from sklearn.preprocessing import StandardScaler
##from sklearn.metrics import adjusted_rand_score, adjusted_mutual_info_score
##
##
### Loading the iris data
##iris = datasets.load_iris()
##X_raw = iris.data    # Data
##y = iris.target  # Target i.e., true clusters
##varNames = iris.feature_names  # variable names
##targetNames = iris.target_names  # names of irises
##nVar = X.shape[1]  # number of features
##
### standardizing the features
##irisNorm = StandardScaler().fit(X_raw)  # learning standardization
##X = irisNorm.transform(X_raw)  # transforming the raw features
##
##
##
### K-means clustering, raw data
##numClus = 3  # number of clusters
##kmRaw = KMeans(n_clusters=numClus)  # defining the clustering object
##kmRaw.fit(X_raw)  # actually fitting the data
##yRaw_clus = kmRaw.labels_   # clustering info resulting from K-means
##
##
### K-means clustering, normalized data
##kmNorm = KMeans(n_clusters=numClus)  # defining the clustering object
##kmNorm.fit(X)  # actually fitting the data
##yNorm_clus = kmNorm.labels_   # clustering info resulting from K-means
##
##
### ARI
##print('ARI (raw)=  %7.4f' % adjusted_rand_score(y, yRaw_clus))
##print('ARI (norm)=  %7.4f' % adjusted_rand_score(y, yNorm_clus))
##
##
### AMI
##print('AMI (raw)=  %7.4f' % adjusted_mutual_info_score(y, yRaw_clus))
##print('AMI (norm)=  %7.4f' % adjusted_mutual_info_score(y, yNorm_clus))
##
