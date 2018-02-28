'''
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．

argv[1]: [INPUT] UK text file
'''
import re
import sys

UK_data = open(sys.argv[1], 'r').readlines()
sec_ptrn = re.compile(r'^=+(.+?)=+$')
for line in UK_data:
    if sec_ptrn.match(line):
        level = int((line.count("=") / 2) - 1)
        sec_name = sec_ptrn.sub(string=line.rstrip("\n"), repl=r'\g<1>')
        print("{}: level{}".format(sec_name, level))
UK_data.close()
