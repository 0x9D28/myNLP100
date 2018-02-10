'''
36. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．

argv[1]: neko.txt.mecab
'''
from no30 import read_morphemes
from collections import Counter


def get_flat_data(key, sents):
    for sent in sents:
        for morph in sent:
            yield morph[key]


if __name__ == "__main__":
    import sys
    sentences = read_morphemes(sys.argv[1])
    cnt = Counter(get_flat_data(key="base", sents=sentences))
    for k, v in sorted(cnt.items(), key=lambda x: -x[1]):
        print("{}: {}".format(k, v))
