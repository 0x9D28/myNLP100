'''
08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
・英小文字ならば(219 - 文字コード)の文字に置換
・その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
'''
import re


def cipher(string):
    return "".join([chr(219-ord(c)) if re.match(r'[a-z]', c) else c for c in string])


if __name__ == '__main__':
    string = "I am an NLPer"
    print("Origin:  " + string)
    encode = cipher(string)
    print("Encoded: " + encode)
    decode = cipher(encode)
    print("Decoded: " + decode)
