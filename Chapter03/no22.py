'''
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

argv[1]: [INPUT] UK text file
'''
import re
import sys

UK_data = open(sys.argv[1], 'r').readlines()
category_pattern = re.compile(r'\[\[Category:(.+.?)\]\]')
for line in UK_data:
    if category_pattern.match(line):
        print(category_pattern.sub(string=line.rstrip("\n"), repl=r'\g<1>'))
UK_data.close()
