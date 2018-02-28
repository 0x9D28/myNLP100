'''
82. 文脈の抽出
81で作成したコーパス中に出現するすべての単語tに関して，
単語tと文脈語cのペアをタブ区切り形式ですべて書き出せ．
ただし，文脈語の定義は次の通りとする．
・ある単語tの前後d単語を文脈語cとして抽出する
  （ただし，文脈語に単語tそのものは含まない）
・単語tを選ぶ度に，文脈幅dは{1,2,3,4,5}の範囲でランダムに決める．
'''
import sys
import random

infile = open(sys.argv[1], 'rt', encoding='utf8')
outfile = open(sys.argv[2], 'wt', encoding='utf8')

for j, line in enumerate(infile):
    line = line.split()
    for i, token in enumerate(line):
        window_size = random.choice(range(1, 6))
        context = line[i-window_size:i] + line[i+1:i+window_size+1]
        outfile.write("{}\t{}\n".format(token, " ".join(context)))
    if j % 100000 == 0:
        print("iter: {}".format(j))
infile.close()
outfile.close()
