'''
40. 係り受け解析結果の読み込み（形態素）形態素を表すクラスMorphを実装せよ．
このクラスは表層形（surface），基本形（base），品詞（pos），
品詞細分類1（pos1）をメンバ変数に持つこととする．
さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，
各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．
'''
import sys


class Morph(object):
    def __init__(self, line):
        self.surface, info = line.split("\t")
        info = info.split(",")
        self.base = info[6]
        self.pos = info[0]
        self.pos1 = info[1]
    def __repr__(self):
        return "surface:{}, base:{}, pos:{}, pos1:{}"\
               .format(self.surface, self.base, self.pos, self.pos1)

def load_cabocha(lines):
    sents, sent = [], []
    for line in lines:
        if line[0] == "*":
            continue
        elif line[:3] == "EOS":
            sents.append(sent)
            sent = []
        else:
            sent.append(Morph(line))
    return sents


if __name__ == '__main__':
    f = open(sys.argv[1], 'rt')
    sents = load_cabocha(f)
    f.close()
    print(*sents[2], sep="\n")
