'''
78. 5分割交差検定
76-77の実験では，学習に用いた事例を評価にも用いたため，正当な評価とは言えない．
すなわち，分類器が訓練事例を丸暗記する際の性能を評価しており，モデルの汎化性能を測定していない．
そこで，5分割交差検定により，極性分類の正解率，適合率，再現率，F1スコアを求めよ．

argv[1]: [INPUT]  features csv
'''


def split_seq(seq, K=5):
    split_seq = [[] for i in range(K)]
    for i in range(len(seq)):
        split_seq[i % K].append(seq[i])
    return split_seq


def get_train(split_seq, test_idx):
    train_data = []
    for i, seq in enumerate(split_seq):
        if i == test_idx:
            continue
        train_data += seq
    return train_data


if __name__ == '__main__':
    import sys
    from no73 import load_feats
    from sklearn.linear_model import LogisticRegression
    from no77 import get_metrics
    fname = sys.argv[1]
    K = 5
    feats, labels, _ = load_feats(fname)
    split_feats = split_seq(feats, 5)
    split_labels = split_seq(labels, 5)
    metrics_list = []
    # import pdb; pdb.set_trace()
    for i in range(5):
        model = LogisticRegression(C=1e5)
        model.fit(get_train(split_feats, i), get_train(split_labels, i))
        predicts = model.predict(split_feats[i])
        metrics_list.append(get_metrics(split_labels[i], predicts))
    accuracy = sum([metric[0] for metric in metrics_list]) / K
    precision = sum([metric[1] for metric in metrics_list]) / K
    recall = sum([metric[2] for metric in metrics_list]) / K
    Fmeasure = sum([metric[3] for metric in metrics_list]) / K
    print("accuracy:  {}".format(accuracy))
    print("precision: {}".format(precision))
    print("recall:    {}".format(recall))
    print("F-measure: {}".format(Fmeasure))
