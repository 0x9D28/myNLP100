'''
09. Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
ただし，長さが４以下の単語は並び替えないこととする．適当な英語の文
（例えば"I couldn't believe that I could actually understand
what I was reading : the phenomenal power of the human mind ."）
を与え，その実行結果を確認せよ．
'''
from random import shuffle

sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
typo_tokens = []
for token in sentence.split():
    if len(token) <= 4:
        typo_tokens.append(token)
    else:
        inner = [c for c in token[1:-1]]
        shuffle(inner)
        typo_tokens.append(token[0]+"".join(inner)+token[-1])

print(*typo_tokens, sep=" ")
