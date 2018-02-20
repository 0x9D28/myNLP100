'''
43. 名詞を含む文節が動詞を含む文節に係るものを抽出
名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．
ただし，句読点などの記号は出力しないようにせよ．
'''
from no41 import Chunk, load_cabocha
import sys


def search_pos(chunk, pos, bool=True):
    '''Does the chunk contain the POS?
       if bool == True, return True/False
       else return morph s.t. morph.pos == "pos"
    '''
    for morph in chunk.morphs:
        if morph.pos == pos:
            return True if bool else morph
    return False if bool else None


if __name__ == '__main__':
    f = open('../data/neko.txt.cabocha', 'rt', encoding='utf8')
    sents = load_cabocha(f)
    f.close()
    # import pdb; pdb.set_trace()
    for sent in sents:
        sent2 = sent
        for chunk in sent:
            for chunk2 in sent2:
                if chunk.dst == chunk2.idx and search_pos(chunk, "名詞") and search_pos(chunk2, "動詞"):
                    surface = "".join([morph.surface for morph in chunk.morphs if morph.pos != "記号"])
                    surface2 = "".join([morph.surface for morph in chunk2.morphs if morph.pos != "記号"])
                    print("{}\t{}".format(surface, surface2))
                    break
