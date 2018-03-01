'''
49. 名詞間の係り受けパスの抽出
文中のすべての名詞句のペアを結ぶ最短係り受けパスを抽出せよ．
ただし，名詞句ペアの文節番号がiiとjj（i<ji<j）のとき，係り受けパスは以下の仕様を満たすものとする．

問題48と同様に，パスは開始文節から終了文節に至るまでの各文節の表現
（表層形の形態素列）を"->"で連結して表現する
文節iiとjjに含まれる名詞句はそれぞれ，XとYに置換する
また，係り受けパスの形状は，以下の2通りが考えられる．

文節iiから構文木の根に至る経路上に文節jjが存在する場合: 文節iiから文節jjのパスを表示
上記以外で，文節iiと文節jjから構文木の根に至る経路上で共通の文節kkで交わる場合: 文節iiから文節kkに至る直前のパスと文節jjから文節kkに至る直前までのパス，文節kkの内容を"|"で連結して表示
例えば，「吾輩はここで始めて人間というものを見た。」という文（neko.txt.cabochaの8文目）から，次のような出力が得られるはずである．

Xは | Yで -> 始めて -> 人間という -> ものを | 見た
Xは | Yという -> ものを | 見た
Xは | Yを | 見た
Xで -> 始めて -> Y
Xで -> 始めて -> 人間という -> Y
Xという -> Y
'''
from no41 import Chunk, load_cabocha
from no43 import search_pos
import sys


def get_pos_idx(chunks, pos):
    '''return indexes of chunks having the pos'''
    idxes = []
    for i, chunk in enumerate(chunks):
        if search_pos(chunk, pos):
            idxes.append(i)
    return idxes


def replace_morph(chunk, pos, repl):
    '''
    return surface of chunk replaced
    surface of left side morph(s) having pos with repl
    '''
    rslt = []
    already = False
    for morph in chunk.morphs:
        if not rslt or rslt[-1] != repl:
            if morph.pos == pos and not already:
                rslt.append(repl)
            else:
                rslt.append(morph.surface)
        else:
            if morph.pos != pos:
                already = True
                rslt.append(morph.surface)
    return "".join(rslt)


def does_merge(path1, path2):
    '''
    does separated branches merge on halfway?
    if yes, return a node on which branches merge
    else, return None
    '''
    if len(path1) >= len(path2):
        longer_path = path1
        shorter_path = path2
    else:
        longer_path = path2
        shorter_path = path1
    if shorter_path[0] in longer_path:
        return None
    else:
        for node in shorter_path:
            if node in longer_path:
                return longer_path[longer_path.index(node)]



if __name__ == '__main__':
    infile = open(sys.argv[1], 'rt')
    sents = load_cabocha(infile)
    outfile = open(sys.argv[2], 'wt')

    for sent in sents:
        sent2 = sent
        paths = []
        for chunk in sent:
            noun_chunk = search_pos(chunk, pos="名詞", fmt='chunk')
            if noun_chunk:
                path_chunks = [noun_chunk]
                for current_chunk in sent2:
                    if path_chunks[-1].dst == current_chunk.idx:
                        path_chunks.append(current_chunk)
                paths.append(path_chunks)

        for i, path in enumerate(paths):
            # pattern 2 (straight path)
            noun_idxes = get_pos_idx(path, "名詞")
            if len(noun_idxes) > 2:
                first_idx = noun_idxes[0]
                for second_idx in noun_idxes[1:]:
                    # slice first noun chunk to last noun chunk
                    sliced_path = path[first_idx:second_idx+1]
                    sliced_path[1:-1] = [node.surface for node in sliced_path[1:-1]]
                    sliced_path[0] = replace_morph(sliced_path[0], "名詞", "X")
                    sliced_path[-1] = replace_morph(sliced_path[-1], "名詞", "Y")
                    outfile.write(" -> ".join([node for node in sliced_path])+"\n")
            else:
                # pattern 1 (merge branches on a node)
                paths_cp = paths[i + 1:]
                for path_cp in paths_cp:
                    merge_node = does_merge(path, path_cp)
                    if merge_node:
                        ori_idx = path.index(merge_node)
                        cp_idx = path_cp.index(merge_node)
                        path_surface = [replace_morph(path[0], "名詞", "X")]\
                                       + [c.surface for c in path[1:ori_idx]]
                        path_cp_surface = [replace_morph(path_cp[0], "名詞", "Y")]\
                                          + [c.surface for c in path_cp[1:cp_idx]]
                        outfile.write("{} | {} | {}\n"\
                                      .format(" -> ".join(path_surface),
                                              " -> ".join(path_cp_surface), merge_node.surface))
    infile.close()
    outfile.close()
