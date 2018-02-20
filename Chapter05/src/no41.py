'''
41. 係り受け解析結果の読み込み（文節・係り受け）
40に加えて，文節を表すクラスChunkを実装せよ．
このクラスは
・形態素（Morphオブジェクト）のリスト（morphs），
・係り先文節インデックス番号（dst），
・係り元文節インデックス番号のリスト（srcs）
をメンバ変数に持つこととする．
さらに，入力テキストのCaboChaの解析結果を読み込み，
１文をChunkオブジェクトのリストとして表現し，
8文目の文節の文字列と係り先を表示せよ．
第5章の残りの問題では，ここで作ったプログラムを活用せよ．
'''
import sys
from no40 import Morph
import re

class Chunk(object):
    def __init__(self, chunk_lines, headers_lines):
        header = chunk_lines[0].split()
        self.idx = int(header[1])
        self.dst = int(header[2].replace("D", ""))
        srcs = []
        # import pdb; pdb.set_trace()
        for header_line in headers_lines:
            header_line = header_line.split()
            if self.idx == int(header_line[2].replace("D", "")):
                srcs.append(int(header_line[1]))
        self.srcs = srcs
        self.morphs = [Morph(line) for line in chunk_lines[1:]]
        self.surface = "".join([morph.surface for morph in self.morphs])
    def __repr__(self):
        surfaces = "".join([morph.surface for morph in self.morphs])
        srcs = ",".join([str(src) for src in self.srcs]) if self.srcs else "nan"
        return "idx: {}, srcs: ({}), dst: {}, surface: {}"\
               .format(self.idx, srcs, self.dst, surfaces)


def load_cabocha(lines):
    sents, sent, chunk_lines, headers = [], [], [], []
    for line in lines:
        if line[0] == "*":
            if chunk_lines:
                sent.append(Chunk(chunk_lines, headers))
            headers.append(line)
            chunk_lines = [line]
        elif line.rstrip("\n") == "EOS":
            if chunk_lines:
                sent.append(Chunk(chunk_lines, headers))
                sents.append(sent)
            sent = []
            chunk_lines = []
            headers = []
        else:
            chunk_lines.append(line)
    return sents


if __name__ == '__main__':
    f = open(sys.argv[1], 'rt')
    sents = load_cabocha(f)
    f.close()
    # import pdb; pdb.set_trace()
    print(*sents[8], sep="\n")
