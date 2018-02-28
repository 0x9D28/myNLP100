'''
46. 動詞の格フレーム情報の抽出
45のプログラムを改変し，述語と格パターンに続けて項
（述語に係っている文節そのもの）をタブ区切り形式で出力せよ．
45の仕様に加えて，以下の仕様を満たすようにせよ．
・項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
・述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる

「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える．
この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，
「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．
始める  で      ここで
見る    は を   吾輩は ものを
'''

from no41 import Chunk, load_cabocha
from no43 import search_pos
import sys


if __name__ == '__main__':
    infile = open(sys.argv[1], 'rt')
    sents = load_cabocha(infile)
    infile.close()
    outfile = open(sys.argv[2], 'wt')
    # import pdb; pdb.set_trace()
    for sent in sents:
        sent2 = sent
        for chunk in sent:
            predicate = search_pos(chunk, "動詞", bool=False)
            if predicate:
                particles = []
                chunk2s = []
                for chunk2 in sent2:
                    particle = search_pos(chunk2, "助詞", bool=False)
                    if particle and chunk2.dst == chunk.idx:
                        particles.append(particle)
                        chunk2s.append(chunk2)
                if particles:
                    particles = " ".join([particle.base for particle in particles])
                    arguments = " ".join([c.surface for c in chunk2s])
                    outfile.write("{}\t{}\t{}\n".format(predicate.base, particles, arguments))
    outfile.close()