'''
779. 適合率-再現率グラフの描画
ロジスティック回帰モデルの分類の閾値を変化させることで，適合率-再現率グラフを描画せよ．

argv[1]: [INPUT]  features csv
argv[2]: [OUTPUT] precision-recalll graph file
'''


def prob2bin(probs, threshold):
    predicts = []
    for prob in probs:
        neg, pos = prob
        if pos > threshold:
            predicts.append(1)
        else:
            predicts.append(-1)
    return predicts


if __name__ == '__main__':
    from no73 import load_feats
    from no77 import get_metrics
    from no78 import split_seq, get_train
    from sklearn.linear_model import LogisticRegression
    import matplotlib.pyplot as plt
    import sys
    fname = sys.argv[1]
    K = 5
    feats, labels, _ = load_feats(fname)
    split_feats = split_seq(feats, K)
    split_labels = split_seq(labels, K)

    probs_list = []
    for i in range(K):
        model = LogisticRegression(C=1e5)
        model.fit(get_train(split_feats, i), get_train(split_labels, i))
        probs = model.predict_proba(split_feats[i])
        probs_list.append(probs)
    threshold_list = []
    precision_list = []
    recall_list = []
    for threshold in range(101):
        threshold /= 100
        metrics_list = []
        # import pdb; pdb.set_trace()
        for i in range(K):
            predicts = prob2bin(probs_list[i], threshold)
            metrics_list.append(get_metrics(split_labels[i], predicts))
        precision = sum([metric[1] for metric in metrics_list]) / K
        recall = sum([metric[2] for metric in metrics_list]) / K
        threshold_list.append(threshold)
        precision_list.append(precision)
        recall_list.append(recall)
    plt.plot(recall_list, precision_list)
    plt.xlabel("recall")
    plt.ylabel("precision")
    plt.savefig(sys.argv[2])
    plt.close()
