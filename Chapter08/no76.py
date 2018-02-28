'''
76. ラベル付け
学習データに対してロジスティック回帰モデルを適用し，
正解のラベル，予測されたラベル，予測確率をタブ区切り形式で出力せよ．

argv[1]: [INPUT]  features csv
argv[2]: [OUTPUT] text file (label-predict-probability)
'''
from sklearn.linear_model import LogisticRegression
from no73 import load_feats
import sys

if __name__ == '__main__':
    feats, labels, sents = load_feats(sys.argv[1])
    model = LogisticRegression(C=1e5)
    model.fit(feats, labels)
    print(model)
    predicts = model.predict(feats)
    probs = model.predict_proba(feats)
    f = open(sys.argv[2], 'wt')
    for label, pred, prob in zip(labels, predicts, probs):
        neg_prob, pos_prob = prob
        prob = neg_prob if neg_prob > pos_prob else pos_prob
        f.write("{}\t{}\t{}\n".format(label, pred, prob))
    f.close()
