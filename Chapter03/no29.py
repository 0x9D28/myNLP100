'''
29. 国旗画像のURLを取得する
テンプレートの内容を利用し，国旗画像のURLを取得せよ．
（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）

argv[1]: [INPUT] UK text file
'''
import re
import json
from urllib.parse import urlencode
from urllib.request import urlopen


def recursive_search(dictionary, key):
    value = None
    for k, v in dictionary.items():
        if k == key:
            return v
        elif type(v) is dict:
            value = recursive_search(v, key)
    return value


if __name__ == '__main__':
    import sys
    basic_ptrn = re.compile(r'^\|(?P<field>.+?) = (?P<value>.+?)$')
    UK_data = open(sys.argv[1], 'r')
    basic_dict = {}
    for line in UK_data:
        if basic_ptrn.match(line):
            basic_info = basic_ptrn.search(line)
            if basic_info.group('field') == "国旗画像":
                fname = basic_info.group('value')
    UK_data.close()

    API = "https://en.wikipedia.org/w/api.php"
    fname = 'File:' + fname
    values = {'action': 'query', 'titles': fname,
              'prop': 'imageinfo', 'format': 'json', 'iiprop': 'url'}
    params = urlencode(values)
    url = API + "?" + params
    print("Accessing to "+url)
    data = json.loads(urlopen(url).read().decode('utf-8'))
    print(recursive_search(data, 'imageinfo')[0]['url'])
