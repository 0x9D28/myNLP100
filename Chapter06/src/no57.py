'''
57. 係り受け解析
Stanford Core NLPの係り受け解析の結果
（collapsed-dependencies）を有向グラフとして可視化せよ．
可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．
また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．


'''
import pydot
import xml.etree.ElementTree as ET
import os


def write_digraph(xml_fname, outdir):
    '''
    write digraphes (gov -> dep)
    '''
    for i, dep_relations in enumerate(_get_dep_relations(xml_fname), start=1):
        graph = pydot.Dot(graph_type='digraph')
        for relation in dep_relations:
            gov_idx, gov_txt = relation['gov']
            dep_idx, dep_txt = relation['dep']
            gov_node = pydot.Node("({}) {}".format(gov_idx, gov_txt))
            dep_node = pydot.Node("({}) {}".format(dep_idx, dep_txt))
            graph.add_node(gov_node)
            graph.add_node(dep_node)
            graph.add_edge(pydot.Edge(gov_node, dep_node))
        graph.write_png(os.path.join(outdir, 'digraph-{}.png'.format(i)))


def _get_dep_relations(xml_fname):
    '''
    Return a list containing dictionaries (key: "gov" or "dev",
    value: (idx, txt) tuple)
    '''
    tree = ET.parse(xml)
    root = tree.getroot()
    for deps in root.iter('dependencies'):
        if deps.attrib['type'] == 'collapsed-dependencies':
            deps_list = []
            for dep in deps.findall('dep'):
                gov_txt = dep.find('governor').text
                gov_idx = dep.find('governor').attrib['idx']
                dep_txt = dep.find('dependent').text
                dep_idx = dep.find('dependent').attrib['idx']
                deps_list.append({"gov": (gov_idx, gov_txt),
                                  "dep": (dep_idx, dep_txt)})
            yield deps_list


if __name__ == '__main__':
    import sys
    xml = sys.argv[1]
    outdir = sys.argv[2]
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    write_digraph(xml, outdir)
