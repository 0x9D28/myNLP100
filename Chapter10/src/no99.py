'''
99. t-SNEによる可視化
96の単語ベクトルに対して，ベクトル空間をt-SNEで可視化せよ．
'''
import sys
import pickle as pkl
from matplotlib import pyplot as plt
from collections import OrderedDict
from sklearn.manifold import TSNE

if __name__ == '__main__':
    X = pkl.load(open(sys.argv[1], 'rb'))
    X = OrderedDict(X)
    X_embedded = TSNE().fit_transform([x for x in X.values()])
    x = [point[0] for point in X_embedded]
    y = [point[1] for point in X_embedded]
    plt.scatter(x, y)
    plt.title('visualization of semantic space')
    '''
    for i, label in enumerate([country for country in X.keys()]):
        plt.annotate(label, (x[i], y[i]))
    '''
    plt.savefig(sys.argv[2])
    plt.close()
