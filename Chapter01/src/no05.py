'''
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
この関数を用い，"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
'''


def Ngram(seq, N=2):
    return [seq[i:i+N] for i in range(len(seq)-(N-1))]


if __name__ == '__main__':
    string = "I am an NLPer"
    word_bigram = Ngram(string.split())
    char_bigram = Ngram(string)

    print(word_bigram)
    print(char_bigram)
