'''
13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，
元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
確認にはpasteコマンドを用いよ．
'''
import sys

infile1 = open(sys.argv[1], 'rt')
infile2 = open(sys.argv[2], 'rt')
outfile = open(sys.argv[3], 'wt')

for line1, line2 in zip(infile1, infile2):
    outfile.write("{}\t{}".format(line1.rstrip("\n"), line2))

infile1.close()
infile2.close()
outfile.close()
