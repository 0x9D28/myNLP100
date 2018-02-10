'''
71. ストップワード
英語のストップワードのリスト（ストップリスト）を適当に作成せよ．
さらに，引数に与えられた単語（文字列）がストップリストに含まれている場合は真，
それ以外は偽を返す関数を実装せよ．さらに，その関数に対するテストを記述せよ．

argv[1]: [INPUT]  sentence
'''


def isstopwords(word):
    from nltk.corpus import stopwords
    marks = ". , : ; @ / \ # $ % ( ) [ ] \{ \} \" \" < >".split()
    stops = stopwords.words('english')
    return True if word in marks+stops else False


if __name__ == '__main__':
    import sys
    for word in sys.argv[1].split():
        if isstopwords(word.lower()):
            print("'{}' is stopword".format(word))
        else:
            print("'{}' is not stopword".format(word))
