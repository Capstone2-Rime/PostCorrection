import hgtk
import textdistance
import os
import csv
import pandas as pd
import time
# 격조사, 접속조사 (무조건 단어 뒤에 붙어어있음)
josa1_high = ['에서', '에게서', '께서', '를', '에게', '는', '랑', '께서', '이에게', '이하고']
# low: 길이별로
josa1_low1 = ['의', '가', '을', '은', '와', '과', '나', '이', '며']
josa1_low2 = ['에다', '하고', '이가', '이는', '이랑', '이나', '이와', '이며']
# 보조사
# 무조건보조사
josa2_high = ['까지', '만큼', '이라도', '커녕', '부터', '이나마']
josa2 = ['만', '도', '마저', '나마', '마다', '라도', '치고']
# 서술격조사 : 마침표 찍는용
josa3_s0 = ['다', '요']
josa3_s = ['하다', '에요', '죠', '지요']
#이게 있으면 무조건 서술어
josa3_sb = ['ㅇㅣᴥㄷㅏ', 'ㅂᴥㄴㅣᴥㄷㅏ', 'ㄹᴥㄲㅏ', 'ㅆᴥㄷㅏ', 'ㅆᴥㅅㅗ', 'ㄴᴥㄷㅏ', 'ㄶᴥㄷㅏ', 'ㅆᴥㅇㅓᴥㅇㅛ', 'ㅆᴥㅈㅛ'] 

def bojung(a):
    inittime = time.time()
    a_split = a[2].split()              # a_split에는 띄어쓰기별 단어 저장됨
    n = []
    stopfile = './stopword_post.csv'
    stopdata = pd.read_csv(stopfile, encoding='cp949')
    stopset = list(stopdata.stopword)
    
    for word in a_split:
        d = []
        f = open('./newExample16.csv','r', encoding='utf-8')
        rdr = csv.reader(f)
        new_word = word
        j = ''
        geok_flag = 0
        flag = 0
        # stopset 검사
        if word in stopset:
            #print("원본그대로 stopword")
            flag=1
            n.append(word)
        if flag:
            continue
        # 조사 여부 검사
        # 서술격조사(확률높은) 확인
        for josa in josa3_sb:
            if josa in hgtk.text.decompose(word):
                flag=1
                n.append(hgtk.text.compose(word)+'.')
                break
        if flag:
            continue
        # 격조사(확률높은) 확인
        for josa in josa1_high:
            if josa in word:
                #print('확률높은격조사')
                idx = word.index(josa)
                new_word = word[:idx]
                j = word[idx:]
                geok_flag = 1
                break
        # print('격조사1: ', time.time()-inittime)
        if not geok_flag:
            if len(word)>1:
                for josa in josa1_low1:
                    if word[-1]==josa:
                        new_word = word[:-1]
                        j = josa
                        geok_flag = 1
                        break
        # print('격조사2: ', time.time()-inittime)
        if not geok_flag:
            if len(word)>2:
                for josa in josa1_low1:
                    if word[-2]==josa:
                        new_word = word[:-2]
                        j = josa
                        geok_flag = 1
                        break
        # 조사제거후 stopset검사
        if new_word in stopset:
            #print('조사제거후 stopset')
            flag=1
            n.append(word)
        if flag:
            continue

        if geok_flag:
            wordlen=len(new_word)
        else:
            wordlen = len(word)      
        word = hgtk.text.decompose(new_word)     
        # csv 파일 한줄씩 접근해서 작은값 넣기
        for line in rdr:
            if abs(wordlen-len(line[0]))<2:
                if word[0] == line[1][0]:
                    tmp = textdistance.levenshtein(word, line[1])
                    num = word.count('ᴥ')
                    if tmp < num:
                        d.append((tmp, line[0]))
        # 최솟값에 해당하는 단어를 n에 넣음
        if d:
            word = min(d)[1]+j
            n.append(word)
        else:
            n.append(hgtk.text.compose(word)+j)
        #print(n)
        # print('append: ', time.time()-inittime)
    print('소요시간: ', time.time()-inittime)
    return ' '.join(n)

# db에서 데이터를 튜플 형태로 받아왔다고 가정
#a=("14:24:20","lyj","구로피우스는 모더니즘을 대표하는 독일의 건축가이다 바우하우스의 창립자이다")
#a=("14:24:23","kyh","스패인 알카싸르에서 이술람 양식을 엿볼 수 있습니다")
#a=("14:24:26","byh","색상완은 가시강선의 스팩트럼을 고리형태로 연결하여 색을 배열한 것을 말합니다")
a4=("14:24:30","osh","태피스트리는 고대 이집스를 비롯하여 중세 초기의 페르샤를 중심으로 화려한 작품이 많이 나왔는데")
a5=("14:24:32","osh","가브리앨은 미가엘처럼 유대교와 기독고, 그리고 이슬람교에서 중요한 위치를 차지한다")

print('Initial   : ', end='')
print(a4)
print('Corrected : ', end='')
print(bojung(a4))
print("\n")
print('Initial   : ', end='')
print(a5)
print('Corrected : ', end='')
print(bojung(a5))