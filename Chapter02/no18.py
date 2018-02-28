'''
18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ
（注意: 各行の内容は変更せずに並び替えよ）．
確認にはsortコマンドを用いよ
（この問題はコマンドで実行した時の結果と合わなくてもよい）．
'''
import sys

infile = open(sys.argv[1], 'rt')
outfile = open(sys.argv[2], 'wt')

hightemp_dic = {}
for line in infile:
    col2 = line.rstrip("\n").split("\t")[2]
    hightemp_dic[float(col2)] = line
for k, v in sorted(hightemp_dic.items(), reverse=True):
    outfile.write(v)

infile.close()
outfile.close()
