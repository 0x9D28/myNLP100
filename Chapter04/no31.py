'''
31. 動詞
動詞の表層形をすべて抽出せよ．

argv[1]: neko.txt.mecab
'''
from no30 import read_morphemes
import sys

sentences = read_morphemes(sys.argv[1])
for sentence in sentences:
    for morpheme in sentence:
        if morpheme["pos"] == "動詞":
            print(morpheme["surface"])
