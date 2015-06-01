import numpy as np
from scipy.cluster.vq import kmeans
from scipy.spatial.distance import cdist,pdist
import time
from sklearn import datasets
from sklearn.decomposition import RandomizedPCA
from matplotlib import pyplot as plt
from matplotlib import cm

client = Client()
v = client[:]
##### data #####
# load digits dataset
data = datasets.load_digits()
t = data['target']

# perform PCA dimensionality reduction
pca = RandomizedPCA(n_components=2).fit(data['data'])
X = pca.transform(data['data'])

##### cluster data into K=1..20 clusters #####
K_MAX = 20
# unparallel_time
t0=time.time()
KK = range(1,K_MAX+1)
KM = [kmeans(X,k) for k in KK]
centroids = [cent for (cent,var) in KM]
D_k = [cdist(X, cent, 'euclidean') for cent in centroids]
dist = [np.min(D,axis=1) for D in D_k]

tot_withinss = [sum(d**2) for d in dist]  # Total within-cluster sum of squares
Unparallel_time=time.time()-t0
print Unparallel_time


# parallel_time
def test_k_means(tup):
    from scipy.cluster.vq import kmeans
    from scipy.spatial.distance import cdist,pdist
    import numpy as np
    X = arg[0]
    k = arg[1]
    KM = kmeans(X, k)
    centroid = KM[0]
    D = cdist(X, centroid, 'euclidean')
    dist = np.min(D,axis=1)
    avgWithinSS = sum(dist**2)
    return avgWithinSS
t0 =time.time()
KK =range(1,K_MAX + 1)
arg=[(X,i) for i in KK]
r=v.map(kmeansExt, arg)
res=r.get()
Parallel_time=time.time()-t0
print Parallel_time


##### plots #####
kIdx = 9        # K=10
clr = cm.spectral( np.linspace(0,1,10) ).tolist()
mrk = 'os^p<dvh8>+x.'

# elbow curve
fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(KK, betweenss/totss*100, 'b*-')
ax.plot(KK[kIdx], betweenss[kIdx]/totss*100, marker='o', markersize=12, 
    markeredgewidth=2, markeredgecolor='r', markerfacecolor='None')
ax.set_ylim((0,100))
plt.grid(True)
plt.xlabel('Number of clusters')
plt.ylabel('Percentage of variance explained (%)')
plt.title('Elbow for KMeans clustering')

