'''
27. 内部リンクの除去
26の処理に加えて，テンプレートの値からMediaWikiの内部リンクマークアップを除去し，
テキストに変換せよ（参考: マークアップ早見表）．

argv[1]: [INPUT] UK text file
'''
import re


def removeInnerLinks(string):
    inlink_ptrn = re.compile(r'\[\[(?!ファイル:)(.+?)(#.+?)?(\|.+?)?\]\]')
    inlinks = inlink_ptrn.findall(string)
    repls = _gen_repls(inlinks)
    for repl in repls:
        string = inlink_ptrn.sub(repl, string, count=1)
    return string


def _gen_repls(found):
    for article, _, surface in found:
        if surface:
            yield surface.replace("|", "")
        else:
            yield article


if __name__ == '__main__':
    import sys
    basic_ptrn = re.compile(r'^\|(?P<field>.+?) = (?P<value>.+?)$')
    UK_data = open(sys.argv[1], 'r')
    basic_dict = {}
    for line in UK_data:
        if basic_ptrn.match(line):
            basic_info = basic_ptrn.search(line)
            field = basic_info.group('field')
            value = removeInnerLinks(basic_info.group('value').replace("'", ""))
            basic_dict[field] = value
    UK_data.close()
    print(*["{}: {}".format(k, v) for k, v in basic_dict.items()], sep="\n")
