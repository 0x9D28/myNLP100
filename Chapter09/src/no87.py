'''
87. 単語の類似度
85で得た単語の意味ベクトルを読み込み，
"United States"と"U.S."のコサイン類似度を計算せよ．
ただし，"U.S."は内部的に"U.S"と表現されていることに注意せよ．
'''
import pickle as pkl
import sys
import os
from numpy import linalg as LA
import numpy as np

def cos_sim(vec1, vec2):
    return np.dot(vec1, vec2) / (LA.norm(vec1) * LA.norm(vec2))


if __name__ == '__main__':
    indir = sys.argv[1]
    with open(os.path.join(indir, 'svd-X.pkl'), 'rb') as f:
        X = pkl.load(f)
    with open(os.path.join(indir, 'idx.pkl'), 'rb') as f:
        idx = pkl.load(f)
    
    sim = cos_sim(X[idx['United_States']], X[idx['U.S']])
    print(sim)
