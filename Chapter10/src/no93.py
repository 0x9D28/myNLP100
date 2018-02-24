'''
93. アナロジータスクの正解率の計算
92で作ったデータを用い，各モデルのアナロジータスクの正解率を求めよ．
'''
import sys


if __name__ == '__main__':
    infile = open(sys.argv[1], 'rt')
    hm_cnt = {'o':0, 'x':0}
    w2v_cnt = {'o':0, 'x':0}
    for line in infile:
        words = line.rstrip('\n').split()
        ans = words[-3]
        hm_predict = words[-2].split(':')[0]
        w2v_predict = words[-1].split(':')[0]
        if ans == hm_predict:
            hm_cnt['o'] += 1
        else:
            hm_cnt['x'] += 1
        if ans == w2v_predict:
            w2v_cnt['o'] += 1
        else:
            w2v_cnt['x'] += 1
    print("HandMadeModel's accuracy: {}".format(hm_cnt['o']/(hm_cnt['o']+hm_cnt['x'])))
    print("Word2VecModel's accuracy: {}".format(w2v_cnt['o']/(w2v_cnt['o']+w2v_cnt['x'])))
