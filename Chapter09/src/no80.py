'''
80. コーパスの整形
文を単語列に変換する最も単純な方法は，空白文字で単語に区切ることである．
ただ，この方法では文末のピリオドや括弧などの記号が単語に含まれてしまう．
そこで，コーパスの各行のテキストを空白文字でトークンのリストに分割した後，
各トークンに以下の処理を施し，単語から記号を除去せよ．
・トークンの先頭と末尾に出現する次の文字を削除: .,!?;:()[]'"
・空文字列となったトークンは削除
以上の処理を適用した後，トークンをスペースで連結してファイルに保存せよ．
'''
import re
import sys

rm_head = re.compile(r'^[\.,!\?;:\(\)\[\]\'\"]+(.+)$')
rm_tail = re.compile(r'^(.+?)[\.,!\?;:\(\)\[\]\'\"]+?$')

infile = open(sys.argv[1], 'rt')
outfile = open(sys.argv[2], 'wt')
lines = []
print("start spliting sentences into tokens")
for i, line in enumerate(infile, start=1):
    for token in line.split():
        token = rm_head.sub(repl='\g<1>', string=token)
        token = rm_tail.sub(repl='\g<1>', string=token)
        outfile.write(token + " ")
    outfile.write("\n")
    if i % 50000 == 0:
        print("iter: {} ({}%)".format(i, round(100*i/2875326, 2)))
infile.close()
outfile.close()
print("finished spliting sentences into tokens")
