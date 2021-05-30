import hgtk
import textdistance
import os
import csv
from kiwipiepy import Kiwi
#loc = "/home/yjlee/capstone_m/"

# db에서 데이터를 튜플 형태로 받아왔다고 가정
a=("14:24:23","kyh","경복꿍에서만이라도 안경의 몬유도원도를 봤고 행복해서 알테피나코택을 생각했다")
#a=("14:24:28","kyh","그냥 끄는 법이 주고 근데 우리 저거 말고 아마 돈을 써야 할 이유가 있어요")

# a_split에는 띄어쓰기별 단어 저장됨
a_split = a[2].split()

josa = ['JKS','JKC','JKG','JKO','JKB','JKV','JKQ', 'JX', 'JC']
noun = ['NNG','NNP']
eomi = ['EP', 'EF' 'ETN', 'ETM', 'XSV', 'XSA']

# t에는 a_split 요소별 품사분류된 결과가 저장됨
kiwi = Kiwi()
kiwi.prepare()
t=[]
for i in a_split:
	t.append(kiwi.analyze(i)[0][0])
# 처리한 어절을 각각 담을 리스트 sentence
sentence = []
# t 요소별 수정
for i in range(len(t)):
	flag = 0
	# 어절별 처리를 위한 리스트 n
	n = []
	# j는 품사 탐색 index
	for j in range(len(t[i])):
		if t[i][j][1] in eomi: # 어미가 있는 경우 원본 단어를 n에 넣음
			flag = 1
			sentence.append(a_split[i])
			break
		elif t[i][j][1] in noun: # 명사일때
			# csv 탐색하며 저장할 리스트 d
			d = []
			f = open('./newExample16.csv','r', encoding='utf-8')
			rdr = csv.reader(f)
			word = hgtk.text.decompose(t[i][j][0])
			for line in rdr: # csv 파일 한줄씩 접근해서 작은값 넣기
				tmp = textdistance.levenshtein(word, line[0])
				num = word.count('ᴥ')
				if tmp < num:
					d.append((tmp, hgtk.text.compose(line[0])))
			if d: # 최솟값에 해당하는 단어를 n에 넣음
				n.append(min(d)[1])
		else: #나머지는 수정 없이 단어 n에 바로 넣기
			n.append(t[i][j][0])
	if flag==0:
		sentence.append(''.join(n))
final = ' '.join(sentence)

print('Initial   : ', end='')
print(a)
print('Corrected : ', end='')
print(final)