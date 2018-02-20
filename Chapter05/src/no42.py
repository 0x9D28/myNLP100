'''
42. 係り元と係り先の文節の表示
係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．
'''
from no41 import Chunk, load_cabocha
import sys

if __name__ == '__main__':
    f = open('../data/neko.txt.cabocha', 'rt', encoding='utf8')
    sents = load_cabocha(f)
    f.close()
    # import pdb; pdb.set_trace()
    print(*sents[8], sep="\n")
    for sent in sents:
        sent2 = sent
        for chunk in sent:
            for chunk2 in sent2:
                if chunk.dst == chunk2.idx:
                    surface = "".join([morph.surface for morph in chunk.morphs if morph.pos != "記号"])
                    surface2 = "".join([morph.surface for morph in chunk2.morphs if morph.pos != "記号"])
                    print("{}\t{}".format(surface, surface2))
                    break
