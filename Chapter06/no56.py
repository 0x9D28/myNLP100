'''
56. 共参照解析
Stanford Core NLPの共参照解析の結果に基づき，文中の参照表現（mention）を代表参照表現
（representative mention）に置換せよ．
ただし，置換するときは，「代表参照表現（参照表現）」のように，元の参照表現が分かるように配慮せよ．
'''
import xml.etree.ElementTree as ET
from collections import OrderedDict


def get_indexed_text(xml):
    '''
    Return a dictionary (key: sentence id,
    value: list containing (tokenID, word) tuples)
    '''
    tree = ET.parse(xml)
    root = tree.getroot()
    container = OrderedDict()
    for sent in root.iter('sentence'):
        if sent.attrib:
            container[sent.attrib['id']] = []
            for token in sent.iter('token'):
                container[sent.attrib['id']].append((token.attrib['id'],
                                                     token.find('word').text))
    return container


def get_coreferences(xml):
    '''
    Return a dictionary (key: mention,
    value: representative mention)
    '''
    tree = ET.parse(xml)
    root = tree.getroot()
    coref_container = OrderedDict()
    for coref in root.iter('coreference'):
        for ment in coref.findall('mention'):
            if ment.attrib:
                rep = ment
            else:
                coref_container[ment] = rep
    return coref_container


def get_rep_mention(coref_container, sent_id, token_id):
    '''
    Return a mention and the representative mention.
    '''
    for ment, rep in coref_container.items():
        if ment.find('sentence').text == sent_id \
           and ment.find('start').text == token_id:
            return rep, ment
    return None, None


if __name__ == '__main__':
    xml = 'nlp.xml'
    coref_container = get_coreferences(xml)
    text_container = get_indexed_text(xml)
    f = open('nlp56.txt', 'w')
    for sent_id, tokens in text_container.items():
        end = ""
        for token_id, word in tokens:
            rep, ment = get_rep_mention(coref_container, sent_id, token_id)
            # when hitting a mention, write the representative mention
            # before write a current word
            if rep and ment:
                f.write(rep.find('text').text+" ")
                f.write("( ")
                end = ment.find('end').text
            # when mention ends, write ")"
            elif end == token_id:
                f.write(") ")
            # finally, always write a current word
            f.write(word+" ")
    f.close()
