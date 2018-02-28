'''
73. 学習
72で抽出した素性を用いて，ロジスティック回帰モデルを学習せよ．

argv[1]: [INPUT]  features csv
'''
from sklearn.linear_model import LogisticRegression


def load_feats(fname):
    f = open(fname, 'r')
    feats = []
    labels = []
    sents = []
    for line in f:
        line = line.split(",")
        if line[0] == "LABEL":
            continue
        sents.append(line[1])
        labels.append(int(line[0]))
        feats.append([int(v) for v in line[2:]])
    f.close()
    return feats, labels, sents


if __name__ == '__main__':
    import sys
    fname = sys.argv[1]
    data = load_feats(fname)
    model = LogisticRegression(C=1e5)
    model.fit(data[0], data[1])
    print(model)
