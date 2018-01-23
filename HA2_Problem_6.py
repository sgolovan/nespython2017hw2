import pandas as pd
import random


def check(ww, nw):
    for m in range(len(ww)):
        if not len(set(nw) & set(ww[m][0])) == ww[m][1]:
            return False
    return True


df = pd.read_csv('words-list-russian.txt', encoding='utf-8', names=['words'])

myList = []
for i in df['words']:
    if len(i) == 5 and len(set(i)) == 5:
        myList.append(i)

length = len(myList)
rand = myList[random.randint(0, length)]
randSet = set(rand)

print('Начинаю угадывать')
k = 1  # кол-во попыток
t = 1  # для цикла while
fw = myList[0]
print(fw)
print('Введите число совпадающих букв: ', end='')
a = input()
if a == '!':
    print('Я угадала с попытки номер', k)
else:
    ww = [(fw, int(a))]
    for j in range(1, length):
        nw = myList[j]
        if check(ww, nw):
            print(nw)
            print('Введите число совпадающих букв: ', end='')
            k += 1
            a = input()
            if a == '!':
                print('Я угадала с попытки номер', k)
                break
            ww.append((nw, int(a)))
            fw = nw
        elif j == length - 1:
            print('Загаданное слово не соответсвует правилам или не находится в списке')
