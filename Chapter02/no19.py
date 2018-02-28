'''
19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
確認にはcut, uniq, sortコマンドを用いよ．
'''
import sys
from collections import Counter

infile = open(sys.argv[1], 'rt')

word_cnt = Counter()
for line in infile:
    line = line.split('\t')
    word_cnt.update(line[0])
for k, v in sorted(word_cnt.items(), key=lambda x: -x[1]):
    print("{}: {}".format(k, v))

infile.close()
