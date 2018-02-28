'''
85. 主成分分析による次元圧縮
84で得られた単語文脈行列に対して，主成分分析を適用し，
単語の意味ベクトルを300次元に圧縮せよ．
'''
import pickle as pkl
import sys
from sklearn.decomposition import TruncatedSVD as TSVD
import numpy as np
from numpy import linalg as LA


class SemanticSpace(object):
    def __init__(self, labeled_matrix):
        self.matrix = labeled_matrix

    def cos_sim(self, vec1, vec2):
        sim = np.dot(vec1, vec2) / (LA.norm(vec1) * LA.norm(vec2))
        return sim if sim > 0 else 0

    def similarity(self, term1, term2):
        return self.cos_sim(self.matrix[term1], self.matrix[term2])

    def most_similar(self, positive=[], negative=[], topn=10):
        sim_dic = {}
        rslt = []
        for val in self.matrix.values():
            Ndim = val.shape[0]
            break
        vec_sum = np.zeros(Ndim)
        for term in positive:
            vec_sum += self.matrix[term]
        for term in negative:
            vec_sum -= self.matrix[term]
        for term, vec in self.matrix.items():
            sim_dic[term] = self.cos_sim(vec_sum, vec)
        for i, t_s in enumerate(sorted(sim_dic.items(),
                                       key=lambda x: -x[1]), start=1):
            term, sim = t_s
            rslt.append((term, sim))
            if i >= topn:
                break
        return rslt

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
        pkl.dump(SemanticSpace(X_dic), f)
    
    
