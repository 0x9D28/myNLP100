'''
85. 主成分分析による次元圧縮
84で得られた単語文脈行列に対して，主成分分析を適用し，
単語の意味ベクトルを300次元に圧縮せよ．
'''
import pickle as pkl
import sys
from sklearn.decomposition import TruncatedSVD as TSVD
import numpy as np
import os

if __name__ == '__main__':
    # SVD
    with open(sys.argv[1], 'rb') as f:
        X = pkl.load(f)
    svd = TSVD(n_components=300)
    svd.fit(X)
    print(svd.components_)

    # load idx
    with open(sys.argv[2], 'rb') as f:
        idx = pkl.load(f)

    # attach labels to rows of transposed X
    # for calling vector by X[term]
    X = np.transpose(svd.components_)
    X_dic = {}
    for term, i in idx.items():
        X_dic[term] = X[i]

    with open(sys.argv[3], 'wb') as f:
        pkl.dump(X_dic, f)
    
    
