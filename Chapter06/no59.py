'''
59. S式の解析
Stanford Core NLPの句構造解析の結果（S式）を読み込み，
文中のすべての名詞句（NP）を表示せよ．入れ子になっている名詞句もすべて表示すること．
'''
import xml.etree.ElementTree as ET
import sys


def extract_phrases(string, tag):
    sexp = parse_sexp(string)
    


def parse_sexp(string):
    """
    from https://en.wikipedia.org/wiki/S-expression
    >>> parse_sexp("(+ 5 (+ 3 5))")
    [['+', '5', ['+', '3', '5']]]
    """
    sexp = [[]]
    word = ''
    in_str = False
    for char in string:
        if char is '(' and not in_str:
            sexp.append([])
        elif char is ')' and not in_str:
            if word:
                sexp[-1].append(word)
                word = ''
            temp = sexp.pop()
            sexp[-1].append(temp)
        elif char in (' ', '\n', '\t') and not in_str:
            if word:
                sexp[-1].append(word)
                word = ''
        elif char is '\"':
            in_str = not in_str
        else:
            word += char
    return sexp[0]


if __name__ == '__main__':
    tree = ET.parse(sys.argv[1])
    root = tree.getroot()
    for sexp in root.iter('parse') :
        NP_list = extract_phrases(sexp.text, 'NP')
        print(*NP_list, sep='\n')
