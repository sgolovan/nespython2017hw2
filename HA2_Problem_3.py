import pandas as pd


def anagr(a):
    aa = []
    n = 0
    for i in range(1, len(a)):
        if a[i][0] == a[i - 1][0]:
            aa.append(a[i - 1][1])
            n += 1
        elif n > 2:
            aa.append(a[i - 1][1])
            print(aa)
            aa = []
            n = 0
        else:
            aa = []
            n = 0


df = pd.read_csv('words-list-russian.txt', encoding='utf-8', names=['words'])

myWords = [i for i in df['words']]
mySplite = [list(i) for i in df['words']]
[i.sort() for i in mySplite]
myJoin = [''.join(i) for i in mySplite]
myLove = list(zip(myJoin, myWords))
myLove = sorted(myLove, key=lambda x: (len(x[0]), x[0]))
anagr(myLove)
