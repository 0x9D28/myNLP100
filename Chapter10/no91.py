'''
91. アナロジーデータの準備
単語アナロジーの評価データをダウンロードせよ．
このデータ中で": "で始まる行はセクション名を表す．
例えば，": capital-common-countries"という行は，
"capital-common-countries"というセクションの開始を表している．
ダウンロードした評価データの中で，"family"というセクションに
含まれる評価事例を抜き出してファイルに保存せよ．
'''
import sys

if __name__ == '__main__':
    start_flag = False
    infile = open(sys.argv[1], 'rt', encoding='utf8')
    outfile = open(sys.argv[2], 'wt', encoding='utf8')
    for line in infile:
        if line.rstrip('\n') == ': family':
            start_flag = True
        elif line[0] != ':' and start_flag:
            outfile.write(line)
        elif line[0] == ':' and start_flag:
            break
    infile.close()
    outfile.close()