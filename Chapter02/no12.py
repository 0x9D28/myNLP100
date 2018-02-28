'''
12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，
2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
確認にはcutコマンドを用いよ．
'''
import sys
import os.path

infname = sys.argv[1]
outfname1 = os.path.join(os.path.dirname(infname), 'col1.txt')
outfname2 = os.path.join(os.path.dirname(infname), 'col2.txt')

infile = open(infname, 'rt')
outfile1 = open(outfname1, 'wt')
outfile2 = open(outfname2, 'wt')

for line in infile:
    line = line.split('\t')
    outfile1.write(line[0]+"\n")
    outfile2.write(line[1]+"\n")

infile.close()
outfile1.close()
outfile2.close()
