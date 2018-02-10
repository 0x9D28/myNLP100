'''
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，
入力のファイルを行単位でN分割せよ．
同様の処理をsplitコマンドで実現せよ．
'''
import sys
import os

infile = open(sys.argv[1], 'rt')
N = int(sys.argv[2])
outdir = sys.argv[3]
lines = infile.readlines()
full_len = len(lines)
each_len = 0
for i in range(1, len(lines)+1):
    if full_len / i == N:
        each_len = i
        break
    elif (full_len // i == N - 1) and (full_len % i != 0):
        if each_len == 0:
            each_len = i
if each_len:
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    for i in range(N):
        outfname = os.path.join(outdir, 'out16py-{}.txt'.format(i+1))
        outfile = open(outfname, 'wt')
        outfile.write("".join(lines[each_len*i:each_len*(i+1)]))
        outfile.close()
else:
    print("can not split {} into {} files"
          .format(os.path.basename(sys.argv[1]), N))
