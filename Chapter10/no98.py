'''
98. Ward法によるクラスタリング
96の単語ベクトルに対して，Ward法による階層型クラスタリングを実行せよ．
さらに，クラスタリング結果をデンドログラムとして可視化せよ．
'''
import sys
import pickle as pkl
from scipy.cluster.hierarchy import ward, dendrogram
from matplotlib import pyplot as plt
from collections import OrderedDict

if __name__ == '__main__':
    X = pkl.load(open(sys.argv[1], 'rb'))
    X = OrderedDict(X)
    Z = ward([x for x in X.values()])
    plt.figure(figsize=(25, 10))
    plt.title('Hierarchical Clustering Dendrogram')
    plt.xlabel('countries')
    plt.ylabel('distance')
    dendrogram(Z,
               leaf_rotation=90.,
               leaf_font_size=8.,
               labels=[country for country in X.keys()])
    plt.savefig(sys.argv[2])
    plt.close()
