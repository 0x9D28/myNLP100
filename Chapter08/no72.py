'''
72. 素性抽出
極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．
素性としては，レビューからストップワードを除去し，
各単語をステミング処理したものが最低限のベースラインとなるであろう．

argv[1]: sentiment.txt
argv[2]: number of features
argv[3]: features csv file
'''
import snowballstemmer
from no71 import isstopwords
from collections import Counter


def write_feats(infile, outfile, N=5000):
    stemmer = snowballstemmer.stemmer('english')
    feats_list = _extract_features(infile, N)
    with open(infile, 'r') as inf, open(outfile, 'w') as outf:
        # write header
        outf.write("LABEL,SENTENCE,"
                   + ",".join([str(feat) for feat in feats_list])+"\n")
        for line in inf:
            # write pos/neg, raw sent(except comma), feats cnt for each line
            feats_cnt = [0 for i in range(len(feats_list))]
            line = line.split()
            for word in line[1:]:
                word = stemmer.stemWord(word)
                if word in feats_list:
                    feats_cnt[feats_list.index(word)] += 1
            sentence = " ".join(line[1:]).replace(",", "")
            outf.write(line[0]+","+sentence+","
                       + ",".join([str(feat) for feat in feats_cnt])+"\n")


def _extract_features(infile, N=5000):
    '''return a word-list as feats'''
    stemmer = snowballstemmer.stemmer('english')
    feats_set = Counter()
    # collect all features to generatete feature-index
    with open(infile, 'r') as f:
        for line in f:
            line = line.split()
            feats_set.update([word for word in stemmer.stemWords(line[1:])
                              if not isstopwords(word)])
    # generate each line features
    # features: top N freq words
    feats_list = []
    for i, wf in enumerate(sorted(feats_set.items(), key=lambda x: -x[1])):
        if i >= N:
            break
        feats_list.append(wf[0])
    return feats_list


if __name__ == '__main__':
    import sys
    write_feats(infile=sys.argv[1], outfile=sys.argv[3], N=int(sys.argv[2]))
