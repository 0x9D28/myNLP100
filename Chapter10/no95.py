'''
95. WordSimilarity-353での評価
94で作ったデータを用い，各モデルが出力する類似度のランキングと，
人間の類似度判定のランキングの間のスピアマン相関係数を計算せよ．
'''
import sys
from scipy.stats import spearmanr


if __name__ == '__main__':
    human_sims, hm_sims, wv_sims = [], [], []
    for i, line in enumerate(open(sys.argv[1], 'rt', encoding='utf8')):
        if i == 0:
            continue
        words = line.rstrip('\n').split(',')
        human_sims.append(float(words[-3]))
        hm_sims.append(float(words[-2]))
        wv_sims.append(float(words[-1]))
    hm_coef, hm_p = spearmanr(human_sims, hm_sims)
    wv_coef, wv_p = spearmanr(human_sims, wv_sims)
    print("HandMadeModel: rho-{}, p-{}".format(hm_coef, hm_p))
    print("Word2VecModel: rho-{}, p-{}".format(wv_coef, wv_p))
