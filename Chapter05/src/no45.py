'''
45. 動詞の格パターンの抽出
今回用いている文章をコーパスと見なし，日本語の述語が取りうる格を調査したい．
 動詞を述語，動詞に係っている文節の助詞を格と考え，述語と格をタブ区切り形式で出力せよ．
 ただし，出力は以下の仕様を満たすようにせよ．
・動詞を含む文節において，最左の動詞の基本形を述語とする
・述語に係る助詞を格とする
・述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる

「吾輩はここで始めて人間というものを見た」という例文（neko.txt.cabochaの8文目）を考える．
この文は「始める」と「見る」の２つの動詞を含み，「始める」に係る文節は「ここで」，
「見る」に係る文節は「吾輩は」と「ものを」と解析された場合は，次のような出力になるはずである．
始める  で
見る    は を

このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．
・コーパス中で頻出する述語と格パターンの組み合わせ
・「する」「見る」「与える」という動詞の格パターン（コーパス中で出現頻度の高い順に並べよ）
'''
from no41 import Chunk, load_cabocha
from no43 import search_pos
import sys


if __name__ == '__main__':
    infile = open('../data/neko.txt.cabocha', 'rt', encoding='utf8')
    sents = load_cabocha(infile)
    infile.close()
    outfile = open('../data/out45.txt', 'wt', encoding='utf8')
    # import pdb; pdb.set_trace()
    for sent in sents:
        sent2 = sent
        for chunk in sent:
            predicate = search_pos(chunk, "動詞", bool=False)
            if predicate:
                particles = []
                for chunk2 in sent2:
                    particle = search_pos(chunk2, "助詞", bool=False)
                    if particle and chunk2.dst == chunk.idx:
                        particles.append(particle)
                if particles:
                    outfile.write("{}\t{}\n".format(predicate.base,
                                           " ".join([particle.base for particle in particles])))
    outfile.close()