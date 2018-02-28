'''
70. データの入手・整形
文に関する極性分析の正解データを用い，以下の要領で正解データ（sentiment.txt）を作成せよ．
・rt-polarity.posの各行の先頭に"+1 "という文字列を追加する（極性ラベル"+1"とスペースに続けて肯定的な文の内容が続く）
・rt-polarity.negの各行の先頭に"-1 "という文字列を追加する（極性ラベル"-1"とスペースに続けて否定的な文の内容が続く）
・上述1と2の内容を結合（concatenate）し，行をランダムに並び替える
sentiment.txtを作成したら，正例（肯定的な文）の数と負例（否定的な文）の数を確認せよ．

argv[1]: [INPUT]  rt-polarity.pos
argv[2]: [INPUT]  rt-polarity.neg
argv[3]: [OUTPUT] sentiment.txt
'''
import random
import io
import sys

pos_file = io.open(sys.argv[1], encoding='latin-1')
neg_file = io.open(sys.argv[2], encoding='latin-1')
all_reviews = ["+1 {}".format(line) for line in pos_file] \
              + ["-1 {}".format(line) for line in neg_file]
random.shuffle(all_reviews)
pos_file.close()
neg_file.close()
review_fname = sys.argv[3]
review_file = open(review_fname, 'w')
review_file.writelines(all_reviews)
review_file.close()

review_file = open(review_fname, 'r')
pos_cnt = 0
neg_cnt = 0
for line in review_file:
    sentiment = int(line.split(" ")[0])
    if sentiment == 1:
        pos_cnt += 1
    elif sentiment == -1:
        neg_cnt += 1
review_file.close()
print("positive: {}".format(pos_cnt))
print("negative: {}".format(neg_cnt))
