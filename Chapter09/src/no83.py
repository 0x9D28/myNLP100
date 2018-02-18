'''
83. 単語／文脈の頻度の計測
82の出力を利用し，以下の出現分布，および定数を求めよ．
・f(t,c): 単語tと文脈語cの共起回数
・f(t,∗): 単語tの出現回数
・f(∗,c): 文脈語cの出現回数
・N: 単語と文脈語のペアの総出現回数

$ python3 no83.py [input no.82 output] [number of no.82 output lines (gotten by wc command)] [necessary input amount assigned percentile (0, 100]] [output directory]
'''
import sys
from collections import defaultdict, Counter
import os

infile = open(sys.argv[1], 'rt')
outdir = sys.argv[4]
ftc = defaultdict(Counter)
ft = Counter()
fc = Counter()
N = 0

if not os.path.exists(outdir):
    os.mkdir(outdir)

length = int(sys.argv[2])  # number of out82.txt lines
uplimit = float(sys.argv[3])  # use uplimit[%] of out82.txt
for i, line in enumerate(infile, start=1):
    term, context = line.split("\t")
    context = context.split()
    ftc[term].update(context)
    ft.update([term])
    fc.update(context)
    N += len(context)
    percentile = round(100 * i / length, 2)
    if i % 10**6 == 0:
        print('counting frequency: {}%'.format(percentile))
    if percentile > uplimit:
        break
infile.close()
print("finished counting")

print("voc size: {}".format(len(ft)))

# write data as txt file
print("start writing N")
with open(os.path.join(outdir, 'N.txt'), 'wt') as f:
    f.write(str(N))
print("written N")
del N

print("start writing f(t,*)")
with open(os.path.join(outdir, 'ft.txt'), 'wt') as f:
    length = len(ft)
    for i, k_v in enumerate(ft.items(), start=1):
        word, freq = k_v
        f.write("{}:{}\n".format(word, freq))
        if i % 10**5 == 0:
            print("writing f(t,*): {}%".format(100*i/length))
print("written f(t,*)")
del ft

print("start writing f(*,c)")
with open(os.path.join(outdir, 'fc.txt'), 'wt') as f:
    length = len(fc)
    for i, k_v in enumerate(fc.items(), start=1):
        word, freq = k_v
        f.write("{}:{}\n".format(word, freq))
        if i % 10**5 == 0:
            print("writing f(*,c): {}%".format(100*i/length))
print("written f(*,c)")
del fc

print("start writing f(t,c)")
with open(os.path.join(outdir, 'ftc.txt'), 'wt') as f:
    length = len(ftc)
    for i, k_v in enumerate(ftc.items(), start=1):
        word, context = k_v
        context = ["{}:{}".format(k, v) for k, v in context.items()]
        f.write("{}\t{}\n".format(word, ",".join(context)))
        if i % 10**5 == 0:
            print("writing f(t,c): {}%".format(100*i/length))
print("written f(t,c)")

