'''
44. 係り受け木の可視化
与えられた文の係り受け木を有向グラフとして可視化せよ．可視化には，係り受け木をDOT言語に変換し，
Graphvizを用いるとよい．また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
'''
import sys
from no41 import Chunk, load_cabocha
import pydot
import os


def write_digraph(sents, outdir):
    '''
    write digraph png files in outdir
    '''
    for i, sent in enumerate(sents, start=1):
        graph = pydot.Dot(graph_type='digraph')
        for chunk in sent[:-1]:
            cur_idx, cur_text = chunk.idx, chunk.surface
            dst_idx, dst_text = chunk.dst, sent[chunk.dst].surface
            cur_node = pydot.Node("({}) {}".format(cur_idx, cur_text))
            dst_node = pydot.Node("({}) {}".format(dst_idx, dst_text))
            graph.add_node(cur_node)
            graph.add_node(dst_node)
            graph.add_edge(pydot.Edge(cur_node, dst_node))
        graph.write_png(os.path.join(outdir, 'digraph-{}.png'.format(i)))




if __name__ == '__main__':
    import sys
    infile = open(sys.argv[1], 'rt')
    outdir = sys.argv[2]
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    sents = load_cabocha(infile)
    write_digraph(sents, outdir)
    infile.close()
