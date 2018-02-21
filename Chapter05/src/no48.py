'''
48. 名詞から根へのパスの抽出
文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ．
 ただし，構文木上のパスは以下の仕様を満たすものとする．

各文節は（表層形の）形態素列で表現する
パスの開始文節から終了文節に至るまで，各文節の表現を"->"で連結する
「吾輩はここで始めて人間というものを見た」という文（neko.txt.cabochaの8文目）から，
次のような出力が得られるはずである．

吾輩は -> 見た
ここで -> 始めて -> 人間という -> ものを -> 見た
人間という -> ものを -> 見た
ものを -> 見た
'''
from no41 import Chunk, load_cabocha
from no43 import search_pos
import sys


if __name__ == '__main__':
    infile = open('../data/neko.txt.cabocha', 'rt', encoding='utf8')
    sents = load_cabocha(infile)
    infile.close()
    outfile = open('../data/out48.txt', 'wt', encoding='utf8')
    # import pdb; pdb.set_trace()
    for sent in sents:
        sent2 = sent
        for chunk in sent:
            noun_chunk = search_pos(chunk, pos="名詞", fmt='chunk')
            if noun_chunk:
                path_chunks = [noun_chunk]
                for current_chunk in sent2:
                    if path_chunks[-1].dst == current_chunk.idx:
                        path_chunks.append(current_chunk)
                if len(path_chunks) > 1:
                    outfile.write(" -> ".join([node.surface for node in path_chunks])+"\n")

    outfile.close()