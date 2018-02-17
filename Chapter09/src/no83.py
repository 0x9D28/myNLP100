'''
83. 単語／文脈の頻度の計測
82の出力を利用し，以下の出現分布，および定数を求めよ．
・f(t,c): 単語tと文脈語cの共起回数
・f(t,∗): 単語tの出現回数
・f(∗,c): 文脈語cの出現回数
・N: 単語と文脈語のペアの総出現回数

save (f(t,c), f(t,*), f(*,c), N) tuple as pickle file
'''
import sys
from collections import defaultdict, Counter
import pickle
import os

infile = open(sys.argv[1], 'rt')
outdir = sys.argv[2]
ftc = defaultdict(Counter)
ft = Counter()
fc = Counter()
N = 0

if not os.path.exists(outdir):
    os.mkdir(outdir)

for i, line in enumerate(infile):
    term, context = line.split("\t")
    context = context.split()
    ftc[term].update(context)
    if i % 10**6 == 0:
        print('iter: {} ({}%)'.format(i, round(100*i/120418829, 2)))
    if i / (10**7) > 1:
        break
infile.close()
print("finished iter for f(t,c)")
with open(os.path.join(outdir, 'ftc.txt'), 'wt') as f:
    for word, context in ftc.items():
        context = ["{}:{}".format(k, v) for k, v in context.items()]
        f.write("{}\t{}\n".format(word, ",".join(context)))
del ftc  # because too large data
print("dump f(t,c)")

infile = open(sys.argv[1], 'rt')
for i, line in enumerate(infile):
    term, context = line.split("\t")
    context = context.split()
    ft.update([term])
    fc.update(context)
    N += len(context)
    if i % 1000000 == 0:
        print("iter: {} ({}%)".format(i, round(100*i/120418829, 2)))
    if i / (10**7) > 1:
        break
infile.close()
print("finished iter for f(t,*), f(*,c) and N")
with open(os.path.join(outdir, 'ft.txt'), 'wt') as f:
    for word, freq in ft.items():
        f.write("{}:{}\n".format(word, freq))
print("written f(t,*)")
with open(os.path.join(outdir, 'fc.txt'), 'wt') as f:
    for word, freq in fc.items():
        f.write("{}:{}\n".format(word, freq))
print("written f(*,c)")
with open(os.path.join(outdir, 'N.txt'), 'wt') as f:
    f.write(str(N))
print("written N")
