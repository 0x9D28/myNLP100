'''
75. 素性の重み
73で学習したロジスティック回帰モデルの中で，
重みの高い素性トップ10と，重みの低い素性トップ10を確認せよ．
'''
from sklearn.linear_model import LogisticRegression
from no73 import load_feats
import sys

feats, labels, sents = load_feats(sys.argv[1])
model = LogisticRegression(C=1e5)
model.fit(feats, labels)
with open('data/feats.csv') as f:
    header = f.readline()
header = header.split(",")[2:]
feats_dict = {}
for word, weight in zip(header, model.coef_[0]):
    feats_dict[word] = weight
for i, elem in enumerate(sorted(feats_dict.items(), key=lambda x: x[1])):
    if i > 9:
        break
    print("{}: {}".format(elem[0], elem[1]))
for i, elem in enumerate(sorted(feats_dict.items(), key=lambda x: -x[1])):
    if i > 9:
        break
    print("{}: {}".format(elem[0], elem[1]))
