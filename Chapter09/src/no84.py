'''
84. 単語文脈行列の作成
83の出力を利用し，単語文脈行列Xを作成せよ．
ただし，行列Xの各要素X_tcは次のように定義する．
・f(t,c)>=10ならば, X_tc=PPMI(t,c)=max{logN*f(t,c)/(f(t,∗)×f(∗,c)),0}
・f(t,c)<10ならば, X_tc=0
ここで，PPMI(t,c)はPositive Pointwise Mutual Information
（正の相互情報量）と呼ばれる統計量である．
なお，行列Xの行数・列数は数百万オーダとなり，
行列のすべての要素を主記憶上に載せることは無理なので注意すること．
幸い，行列Xのほとんどの要素は0になるので，非0の要素だけを書き出せばよい．
'''
import sys
import os
import pickle
from math import log2
import scipy.sparse as sp
from collections import defaultdict

def pkl_load(indir, infile):
    with open(os.path.join(indir, infile), 'rb') as f:
        obj = pickle.load(f)
    return obj


if __name__ == '__main__':
    # load pickle files
    indir = sys.argv[1]
    infiles = os.listdir(indir)
    for infile in infiles:
        if infile == 'ftc.pkl':
            ftc = pkl_load(indir, infile)
        elif infile == 'ft.pkl':
            ft = pkl_load(indir, infile)
        elif infile == 'fc.pkl':
            fc = pkl_load(indir, infile)
        elif infile == 'N.pkl':
            N = pkl_load(indir, infile)
    # make term-context index for X matrix
    tc_idx = defaultdict(lambda: len(tc_idx))
    for k in ft.keys():
        tc_idx[k]
    # make X matrix embedded PPMI
    size = len(tc_idx)
    X = sp.lil_matrix((size, size))
    for term, contexts in ftc.items():
        for context, freq in contexts.items():
            if freq >= 10:
                pmi = log2(N) + log2(ftc[term][context]) \
                      - log2(ft[term]) - log2(fc[context])
                X[tc_idx[term], tc_idx[context]] = max(pmi, 0)
    # write tc_idx and X as pickle file
    outdir = sys.argv[2]
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    with open(os.path.join(outdir, 'idx.pkl'), 'wb') as outfile1:
        pickle.dump(dict(tc_idx), outfile1)
    with open(os.path.join(outdir, 'X.pkl'), 'wb') as outfile2:
        pickle.dump(X, outfile2)

