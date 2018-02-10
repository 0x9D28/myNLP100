'''
06. 集合
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
'''
from no05 import Ngram

X = set(Ngram("paraparaparadise"))
Y = set(Ngram("paragraph"))

print("X: {}".format(X))
print("Y: {}".format(Y))
print("Union: {}".format(X.union(Y)))
print("Intersection: {}".format(X.intersection(Y)))
print("Difference: {}".format(X.difference(Y)))
print("Is 'se' in X? -- {}".format('Yes' if 'se' in X else 'No'))
print("Is 'se' in Y? -- {}".format('Yes' if 'se' in Y else 'No'))
