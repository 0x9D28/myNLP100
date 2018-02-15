'''
81. 複合語からなる国名への対処
英語では，複数の語の連接が意味を成すことがある．
例えば，アメリカ合衆国は"United States"，
イギリスは"United Kingdom"と表現されるが，
"United"や"States"，"Kingdom"という単語だけでは，
指し示している概念・実体が曖昧である．
そこで，コーパス中に含まれる複合語を認識し，
複合語を1語として扱うことで，複合語の意味を推定したい．
しかしながら，複合語を正確に認定するのは大変むずかしいので，
ここでは複合語からなる国名を認定したい．

インターネット上から国名リストを各自で入手し，
80のコーパス中に出現する複合語の国名に関して，
スペースをアンダーバーに置換せよ．
例えば，"United States"は"United_States"，
"Isle of Man"は"Isle_of_Man"になるはずである．
'''
import sys


def join_compounds(string, compounds, sep="_"):
    '''
    replace compounds separated by space
    to compounds separated by underbar 
    '''
    for compound in compounds:
        inserted = sep.join(compound.split())
        string = string.replace(compound, inserted)
    return string


if __name__ == '__main__':
    infile1 = open(sys.argv[1], 'rt')
    infile2 = open(sys.argv[2], 'rt')
    outfile = open(sys.argv[3], 'wt')
    countries = [country.rstrip('\n') for country in infile2]
    for i, line in enumerate(infile1):
        outfile.write(join_compounds(line, countries))
    infile1.close()
    infile2.close()
    outfile.close()



