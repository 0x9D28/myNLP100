'''
24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．

argv[1]: [INPUT] UK text file
'''
import re
import sys

UK_data = open(sys.argv[1], 'r').readlines()
media_ptrn = re.compile(r'^\[\[File:(.+?)\|.+?\]\]$')
for line in UK_data:
    if media_ptrn.match(line):
        print(media_ptrn.sub(string=line.rstrip("\n"), repl=r'\g<1>'))
UK_data.close()
