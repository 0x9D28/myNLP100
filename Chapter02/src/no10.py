'''
10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．
'''
import sys

infile = sys.argv[1]
with open(infile, 'rt') as f:
    print(len(f.readlines()))
