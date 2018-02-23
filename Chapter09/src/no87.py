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
    with open(sys.argv[1], 'rb') as f:
        X = pkl.load(f)
    
    sim = cos_sim(X['United_States'], X['U.S'])
    print(sim)
