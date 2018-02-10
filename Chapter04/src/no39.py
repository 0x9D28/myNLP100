'''
39. Zipfの法則
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．

argv[1]: [INPUT]  neko.txt.mecab
argv[2]: [OUTPUT] Zipf graph file name
'''
from no30 import read_morphemes
from no36 import get_flat_data
from collections import Counter, OrderedDict
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from math import log2
import sys

if __name__ == "__main__":
    fp = FontProperties(fname="/usr/share/fonts/truetype/takao-gothic/TakaoExGothic.ttf")
    sentences = read_morphemes(sys.argv[1])
    # key: word, value: word-freq
    cnt_wf = Counter(get_flat_data(key="base", sents=sentences))
    # key: rank of occurrence freq, value: the freq
    cnt_rf = OrderedDict()
    for rank, freq in enumerate(sorted(cnt_wf.values(), reverse=True), start=1):
        cnt_rf[rank] = freq

    ranks = [rank for rank in cnt_rf.keys()]
    freqs = [freq for freq in cnt_rf.values()]
    plt.loglog(ranks, freqs)
    plt.savefig(sys.argv[2])
    plt.close()
    '''
    log_ranks = [log2(rank) for rank in cnt_rf.keys()]
    log_freqs = [log2(freq) for freq in cnt_rf.values()]
    plt.scatter(log_ranks, log_freqs)
    plt.savefig(sys.argv[2])
    plt.close()
    '''
