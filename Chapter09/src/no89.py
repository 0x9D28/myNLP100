'''
89. 加法構成性によるアナロジー
85で得た単語の意味ベクトルを読み込み，
vec("Spain") - vec("Madrid") + vec("Athens")を計算し，
そのベクトルと類似度の高い10語とその類似度を出力せよ．
'''
import pickle as pkl
import sys
import os
from numpy import linalg as LA
import numpy as np


def cos_sim(vec1, vec2):
    sim = np.dot(vec1, vec2) / (LA.norm(vec1) * LA.norm(vec2))
    return sim if sim > 0 else 0


if __name__ == '__main__':
    indir = sys.argv[1]
    with open(os.path.join(indir, 'svd-X.pkl'), 'rb') as f:
        X = pkl.load(f)
    with open(os.path.join(indir, 'idx.pkl'), 'rb') as f:
        idx = pkl.load(f)
    
    rslt_dic = {}
    formula_vec = X[idx["Spain"]] - X[idx["Madrid"]] + X[idx["Athens"]]
    for term, idx in idx.items():
        rslt_dic[term] = cos_sim(formula_vec, X[idx])
    
    for i, t_s in enumerate(sorted(rslt_dic.items(), key=lambda x: -x[1]), 
                            start=1):
        term, sim = t_s
        print("{}. {}: {}".format(i, term, sim))
        if i >= 10:
            break
        
