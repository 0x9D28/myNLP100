'''
86. 単語ベクトルの表示
85で得た単語の意味ベクトルを読み込み，
"United States"のベクトルを表示せよ．
ただし，"United States"は内部的には
"United_States"と表現されていることに注意せよ．
'''
import pickle as pkl
import sys
import os

if __name__ == '__main__':
    infile = sys.argv[1]
    with open(infile, 'rb') as f:
        X = pkl.load(f)
    
    print(X['United_States'])
