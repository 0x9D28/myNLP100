'''
92. アナロジーデータへの適用
91で作成した評価データの各事例に対して，
vec(2列目の単語) - vec(1列目の単語) + vec(3列目の単語)を計算し，
そのベクトルと類似度が最も高い単語と，その類似度を求めよ．
求めた単語と類似度は，各事例の末尾に追記せよ．
このプログラムを85で作成した単語ベクトル，
90で作成した単語ベクトルに対して適用せよ．

$ python3 no92.py [input analogy set] []
'''
import sys
from gensim.models import Word2Vec
import pickle as pkl
sys.path.append('../Chapter09/src')
from no85 import SemanticSpace

if __name__ == '__main__':
    infile = open(sys.argv[1], 'rt', encoding='utf8')
    handmade_model = pkl.load(open(sys.argv[2], 'rb'))
    word2vec_model = Word2Vec.load(sys.argv[3])
    outfile = open(sys.argv[4], 'wt', encoding='utf8')
    i = 0
    for line in infile:
        words = line.rstrip('\n').split()
        try:
            sim_term1 = handmade_model.most_similar(positive=[words[1], words[2]],
                                                    negative=[words[0]], topn=1)[0]
            sim_term2 = word2vec_model.most_similar(positive=[words[1], words[2]],
                                                    negative=[words[0]], topn=1)[0]
        except KeyError as e:
            i += 1
        line = "{} {}:{} {}:{}\n"\
            .format(line.rstrip('\n'), sim_term1[0], sim_term1[1], sim_term2[0], sim_term2[1])
        print(line.rstrip('\n'))
        outfile.write(line)
    print("ignored {} lines".format(i))
    infile.close()
    outfile.close()