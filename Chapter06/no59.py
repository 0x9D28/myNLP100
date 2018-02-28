'''
59. S式の解析
Stanford Core NLPの句構造解析の結果（S式）を読み込み，
文中のすべての名詞句（NP）を表示せよ．入れ子になっている名詞句もすべて表示すること．

S-expression
<parse>(ROOT (S (PP (NP (JJ Natural) (NN language) (NN processing))
(IN From) (NP (NNP Wikipedia))) (, ,) (NP (NP (DT the) (JJ free)
(NN encyclopedia) (JJ Natural) (NN language) (NN processing))
(PRN (-LRB- -LRB-) (NP (NN NLP)) (-RRB- -RRB-))) (VP (VBZ is)
(NP (NP (NP (DT a) (NN field)) (PP (IN of) (NP (NN computer)
(NN science)))) (, ,) (NP (JJ artificial) (NN intelligence))
(, ,) (CC and) (NP (NP (NNS linguistics)) (VP (VBN concerned)
(PP (IN with) (NP (NP (DT the) (NNS interactions)) (PP (IN between)
(NP (NP (NNS computers)) (CC and) (NP (JJ human) (-LRB- -LRB-)
(JJ natural) (-RRB- -RRB-) (NNS languages)))))))))) (. .))) </parse>
'''
import xml.etree.ElementTree as ET
import sys


def parse_SExpression(string, tag):
    pass


if __name__ == '__main__':
    tree = ET.parse(sys.argv[1])
    root = tree.getroot()
    for s_exp in root.iter('parse') :
        NP_list = parse_SExpression(s_exp.text)
        print(*NP_list, sep='\n')
