'''
47. 機能動詞構文のマイニング
動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．
46のプログラムを以下の仕様を満たすように改変せよ．

・「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
・述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，最左の動詞を用いる
・述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで辞書順に並べる
・述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる（助詞の並び順と揃えよ）

例えば「別段くるにも及ばんさと、主人は手紙に返事をする。」という文から，
以下の出力が得られるはずである．
返事をする      と に は        及ばんさと 手紙に 主人は

このプログラムの出力をファイルに保存し，以下の事項をUNIXコマンドを用いて確認せよ．
・コーパス中で頻出する述語（サ変接続名詞+を+動詞）
・コーパス中で頻出する述語と助詞パターン
'''
from no41 import Chunk, load_cabocha
from no43 import search_pos
import sys


if __name__ == '__main__':
    infile = open(sys.argv[1], 'rt')
    sents = load_cabocha(infile)
    outfile = open(sys.argv[2], 'wt')
    # import pdb; pdb.set_trace()
    for sent in sents:
        sent2 = sent
        for chunk in sent:
            # want most left verb in chunk
            predicate = search_pos(chunk, pos="動詞", fmt='morph')
            if predicate:
                particles = []
                chunk2s = []
                for chunk2 in sent2:
                    # want most right particle in chunk
                    particle_chunk = search_pos(chunk2, "助詞", fmt='chunk')
                    if particle_chunk and chunk2.dst == chunk.idx:
                        particle = [morph for morph in particle_chunk.morphs
                                    if morph.pos == '助詞'][-1]
                        particles.append(particle)
                        chunk2s.append(chunk2)
                wo_case_chunk = search_pos(chunk2s, pos="助詞", base="を", fmt='chunk')
                if search_pos(wo_case_chunk, pos="名詞", pos1="サ変接続"):
                    idx = chunk2s.index(wo_case_chunk)
                    del chunk2s[idx]
                    del particles[idx]
                    particles = " ".join([particle.base for particle in particles])
                    arguments = " ".join([c.surface for c in chunk2s])
                    outfile.write("{}\t{}\t{}\n".format(
                        wo_case_chunk.surface+predicate.base, particles, arguments))
    infile.close()
    outfile.close()
