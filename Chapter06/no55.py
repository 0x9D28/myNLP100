'''
55. 固有表現抽出
入力文中の人名をすべて抜き出せ．
'''

import xml.etree.ElementTree as ET


def getPerson(fin, fout):
    '''Extract person names.'''
    tree = ET.parse(fin)
    root = tree.getroot()
    with open(fout, 'wt') as fo:
        for tokens in root.iter('tokens'):
            for token in tokens.findall('token'):
                POS = token.find('NER').text
                if POS == 'PERSON':
                    word = token.find('word').text
                    fo.write(word+'\n')


if __name__ == '__main__':
    fin = 'nlp.xml'
    fout = 'nlp55.txt'
    getPerson(fin, fout)
