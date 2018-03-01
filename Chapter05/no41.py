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


class Chunk(object):
    def __init__(self, chunk_lines, headers_lines):
        """
        Attributes:
            idx (int): index of the chunk in the sentence
            dst (int): index of the distribution chunk in the sentence
            srcs (list): list of indexes of the source chunks in the sentence
            morphs (list): list of morph class objects
            surface (str): surface of the chunk
        """
        header = chunk_lines[0].split()
        self.idx = int(header[1])
        self.dst = int(header[2].replace("D", ""))
        srcs = []
        for header_line in headers_lines:
            header_line = header_line.split()
            if self.idx == int(header_line[2].replace("D", "")):
                srcs.append(int(header_line[1]))
        self.srcs = srcs
        self.morphs = [Morph(line) for line in chunk_lines[1:]]
        self.surface = "".join([morph.surface for morph in self.morphs
                                if morph.pos != '記号'])

    def __repr__(self):
        surfaces = "".join([morph.surface for morph in self.morphs])
        srcs = ",".join([str(src) for src in self.srcs]) if self.srcs else "nan"
        return "idx: {}, srcs: ({}), dst: {}, surface: {}"\
               .format(self.idx, srcs, self.dst, surfaces)


def load_cabocha(lines):
    sent, chunk_lines, headers = [], [], []
    for line in lines:
        if line[0] == "*":
            if chunk_lines:
                sent.append(Chunk(chunk_lines, headers))
            headers.append(line)
            chunk_lines = [line]
        elif line.rstrip("\n") == "EOS":
            if chunk_lines:
                sent.append(Chunk(chunk_lines, headers))
                yield sent
            sent = []
            chunk_lines = []
            headers = []
        else:
            chunk_lines.append(line)


if __name__ == '__main__':
    f = open(sys.argv[1], 'rt')
    sents = load_cabocha(f)
    for i, sent in enumerate(sents, start=1):
        if i == 8:
            print(sent)
            break
    f.close()
