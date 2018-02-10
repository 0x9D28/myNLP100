'''
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．

argv[1]: [INPUT] UK text file
'''
import re
import sys

UK_data = open(sys.argv[1], 'r').readlines()
category_pattern = re.compile(r'\[\[Category:(.+.?)\]\]')
for line in UK_data:
    if category_pattern.match(line):
        print(line.rstrip('\n'))
UK_data.close()
