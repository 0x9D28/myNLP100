'''
34. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ．

argv[1]: neko.txt.mecab
'''
from no30 import read_morphemes
import sys

sentences = read_morphemes(sys.argv[1])
for sentence in sentences:
    tri = []
    for morpheme in sentence:
        # tri contain three words which are noun or の
        if morpheme["pos"] == "名詞" or morpheme["surface"] == "の":
            tri.append(morpheme)
            # if tri is noun-の-noun sequence
            if len(tri) == 3 and tri[0]["pos"] == "名詞" \
               and tri[1]["surface"] == "の" and tri[2]["pos"] == "名詞":
                print(*[tri[i]["surface"] for i in range(3)], sep="")
        else:
            tri = []
