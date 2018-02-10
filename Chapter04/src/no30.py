'''
30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は表層形（surface），基本形（base），品詞（pos），
品詞細分類1（pos1）をキーとするマッピング型に格納し，1文を形態素（マッピング型）の
リストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．
'''


def read_morphemes(infile):
    '''
    Load a file containing MeCab analysis results.
    e.g., an analysis result is as a follow
    吾輩	名詞,代名詞,一般,*,*,*,吾輩,ワガハイ,ワガハイ

    for each sentence:
        yield [{morpheme data}, {morpheme data}, ...]
    '''
    f = open(infile, 'r')
    sentence = []
    for line in f:
        line = line.rstrip('\n').replace("\t", ",").split(",")
        if line == ["EOS"]:
            if sentence:
                yield sentence
            sentence = []
        else:
            sentence.append({
                "surface": line[0],
                "base": line[7],
                "pos": line[1],
                "pos1": line[2],
                })
    f.close()


if __name__ == '__main__':
    '''
    argv[1]: mecab.txt.mecab
    '''
    import sys
    morphemes = read_morphemes(sys.argv[1])
    for sentence in morphemes:
        print(sentence)
