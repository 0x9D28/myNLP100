'''
96. 国名に関するベクトルの抽出
word2vecの学習結果から，国名に関するベクトルのみを抜き出せ．
'''
import sys
from gensim.models import Word2Vec
import pickle as pkl

if __name__ == '__main__':
    countries_name = [country for country in open(sys.argv[1], 'rt', encoding='utf8')]
    model = Word2Vec.load(sys.argv[2])
    countries_vec = {}
    ignored = []
    for country in countries_name:
        country = country.rstrip('\n').replace(' ', '_')
        try:
            countries_vec[country] = model[country]
        except KeyError:
            ignored.append(country)
    pkl.dump(countries_vec, open(sys.argv[3], 'wb'))
    print("---- not found ----")
    print(*ignored, sep='\n')