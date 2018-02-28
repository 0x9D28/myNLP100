'''
94. WordSimilarity-353での類似度計算
The WordSimilarity-353 Test Collectionの評価データを入力とし，
1列目と2列目の単語の類似度を計算し，各行の末尾に類似度の値を追加するプログラムを作成せよ．
このプログラムを85で作成した単語ベクトル，90で作成した単語ベクトルに対して適用せよ．
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
    ignore = 0
    for i, line in enumerate(infile):
        if i == 0:
            outfile.write(line.rstrip('\n') + ",HandMade,Word2Vec\n")
            continue
        words = line.rstrip('\n').split(',')
        try:
            sim_term1 = handmade_model.similarity(words[0], words[1])
            sim_term2 = word2vec_model.similarity(words[0], words[1])
        except KeyError as e:
            ignore += 1
        line = "{},{},{}\n"\
            .format(line.rstrip('\n'), sim_term1, sim_term2)
        print(line.rstrip('\n'))
        outfile.write(line)
    print("ignored {} lines".format(ignore))
    infile.close()
    outfile.close()