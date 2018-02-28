'''
52. ステミング
51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，
単語と語幹をタブ区切り形式で出力せよ．
Pythonでは，Porterのステミングアルゴリズムの実装として
stemmingモジュールを利用するとよい．
'''
import snowballstemmer


def WordTabLemma(fin, fout):
    '''Convert one word per line format to word-tab-lemma per line format.'''
    stemmer = snowballstemmer.stemmer('english')
    with open(fin, 'rt') as fi, open(fout, 'wt') as fo:
        for word in fi:
            word = word.strip()
            fo.write("{}\t{}\n".format(word, stemmer.stemWord(word)))


if __name__ == '__main__':
    fin = 'nlp51.txt'
    fout = 'nlp52.txt'
    WordTabLemma(fin, fout)
