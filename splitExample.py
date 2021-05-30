import os
import csv
import hgtk

loc = "C:/Users/이윤정/Desktop/회의록보정/"

# read
f = open(loc+'example16.csv','r', encoding='euc-kr')
rdr = csv.reader(f)
f1 = open(loc + 'newExample16.csv','w', newline='', encoding='utf-8')
wr = csv.writer(f1)
for line in rdr:
    #print(line[0])
    word = hgtk.text.decompose(line[0])
    wr.writerow([word])
f.close()
f1.close()