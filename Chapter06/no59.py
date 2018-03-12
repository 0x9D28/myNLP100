'''
59. S式の解析
Stanford Core NLPの句構造解析の結果（S式）を読み込み，
文中のすべての名詞句（NP）を表示せよ．入れ子になっている名詞句もすべて表示すること．
'''
import xml.etree.ElementTree as ET
import sys


class SExpressionParser(object):
    """
    S-expression example
     (ROOT (S (PP (NP (JJ Natural) (NN language) (NN processing)) (IN From) (NP (NNP Wikipedia))) (, ,) (NP (NP (DT the) (JJ free) (NN encyclopedia) (JJ Natural) (NN language) (NN processing)) (PRN (-LRB- -LRB-) (NP (NN NLP)) (-RRB- -RRB-))) (VP (VBZ is) (NP (NP (NP (DT a) (NN field)) (PP (IN of) (NP (NN computer) (NN science)))) (, ,) (NP (JJ artificial) (NN intelligence)) (, ,) (CC and) (NP (NP (NNS linguistics)) (VP (VBN concerned) (PP (IN with) (NP (NP (DT the) (NNS interactions)) (PP (IN between) (NP (NP (NNS computers)) (CC and) (NP (JJ human) (-LRB- -LRB-) (JJ natural) (-RRB- -RRB-) (NNS languages)))))))))) (. .)))
    """
    def __init__(self, sexp):
        self.sexp = sexp

    @classmethod
    def parse_sexp(cls, string):
        """
        copy and paste from https://en.wikipedia.org/wiki/S-expression
        and rewrite a few lines for applying to class method
        >>> parse_sexp("(+ 5 (+ 3 5))")
        ['+', '5', ['+', '3', '5']]
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
        SEparser = cls(sexp[0][0])
        return SEparser

    def print_phrases(self, tag):
        """print tag's phrases"""
        if self._search(self.sexp, tag):
            self._recursive_print(self.sexp, tag)
        else:
            return ["<< Not found {} >>".format(tag)]

    def _search(self, sexp, tag):
        """search tag in sexp. return True or False"""
        if sexp == tag:
            return True
        return isinstance(sexp, list) \
            and any(self._search(subsexp, tag) for subsexp in sexp)

    def _recursive_print(self, sexp, tag):
        """recursive search tag's phrases, and print them."""
        if isinstance(sexp, str):
            return None
        elif isinstance(sexp, list) and sexp[0] == tag:
            self._flat_print(sexp)
            print()
        return [self._recursive_print(subsexp, tag) for subsexp in sexp]

    def _flat_print(self, sexp):
        """print words in sexp, ignoring tags"""
        if isinstance(sexp, str):
            return None
        elif isinstance(sexp, list) and len(sexp) == 2 \
                and all(isinstance(elem, str) for elem in sexp):
            print(sexp[1], end=' ')
        return [self._flat_print(subsexp) for subsexp in sexp]




if __name__ == '__main__':
    tree = ET.parse(sys.argv[1])
    root = tree.getroot()
    for sexp in root.iter('parse') :
        print("<< S-Expression >>")
        print(sexp.text)
        print("<< Noun Phrases >>")
        SExpressionParser.parse_sexp(sexp.text).print_phrases('NP')
        print()
