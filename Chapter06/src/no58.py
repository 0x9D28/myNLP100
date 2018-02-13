'''
58. タプルの抽出
Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）に基づき，
「主語 述語 目的語」の組をタブ区切り形式で出力せよ．
ただし，主語，述語，目的語の定義は以下を参考にせよ．
・述語: nsubj関係とdobj関係の子（dependant）を持つ単語
・主語: 述語からnsubj関係にある子（dependent）
・目的語: 述語からdobj関係にある子（dependent）
'''
import xml.etree.ElementTree as ET
import sys
from collections import defaultdict


def write_SVO(xml_fname):
    '''
    write SVOs
    '''
    for nest_dic in _extract_SVO(xml_fname):
        for k, v in nest_dic.items():
            if 'nsubj' in v and 'dobj' in v:
                print("{}\t{}\t{}".format(
                      v['nsubj'][1], k[1], v['dobj'][1]))


def _extract_SVO(xml_fname):
    '''
    Return a list containing dictionaries (key: "gov" or "dev",
    value: (idx, txt) tuple)
    '''
    tree = ET.parse(xml)
    root = tree.getroot()
    for deps in root.iter('dependencies'):
        if deps.attrib['type'] == 'collapsed-dependencies':
            svo_dic = defaultdict(dict)
            for dep in deps.findall('dep'):
                if dep.attrib['type'] == 'nsubj' \
                   or dep.attrib['type'] == 'dobj':
                    gov_txt = dep.find('governor').text
                    gov_idx = dep.find('governor').attrib['idx']
                    dep_txt = dep.find('dependent').text
                    dep_idx = dep.find('dependent').attrib['idx']
                    svo_dic[(gov_idx, gov_txt)][dep.attrib['type']] \
                        = (dep_idx, dep_txt)
            yield svo_dic


if __name__ == '__main__':
    xml = sys.argv[1]
    write_SVO(xml)
