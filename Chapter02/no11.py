'''
11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．
確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
'''
import sys

infile = open(sys.argv[1], 'rt')
outfile = open(sys.argv[2], 'wt')

for line in infile:
    outfile.write(line.replace('\t', ' '))

infile.close()
outfile.close()
