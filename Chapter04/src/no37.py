'''
37. 頻度上位10語
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．

argv[1]: [INPUT]  neko.txt.mecab
argv[2]: [OUTPUT] word-freq barchart file name
'''
from no30 import read_morphemes
from no36 import get_flat_data
from collections import Counter
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import sys


fp = FontProperties(fname="/usr/share/fonts/truetype/takao-gothic/TakaoExGothic.ttf")
sentences = read_morphemes(sys.argv[1])
cnt = Counter(get_flat_data(key="base", sents=sentences))
words, freqs = [], []
for i, (word, freq) in enumerate(sorted(cnt.items(), key=lambda x: -x[1])):
    if i > 9:
        break
    else:
        words.append(word)
        freqs.append(freq)
print(words)
print(freqs)
plt.bar(range(10), freqs)
plt.xticks(range(10), words, fontproperties=fp)
plt.xlabel("word")
plt.ylabel("frequency")
plt.savefig(sys.argv[2])
plt.close()
