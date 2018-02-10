'''
14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，
入力のうち先頭のN行だけを表示せよ．
確認にはheadコマンドを用いよ．
'''
import sys

infile = open(sys.argv[1], 'rt')
N = int(sys.argv[2])

for i, line in enumerate(infile):
    if i == N:
        break
    print(line.rstrip("\n"))

infile.close()
