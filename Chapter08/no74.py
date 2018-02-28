'''
74. 予測
73で学習したロジスティック回帰モデルを用い，与えられた文の極性ラベル
（正例なら"+1"，負例なら"-1"）と，その予測確率を計算するプログラムを実装せよ．
'''
import random
from sklearn.linear_model import LogisticRegression
from no73 import load_feats
import sys

feats, labels, sents = load_feats(sys.argv[1])
model = LogisticRegression(C=1e5)
model.fit(feats, labels)
print(model)
row_nums = [random.randint(0, len(labels)-1) for i in range(100)]
test_feats, test_labels, test_sents = [], [], []
for i in row_nums:
    test_feats.append(feats[i])
    test_labels.append(labels[i])
    test_sents.append(sents[i])
predicts = model.predict(test_feats)
probs = model.predict_proba(test_feats)
for l, s, pred, prob in zip(test_labels, test_sents, predicts, probs):
    print("'{}'\n \tlabel: {}, predict: {}, probability: {}"
          .format(s, l, pred, prob))
