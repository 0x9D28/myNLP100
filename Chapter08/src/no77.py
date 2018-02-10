'''
77. 正解率の計測
76の出力を受け取り，予測の正解率，正例に関する適合率，
再現率，F1スコアを求めるプログラムを作成せよ．

argv[1]: [INPUT]  text file (label-predict-probability)
'''


def get_metrics(labels, predicts):
    tp, tn, fp, fn = 0, 0, 0, 0
    for label, predict in zip(labels, predicts):
        if label == predict:
            if predict == 1:
                tp += 1
            else:
                tn += 1
        else:
            if predict == 1:
                fp += 1
            else:
                fn += 1
    accuracy = (tp + tn) / (tp + tn + fp + fn)
    try:
        precision = tp / (tp + fp)
    except ZeroDivisionError:
        precision = 1.0
    recall = tp / (tp + fn)
    Fmeasure = 2 * precision * recall / (precision + recall)
    return accuracy, precision, recall, Fmeasure


if __name__ == '__main__':
    import sys
    f = open(sys.argv[1])
    labels, predicts = [], []
    for line in f:
        line = line.split("\t")
        labels.append(int(line[0]))
        predicts.append(int(line[1]))
    f.close()
    accuracy, precision, recall, Fmeasure = get_metrics(labels, predicts)
    print("accuracy:  {}".format(accuracy))
    print("precision: {}".format(precision))
    print("recall:    {}".format(recall))
    print("F-measure: {}".format(Fmeasure))
