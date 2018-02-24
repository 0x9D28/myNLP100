'''
97. k-meansクラスタリング
96の単語ベクトルに対して，k-meansクラスタリングをクラスタ数(k=5)として実行せよ．
'''
from sklearn.cluster import KMeans
import pickle as pkl
import sys
from collections import OrderedDict, defaultdict

if __name__ == '__main__':
    X = pkl.load(open(sys.argv[1], 'rb'))
    X = OrderedDict(X)
    kmeans = KMeans(n_clusters=5).fit([x for x in X.values()])
    combs = defaultdict(list)
    for country_name, cluster_number in zip(X.keys(), kmeans.labels_):
        combs[cluster_number].append(country_name)
    for k, v in sorted(combs.items()):
        print("{}: {}".format(k, v))

