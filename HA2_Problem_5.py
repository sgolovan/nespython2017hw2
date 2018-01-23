import pandas as pd
import random

df = pd.read_csv('words-list-russian.txt', encoding='utf-8', names=['words'])

fullList = []
myList = []
for i in df['words']:
    if len(i) == 5:
        if len(set(i)) == 5:
            myList.append(i)
            fullList.append(i)
        else:
            fullList.append(i)

length = len(myList)
rand = myList[random.randint(0, length)]
randSet = set(rand)
n = 0  # number of tries
print(rand)
for i in range(10):
    print('//')  # чтобы заранее не спалить слово:)
while True:
    n += 1
    print('Введите слово: ', end='')
    a = input()
    if a == rand:
        print('!')
        print('Угадали с попытки номер', n)
        break
    elif a in fullList:
        letters = 0
        for j in randSet:
            m = a.count(j)
            letters += m
        print(letters)
        #  print(len(randSet & set(a)))
    else:
        print('Не знаю такого слова')
