#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 23:51:12 2018

@author: silis123
"""

#%% 
#Задание 1
def sumThreeFive(n):
    ThreeFives = (3, 5, 15) # определяем набор чисел, которые нам интересны для деления. 15 нужно для того, чтобы это вычесть и не считать 2 раза
    IntDiv = [(n-1) // TF for TF in ThreeFives] #смотрим целочисленное деление
    S = [ID*TF*(1+ID)/2 for ID,TF in zip(IntDiv, ThreeFives)] #арифметическая прогрессия из ID и TF из zip с наборами, которые опираются на 3,5, 15
    a = (S[0] + S[1] - S[2]) #вычитаем лишнее пересечени по 15 (3+5+2*15-15)
    b = int(a) #переводим число в класс int, тк в примере, судя по всему, класс int
    return b

print(sumThreeFive(10000)) #23331668
#%% 
#Задание 2
def dibo(n): #здесь определяем функцию для подсчёта фибоначчи
      if n in hs: #здесь начинаются итерации
          return hs[n]
      hs[n] = dibo(n-1) + dibo(n - 2) #сама формула для расчёта последовательности   
      return hs[n]

def fibo(n): 
    hs = {1: 1, 2: 2}   # создаем внешнее хранилище промежуточных результатов, чтобы сократить время работы кода в корень из n раз
    print (dibo(n))
    
fibo(200) #453973694165307953197296969697410619233826
#%% 
#Задание 3
import pandas
def splitbylettersnumber(file): #функция для разделения списка слов на группы по количеству букв
    name = file
    df = (pandas.read_table(name, header = None))[0].tolist() #читаем файл
    d={}
    for word in df:
        Length = len(word) #определяем длину слова в df

        d.setdefault(Length, []).append(word) #вносим слова по группам в словарь d
    result=[d[n] for n in sorted(d, reverse=False)]
    return result

def comparison(spisok): #функция для сравнения количества слов в классах с 4
    UsedWord = [False for i in range(len(spisok))]  #обозначаем, что все слова у нас ещё не были использованы/проверены
    CopiedWords = [] # лист для вывода слов по классам
    for j, word in enumerate(spisok): #spisok[j] = word
        if UsedWord[j] == True: #проверяем, использовали ли мы уже это слово
            continue
        
        else: 
            SortedWord = sorted(word)  #сорируем по буквам слово
            for i, AnotherWord in enumerate(spisok):#spisok[i] = AnotherWord
                if UsedWord[i] == True: #если это слово мы проверили, то оно нам не интересно
                    continue
                AnotherSortedWord = sorted(AnotherWord) #сортируем следующее слово из класса
                if AnotherSortedWord == SortedWord: #если у нас слова равны, то вешаем ярлык true и аппендим в наш лист
                    UsedWord[i] = True
                    CopiedWords.append(AnotherWord)
            if len(CopiedWords)>=4: #непосредственно сравнение длины листа слов с 4
                print(CopiedWords) #вывод листа
            CopiedWords = [] # очищаем лист
            
def anagrams(n): #команда для задания
    a = splitbylettersnumber (n) #задаем переменную а для дальнейшего поиска классов
    for i in a:
        if comparison (i)==None:
            continue
        print (comparison(i)) # вывод списка
        
anagrams("words-list-russian.txt") #7 классов
#%% 
#Задание 4
import pandas #импортирую пандас и каунтер, потому что это позволит проще сделать задание
from collections import Counter
def typesetter(wordlist, word): #определяем команду для выполнения задания
    name = wordlist  
    df = (pandas.read_table(name, header = None))[0].tolist() #открываем текстовый файл
    b = sorted(word) # сортируем слово, для которого необходимо найти анаграммы
    count = 0 # делаем счётчик для того, чтобы можно было сразу определить количество выведенных слов
    for i in df:
        a = sorted(i) #сортируем каждое слово в листе df
        nf = Counter(a) & Counter(b) # ищем пересечение сетов с дупликатами
        if len(a) > len(b): # отбрасываем слова, которые длиннее заданного word
            continue
        else:
            if sum(iter(nf.values())) == len(a): #сравниваем длину отсортированного слова из списка и размер пересечения (с учетом наименования букв)
                count+=1 #прибавляем счетчик
                print(count, i) #выводим номер слова и само слово из списка, которое является анаграммой
typesetter("words-list-russian.txt", 'лекарство')
#%% 
#Задание 5
import pandas
import random
from collections import Counter

playing = True #вешаю флажок для игры
guesses = 0 #начальное значения счетчика для определения количества попыток
def outputrandom5(file): #команда, которая будет вызывать рандомное слово из 5 букв из нашего текстового файла
    name = file
    df = (pandas.read_table(name, header = None))[0].tolist()
    d={}
    for word in df: #делим на классы по кличеству букв
        Length = len(word)
        d.setdefault(Length, []).append(word)
    result=d[5]  #выбираем класс из 5 букв
    rm = random.choice(result) #выбираем случайное слово
    return rm

wordlist = open("words-list-russian.txt", "r", encoding="UTF-8") # открываю ещё раз список слов, потому что нужно разделить его на линии для дальшейшего использования
lines = wordlist.read().splitlines()

a = outputrandom5('words-list-russian.txt') #фактически, начало игры. выбор рандомного слова
print ('Сыграем в "отгадай слово!" Я загадываю слово из 5 букв, а Вам нужно его угадать') 
print ('Подсказка: правильное слово: ' + a) #на всякий случай вывожу правильное слово, чтобы было удобнее проверять

while playing: #начало цикла игры
    user_guess = input('Предложите слово из 5 букв!\n') #здесь необходимо ввести свою догадку
    if user_guess == 'стоп': #ставлю спорно
        break
    sortedinput = sorted(user_guess) #сотируем по буквам загаданное слово 
    sortedrandom = sorted(a) #сортируем по буквам рандомное слово из списка
    lettermatch = Counter(sortedrandom) & Counter(sortedinput) #ищем пересечение с дупликатами
    guesses +=1 #прибавляем счетчик
    if sum(iter(lettermatch.values())) == 5 and a==user_guess: #условие завершения игры: пересечение =5, и загаданное слово совпадает со случайным
        playing = False #завершаем игровой цикл
        print('!')
        print('Угадали с попытки номер %s' %guesses) 
    elif sum(iter(lettermatch.values())) == 5 and a!=user_guess: #условие, которое покажет, что все буквы верны, но их расположение неверно
        print('Теперь попробуйте другие комбинации букв!')
    elif len(user_guess)!=5: # условие для отказа работы с непятисимвольной вводимой информацией
        print("Ошибка: введите слово из 5 букв")
    elif user_guess not in lines: #необходимое условие для того, чтобы угадывающий обращался только к словам из списка. Зачем - не понятно, но так хотят по условию
        print('Ошибка: я не знаю такого слова')
    else: 
        print('Вы угадали %s букв из 5!' %sum(iter(lettermatch.values()))) #если все ограничения не срабатывают, то пишем количество совпавших букв и оправляем в начало
#%% 
#Задание 6
import pandas

def output5(file): #вытаскиваем пятибуквенные слова для дальнейшей работы. Более подробное описание было выше
    name = file
    df = (pandas.read_table(name, header = None))[0].tolist()
    d={}
    for word in df:
        Length = len(word)
        d.setdefault(Length, []).append(word)
    result=d[5]
    return result

a = output5('words-list-russian.txt') #задаем переменную для работы с функцией
playing = True # вешаем флажок для начала игрового цикла
guesses = 0 #обозначаем что значение попыток равно пока что нулю
print('Введите слово из 5 букв, и я его угадаю.')
print('Начинаю угадывать')


while playing:
    if guesses == len(a): #необходимое условие, которые завершает работу игры после проверки всех слов из доступного словаря
            print ('Я не знаю такого слова')
            break
    user_input = input('Введите слово из 5 букв:') # здесь пользователь вводит слово, которое будет отгадывать компьютер
    if user_input == 'стоп': #стопор для выхода из игры
        break
    if len(user_input)!=5: #уловие для отказа работы с непятисимвольной вводимой информацией
        print('Ошибка: длина слова должна составлять 5 букв')
        continue
    else:
        sortedinput = sorted(user_input) #сортируем введённое слово
    
    for i in a: # для каждого слова из списка слов по 5 букв
        guesses +=1  #увеличение счетчика
        sortedguess = sorted(i) #сортируем слово из текстового файла 
        lettermatch = Counter(sortedguess) & Counter(sortedinput) #ищем пересечения с input с учетом дупликатов
        
        if sum(iter(lettermatch.values())) == 5 and i==user_input: #условие завершения игры. Объяснение было в 5 задании
            
            playing = False
            print(i) #вывод верного слова
            print('!')
            print('Я угадала с попытки номер %s' %guesses)
            break
        elif sum(iter(lettermatch.values())) <= 5 and i!=user_input: #условие, которое выводит количество совпавших букв в неверном слове из списка
            print (i) #вывод неверного слова
            print('Введите число совпадающих букв: %s ' %sum(iter(lettermatch.values()))) #автоматизация вывода числа совпавших букв
#%% 
#Задание 7
import urllib.request
from bs4 import BeautifulSoup
url = 'http://www.belstat.gov.by/ofitsialnaya-statistika/makroekonomika-i-okruzhayushchaya-sreda/natsionalnye-scheta/godovye-dannye_11/proizvodstvo-valovogo-vnutrennego-produkta/' #ввод рабочего адреса
html = urllib.request.urlopen(url).read() #открытие html кода
soup = BeautifulSoup(html, 'html.parser') #class object creation

table = soup.find('table', attrs={'class':'autotbl nohead'})  # поиск в html атрибута table
table_body = table.find('tbody') #поиск тела таблицы
data=[] #лист для дальнейшей работы
rows = table_body.find_all('tr') #поиск строк по атрибуту tr
for i in rows:
    year = i.find_all('th') #поиск информации по атрибуту th
    year = [element.text.strip()  for element in year] #поиск по элементам в информации по атрибуту th
    if year!=[]: #условие, которое добавляет данные по атрибуту th в data
        data.append(year) 
        
for i in rows:
    gdp = i.find_all('td')#поиск информации по атрибуту td
    gdp = [element.text.strip() for element in gdp] #поиск по элементам в информации по атрибуту td
    data.append(gdp)  #добавляем значения data
data.pop(1)


for i in range(len(data)):# замена символов новой строки и табуляции на ничего, очистка от \xa0 - пробелов
       for k in range(len(data[i])):
           data[i][k]=data[i][k].replace('\n\t\t\t\t','')
           data[i][k]=data[i][k].replace('\xa0','')
#           
for i in range(len(data)):# замена пробелов на ничего и запятых на точки
       for k in range(len(data[i])-1):
           n=k+1
           data[i][n]=data[i][n].replace(' ','')
           data[i][n]=data[i][n].replace(',','.')
  
import numpy as np 
d=np.array(data) #объединяем в один блок
for i in d:
    print(*i, sep='\t') #построчный вывод с очисткой от лишних скобок. разделяем ячейки табуляцией