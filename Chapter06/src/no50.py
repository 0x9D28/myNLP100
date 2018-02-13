'''
(. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを
文の区切りと見なし，入力された文書を1行1文の形式で出力せよ．
'''
import re


def SplitSentences(fin, fout):
    '''Convert txt file format to one sentence per line format.'''
    # end mark → space → upper case
    pttrn = re.compile(r'([\.;:\?\!])\s([A-Z])')
    with open(fin, 'rt') as fi, open(fout, 'wt') as fo:
        for line in fi:
            # split a line into sentences
            nline = pttrn.sub(r'\g<1>\n\g<2>', line)
            if nline != "\n":
                fo.write(nline)


if __name__ == '__main__':
    fin = 'nlp.txt'
    fout = 'nlp50.txt'
    SplitSentences(fin, fout)
