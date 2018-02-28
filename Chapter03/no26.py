'''
26. 強調マークアップの除去
25の処理時に，テンプレートの値からMediaWikiの強調マークアップ
（弱い強調，強調，強い強調のすべて）を除去してテキストに変換せよ
（参考: https://ja.wikipedia.org/wiki/Help:早見表）．

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
        field = basic_info.group('field')
        value = basic_info.group('value').replace("'", "")
        basic_dict[field] = value
UK_data.close()
print(*["{}: {}".format(k, v) for k, v in basic_dict.items()], sep="\n")
