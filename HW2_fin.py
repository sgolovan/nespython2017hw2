#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 18:11:56 2018

@author: khankishialiev
"""
#%%
#Task 1
def sumThreeFive(n):
    s=0
    i=1
    while (i<n):
        if ((i % 5 == 0) or (i % 3 == 0)):
            s=s+i
        i=i+1
    return(s)
#%%
#Task 2
Dict = {1: 1, 2: 2}

def fib(n):
    if n in Dict:
        return Dict[n]
    Dict[n] = fib(n - 1) + fib(n - 2)
    return Dict[n]
#%%
#Task 3
def otkr(s):
    f = open(s, 'r')                   #Открыли файл
    l = [line.strip() for line in f]    #создали list и каждую строки удалили от пробельных символов
    f.close()   #закрыли файл
    return(l)        
#%%
def anagrammas(s):     
    l = otkr(s)     #открыли файл с помощью otkr
    print(len(l))
    ClassDict = {}  #пустой словарь

    for line in l:
        a = list(line)      #сделали строки списком букв
        a.sort()            #отсортировали
        b = ''.join(a)      #сделали из отсортированного списка снова str
        if b in ClassDict:
            ClassDict[b].append(line)       #если ключ такой есть в словаре, то добавляем в список под этим ключом новое слово
        else:
            ClassDict[b] = [line]           #если нет, создаем под этим ключом новый список из этого слова
            
    keys = dict.keys(ClassDict)         #создали список ключей
    i=1
    for key in keys:            
        if len(ClassDict[key])>=4:          #если длина списка больше 4
            print("Class ", i, " - ",key, ": ", ClassDict[key])        #вывести его на экран
            i += 1
            
    return(ClassDict)               #return для запуска Task4. Если необходимо проверить Task3, нужно воспользоваться пустым return()
    #return()   #ДЛЯ ПРОВЕРКИ ЗАДАЧИ 3
#%%
#Task 4
def task4(s, stroka):
    l = anagrammas(s)           #выгрузили словарь с анаграммами
    keys = dict.keys(l)         #создали список ключей словаря
    a = list(stroka)            
    a = set(a)                  
    wordcount=0                 #счетчик слов
    for key in keys:
        b = set(list(key))      
        if b<=a and (len(b) == len(key)):   #если наш ключ лежит как подмножество в слове и длина совпадает(множество не замечает повторы, а они важны)
            for i in range(len(l[key])):
                print(l[key][i])            #значит составить слово можно
            wordcount = wordcount + len(l[key])     #количество слов увеличили
    print(wordcount, " слов")
    return()
#%%
#Task 5
def task5(s):
    import random
    l = otkr(s)
    l = [line for line in l if (len(line) == 5) and (len(set(line)) == len(line))]   #выбрали только слова из 5 букв с различными буквами
    i = int(random.random()*(len(l)-1))         #генерируем случайное число, которое задаст нам номер загаданного слова из файла
    secret = l[i]                           
    print('Подсказка: ', secret)                #подсказка, чтобы легко угадать ответ
    print('Для выхода напечатайте q')
    ssecret = set(secret)
    count = 0
    Flag=-1                                     #Flag даст нам возможность выйти из цикла
    while Flag != 1:
        print('Введите слово: ')
        guess = input()
        if guess == 'q':                        #возможность выхода досрочно
            Flag = 1
            return('Спасибо за игру')
        while Flag == -1:
            if len(guess)!=5:                   #проверка на то, чтобы слово было из 5 букв
                print('Введите слово длины 5: ')
                guess = input()
                Flag = -1
            else:
                Flag = 0
        count += 1
    
        if guess == secret:     #угадали
            print('Bingo!')
            Flag = 1
            return('Вы угадали с ', count, ' попытки')
        
        lguess = list(guess)
        nummatch = 0                #счетчик количества совпадений
        for j in range(len(guess)):
            if set(lguess[j]) <= ssecret:
                nummatch += 1
        print('Количество совпадений: ', nummatch)
        Flag = -1
    
    return(0)
#%%
#Task 6
def task6(s):
    import random
    l = otkr(s)
    l = [line for line in l if (len(line) == 5) and (len(set(line)) == len(line))] 
    counter = [k for k in range(len(l))]    #вспомогательный массив, чтобы комп выбирал разные слова, пока они не закончатся
    print('Загадайте слово: ')
    secret = input()
    ssecret = set(secret)
    Flag = -1
    count = 0
    while Flag == -1:
            if len(secret) != 5:
                print('Введите слово длины 5: ')
                secret = input()
                Flag = -1
            else:
                Flag = 0
            if len(secret) != len(set(secret)):
                print('Слово должно состоять из разных букв: ')
                secret = input()
                Flag = -1
            else:
                Flag = 0

    while Flag != 1:
            nummatch = 0
            if counter == []:
                return('Такого слова я не знаю')
            i = random.choice(counter)          #случайное число из списка counter
            guess = l[i]
        #if set([guess]) <= GuessSet:
         #   Flag = -1
          #  if len(GuessSet) == len(l):
           #     Flag = 1
            #    return('Такого слова я не знаю')
        #else:
            counter.remove(i)                   #удалить выбранное слово из списка, чтобы его больше не повторять
            print(guess)
            lguess = list(guess)
            #GuessSet.add(guess)
            count += 1
            if guess == secret:
                print('Bingo!')
                print('Угадала за ', count, ' попыток')
                Flag = 1
                return('Конец игры')
            for j in range(len(guess)):
                if set(lguess[j]) <= ssecret:
                    nummatch += 1
            print('Количество совпадений: ', nummatch)
            print('Попытка ', count)
            Flag = -1
#%%
#Task 7
#%%
import re
import urllib.request
from bs4 import BeautifulSoup
url = 'http://www.belstat.gov.by/ofitsialnaya-statistika/makroekonomika-i-okruzhayushchaya-sreda/natsionalnye-scheta/godovye-dannye_11/proizvodstvo-valovogo-vnutrennego-produkta/'
html = urllib.request.urlopen(url).read()       #прочитали html-код с сайта
soup = BeautifulSoup(html, 'html.parser') #class object creation
    
tags = soup.find_all('div',  {"class": "table"})    #выкачали таблицу
#for i in tags:ta
#print(tags)
tags[0].get_text()              #выкачали текст из таблицы

b = tags[0].get_text()
b = re.sub('[\t\n]',' ', b)     #убираем все символы табуляции и возврата каретки и заменяем их на пробелы
b = re.sub('\xa0','', b)        #убираем экзотический символ разделения числа по 3
c = list(b)
Flag = 0
count = 0
for i in range(len(c)):
    if c[i] == ' ':             #первый пробел не трогаем
        if Flag == 0:
            Flag == 1
            count = 1
        else:
            count += 1              
            if count == 2:          #второй пробел будет везде табуляцией
                c.insert(i, '\t')
            if count > 2:
                c.insert(i, '\n')   #остальные пробелы удалим потом. пока \n
    elif Flag == 1:
        if count == 1:          #пробел был 1 - ничего не делаем
            Flag = 0
        elif count == 2:
            c.insert(i, '\t')   #пробелов было 2 - 2-ой заменяем на \t
        else:
            count = 0
b = ''.join(c)          #делаем текст снова строкой
b = re.sub('\n','', b)     #убираем временные \n
b = re.sub(',','.', b)      #заменяем запятые на точки
b = re.sub('2 0','20', b)   #один разделитель числа оказался просто пробелом, поэтому меняем вручную
print(b)
#%% 
        
            
        
    
    
    
    
    
    
    
    
        
        
        