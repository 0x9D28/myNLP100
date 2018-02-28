'''
20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．
問題21-29では，ここで抽出した記事本文に対して実行せよ．

argv[1]: [INPUT]  jawiki-country.json
argv[2]: [OUTPUT] UK text file
'''
import json


def extract_data(infile, title):
    with open(infile, 'r') as f:
        for line in f:
            country_data = json.loads(line)
            if country_data['title'] == title:
                return country_data
    raise KeyError("'{}' data is not in {}".format(title, infile))


def write_data(outfile, dictionary):
    f = open(outfile, 'w')
    for k, v in dictionary.items():
        f.write("{}: {}".format(k, v))
    f.close()


if __name__ == '__main__':
    import sys
    UK_data = extract_data(sys.argv[1], "イギリス")
    write_data(sys.argv[2], UK_data)
