'''
33. サ変名詞
サ変接続の名詞をすべて抽出せよ．

argv[1]: neko.txt.mecab
'''
from no30 import read_morphemes
import sys

sentences = read_morphemes(sys.argv[1])
for sentence in sentences:
    for morpheme in sentence:
        if morpheme["pos1"] == "サ変接続":
            print(morpheme["surface"])
