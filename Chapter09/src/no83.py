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
    if i % 1000000 == 0:
        print('iter: {} ({}%)'.format(i, round(100*i/120000000, 2)))
        print("{} GB".format(sys.getsizeof(ftc)/10**9))
infile.close()
print("finished iter for f(t,c)")
with open(os.path.join(outdir, 'ftc.pkl'), 'wb') as f:
    pickle.dump(ftc, f)
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
        print("iter: {} ({}%)".format(i, round(100*i/120000000, 2)))
infile.close()
print("finished iter for f(t,*), f(*,c) and N")
with open(os.path.join(outdir, 'ft.pkl'), 'wb') as f:
    pickle.dump(ft, f)
print("dump f(t,*)")
with open(os.path.join(outdir, 'fc.pkl'), 'wb') as f:
    pickle.dump(fc, f)
print("dump f(t,*)")
with open(os.path.join(outdir, 'N.pkl'), 'wb') as f:
    pickle.dump(N, f)
print("dump N")
