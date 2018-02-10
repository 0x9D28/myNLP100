'''
15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，
入力のうち末尾のN行だけを表示せよ．
確認にはtailコマンドを用いよ．
'''
import sys

infile = open(sys.argv[1], 'rt')
N = int(sys.argv[2])

lines = []
for i, line in enumerate(reversed(infile.readlines())):
    if N == i:
        break
    lines.append(line)
print(*reversed(lines), sep="")

infile.close()
