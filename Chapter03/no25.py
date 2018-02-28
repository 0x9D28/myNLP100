'''
25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，
辞書オブジェクトとして格納せよ．

argv[1]: [INPUT] UK text file
'''
import re
import sys

basic_ptrn = re.compile(r'^\|(?P<field>.+?) = (?P<value>.+?)$')
UK_data = open(sys.argv[1], 'r')
basic_dict = {}
for line in UK_data:
    if basic_ptrn.match(line):
        basic_info = basic_ptrn.search(line)
        basic_dict[basic_info.group('field')] = basic_info.group('value')
UK_data.close()
print(*["{}: {}".format(k, v) for k, v in basic_dict.items()], sep="\n")
