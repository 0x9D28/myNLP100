'''
35. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．

argv[1]: neko.txt.mecab
'''
from no30 import read_morphemes
import sys

sentences = read_morphemes(sys.argv[1])
for sentence in sentences:
    seq_noun = []
    for morpheme in sentence:
        # seq_noun contains sequential nouns
        if morpheme["pos"] == "名詞":
            seq_noun.append(morpheme)
        else:
            if len(seq_noun) > 1:
                print(*[m["surface"] for m in seq_noun], sep="")
            seq_noun = []
