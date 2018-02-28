'''
51. 単語の切り出し
空白を単語の区切りとみなし，50の出力を入力として受け取り，
1行1単語の形式で出力せよ．ただし，文の終端では空行を出力せよ．
'''
import re


def SplitWords(fin, fout):
    '''Convert one sentence per line format to one word per line format.'''
    with open(fin, 'rt') as fi, open(fout, 'wt') as fo:
        for sentence in fi:
            # delete end mark
            sentence = re.sub(r'[\.;:\?\!]$', r' ', sentence)
            for word in sentence.split(" "):
                # delete some marks for stemming
                word = re.sub(r'[\(\),\"\']', r'', word)
                if word != "\n":
                    fo.write(word+"\n")


if __name__ == '__main__':
    fin = 'nlp50.txt'
    fout = 'nlp51.txt'
    SplitWords(fin, fout)
