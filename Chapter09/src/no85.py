'''
85. 主成分分析による次元圧縮
84で得られた単語文脈行列に対して，主成分分析を適用し，
単語の意味ベクトルを300次元に圧縮せよ．
'''
import pickle as pkl
import sys
from sklearn.decomposition import TruncatedSVD as TSVD
import numpy as np

if __name__ == '__main__':
    with open(sys.argv[1], 'rb') as f:
        X = pkl.load(f)
    svd = TSVD(n_components=300)
    svd.fit(X)
    print(svd.components_)
    with open(sys.argv[2], 'wb') as f:
        pkl.dump(np.transpose(svd.components_), f)
    
    
