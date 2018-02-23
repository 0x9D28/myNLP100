'''
89. 加法構成性によるアナロジー
85で得た単語の意味ベクトルを読み込み，
vec("Spain") - vec("Madrid") + vec("Athens")を計算し，
そのベクトルと類似度の高い10語とその類似度を出力せよ．
'''
import pickle as pkl
import sys
from no85 import SemanticSpace

if __name__ == '__main__':
    with open(sys.argv[1], 'rb') as f:
        model = pkl.load(f)

    print(model.most_similar(positive=['Spain', 'Athens'], negative=['Madrid'], topn=10))

        
