'''
17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．
確認にはsort, uniqコマンドを用いよ．
'''
import sys

infname = sys.argv[1]
infile = open(infname, 'rt')

word_set = set()
for line in infile:
    line = line.split('\t')
    word_set.update([c for c in line[0]])
print(word_set)

infile.close()
