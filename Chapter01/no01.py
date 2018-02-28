'''
01. 「パタトクカシーー」
「パタトクカシーー」という文字列の1,3,5,7文字目を取り出して連結した文字列を得よ．
'''

string = "パタトクカシーー"
pickup_idx = [0, 2, 4, 6]
pickup_str = "".join([c for i, c in enumerate(string) if i in pickup_idx])
print(pickup_str)
