'''
53. Tokenization
Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．
また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．
'''
import xml.etree.ElementTree as ET


def getWords_fromXML(fin, fout):
    '''Read XML file, write a word per line.'''
    tree = ET.parse(fin)
    root = tree.getroot()
    with open(fout, 'wt') as fo:
        for word in root.iter('word'):
            fo.write(word.text + '\n')


if __name__ == '__main__':
    fin = 'nlp.xml'
    fout = 'nlp53.txt'
    getWords_fromXML(fin, fout)
