'''
28. MediaWikiマークアップの除去
27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，
国の基本情報を整形せよ．

argv[1]: [INPUT] UK text file
'''
import re
import sys


def normalizeAngleContents(string):
    '''format [] markup'''
    inlink_ptrn = re.compile(r'\[\[(.+?)(#.+?)?(\|.+?)?\]\]')
    inlinks = inlink_ptrn.findall(string)
    repls = _gen_3repls(inlinks)
    for repl in repls:
        string = inlink_ptrn.sub(repl, string, count=1)
    return string


def _gen_3repls(found):
    for article, _, surface in found:
        if surface:
            yield surface.replace("|", "")
        else:
            yield article


def normalizeCurlyContents(string):
    '''format {} markup'''
    langnote_ptrn = re.compile(r'\{\{(.+?)(\|.+?)(\|.+?)\}\}')
    langnotes = langnote_ptrn.findall(string)
    repls = _gen_3repls(langnotes)
    for repl in repls:
        string = langnote_ptrn.sub(repl, string, count=1)
    return string


if __name__ == '__main__':
    basic_ptrn = re.compile(r'^\|(?P<field>.+?) = (?P<value>.+?)$')
    tag_ptrn1 = re.compile(r'<.+?>.+</.+?>')
    tag_ptrn2 = re.compile(r'<.+?/>')
    UK_data = open(sys.argv[1], 'r')
    basic_dict = {}
    for line in UK_data:
        if basic_ptrn.match(line):
            basic_info = basic_ptrn.search(line)
            field = basic_info.group('field')
            value = basic_info.group('value').replace("'", "")
            value = normalizeAngleContents(value)
            value = tag_ptrn1.sub("", value)
            value = tag_ptrn2.sub("", value)
            value = normalizeCurlyContents(value)
            basic_dict[field] = value
    UK_data.close()
    print(*["{}: {}".format(k, v) for k, v in basic_dict.items()], sep="\n")
