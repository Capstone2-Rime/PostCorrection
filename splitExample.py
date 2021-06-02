import os
import csv
import hgtk

loc = "C:/Users/이윤정/Desktop/회의록보정/"

# read
f = open(loc+'example16.csv','r', encoding='euc-kr')
ff = open('./stopword_post.csv','r', encoding='cp949')
rdr = csv.reader(f)
rrdr = csv.reader(ff)
f1 = open(loc + 'newExample16.csv','w', newline='', encoding='utf-8')
ff1 = open('./newStopword_post.csv','w', newline='', encoding='utf-8')
wr = csv.writer(f1)
wrr = csv.writer(ff1)
for line in rdr:
    word = hgtk.text.decompose(line[0])
    wr.writerow([line[0], word])
for line in rrdr:
    word = hgtk.text.decompose(line[0])
    wrr.writerow([line[0], word])
f.close()
f1.close()