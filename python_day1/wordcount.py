#!/usr/bin/python
file=open("C:\Users\s.yadav.voddepalli\Downloads\Mangroves.txt","r+")
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for k,v in wordcount.items():
    print k, v