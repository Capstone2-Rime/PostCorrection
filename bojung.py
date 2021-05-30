import hgtk
import textdistance
import os
import csv
import numpy as np
from kiwipiepy import Kiwi
loc = "/home/yjlee/capstone_m/"

# db에서 데이터를 튜플 형태로 받아왔다고 가정
a=("14:24:23","kyh","경복꿍에서만이라도 안경의 몬유도원도를 보고 알테피나코택을 생각했다.")
a2=("14:24:28","kyh","그냥 끄는 법이 주고 근데 우리 저거 말고 아마 돈을 써야 할 이유가 있어요")

josa = ['JKS','JKC','JKG','JKO','JKB','JKV','JKQ', 'JX', 'JC']
noun = ['NNG','NNP']

kiwi = Kiwi()
kiwi.prepare()
t = kiwi.analyze(a[2])[0][0]
t_noun = [w[0] for w in t if w[1] in noun]
new_a = [hgtk.text.decompose(w) for w in t_noun]
# distance 배열
# distance = [0]*(len(f.readlines()))
distance = []

for word in new_a:
    d = []
	f = open(loc+'newExample16.csv','r', encoding='utf-8')
	rdr = csv.reader(f)
	for line in rdr:
		tmp = textdistance.levenshtein(word, line[0])
		num = word.count('ᴥ')
		if tmp < num:
			d.append(hgtk.text.compose(line[0]))
	#print(d)
	distance.append(d)
print(distance)
# 마지막에 수정된 자막에 대한 튜플은 디비 저장 및 클라이언트에 전송될 예정
