'''
54. 品詞タグ付け
Stanford Core NLPの解析結果XMLを読み込み，
単語，レンマ，品詞をタブ区切り形式で出力せよ．
'''
import xml.etree.ElementTree as ET


def getElements(fin, fout):
    '''Output word-lemma-POS per line.'''
    tree = ET.parse(fin)
    root = tree.getroot()
    with open(fout, 'wt') as fo:
        for tokens in root.iter('tokens'):
            for token in tokens.findall('token'):
                word = token.find('word').text
                lemma = token.find('lemma').text
                POS = token.find('POS').text
                fo.write("{}\t{}\t{}\n".format(word, lemma, POS))


if __name__ == '__main__':
    fin = 'nlp.xml'
    fout = 'nlp54.txt'
    getElements(fin, fout)
