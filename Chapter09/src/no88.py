'''
88. 類似度の高い単語10件
85で得た単語の意味ベクトルを読み込み，
"England"とコサイン類似度が高い10語と，
その類似度を出力せよ．
'''
import pickle as pkl
import sys
import os
from numpy import linalg as LA
import numpy as np


def cos_sim(vec1, vec2):
    sim = np.dot(vec1, vec2) / (LA.norm(vec1) * LA.norm(vec2))
    if sim > 0:
        return sim
    else:
        return 0

if __name__ == '__main__':
    with open(sys.argv[1], 'rb') as f:
        X = pkl.load(f)
    rslt_dic = {}
    england_vec = X['England']
    for term, vec in X.items():
        rslt_dic[term] = cos_sim(england_vec, vec)
    
    for i, term_sim in enumerate(sorted(rslt_dic.items(), key=lambda x: -x[1]),
                            start=0):
        term, sim = term_sim
        if term == 'England':
            continue
        print("{}. {}: {}".format(i, term, sim))
        if i >= 10:
            break
        
