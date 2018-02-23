'''
87. 単語の類似度
85で得た単語の意味ベクトルを読み込み，
"United States"と"U.S."のコサイン類似度を計算せよ．
ただし，"U.S."は内部的に"U.S"と表現されていることに注意せよ．
'''
import pickle as pkl
import sys
from no85 import SemanticSpace

if __name__ == '__main__':
    with open(sys.argv[1], 'rb') as f:
        model = pkl.load(f)

    print(model.similarity('United_States', 'U.S'))
