'''
00. 文字列の逆順
文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
'''

string = "stressed"

revstr = ''.join([c for c in reversed(string)])
print(revstr)

revstr = string[::-1]
print(revstr)
