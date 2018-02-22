'''
90. word2vecによる学習
81で作成したコーパスに対してword2vecを適用し，単語ベクトルを学習せよ．
さらに，学習した単語ベクトルの形式を変換し，86-89のプログラムを動かせ．
'''
from gensim.models import Word2Vec
import sys


class Sentences(object):
    def __init__(self, fname):
        self.fname = fname
    def __iter__(self):
        for line in open(self.fname, 'rt', encoding='utf8'):
            yield line.split()

if __name__ == '__main__':
    sents = Sentences(sys.argv[1])
    model = Word2Vec(sents ,window=5, min_count=10)
    model.save(sys.argv[2])
    # no.86: print word vec
    print("United_States vec: {}".format(model['United_States']))
    # no.87: cal sim of two words
    print("Sim of United_States and U.S: {}"\
          .format(model.similarity('United_States', 'U.S')))
    # no.88: sim rank with England
    print("Most similar words with England: {}"\
          .format(model.most_similar(positive=['England'])))
    # no89: sim rank with Spain - Madrid + Athens
    print("Most similar word with Spain - Madrid + Athens: {}"\
          .format(model.most_similar(positive=['Spain', 'Athens'], negative=['Madrid'])))