'''
38. ヒストグラム
単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる
単語の種類数を棒グラフで表したもの）を描け．

argv[1]: [INPUT]  neko.txt.mecab
argv[2]: [OUTPUT] word-freq histgram file name
'''
from no30 import read_morphemes
from no36 import get_flat_data
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import sys

if __name__ == "__main__":
    fp = FontProperties(fname="/usr/share/fonts/truetype/takao-gothic/TakaoExGothic.ttf")
    sentences = read_morphemes(sys.argv[1])
    # key: word, value: word-freq
    cnt_wf = Counter(get_flat_data(key="base", sents=sentences))
    freqs = [freq for freq in cnt_wf.values()]
    plt.hist(freqs, bins=max(freqs))
    plt.xlim(1, 50)
    plt.savefig(sys.argv[2])
    plt.close()
