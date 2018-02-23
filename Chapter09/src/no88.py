'''
88. 類似度の高い単語10件
85で得た単語の意味ベクトルを読み込み，
"England"とコサイン類似度が高い10語と，
その類似度を出力せよ．
'''
import pickle as pkl
import sys
from no85 import SemanticSpace

if __name__ == '__main__':
    with open(sys.argv[1], 'rb') as f:
        model = pkl.load(f)
    print(model.most_similar(positive=['England']))
