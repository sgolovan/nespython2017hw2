#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 17:18:03 2018

@author: alex polyakov
"""
#%%
def sum123(n):
    f = 0
    for i in range(1,n):
        if i % 3 == 0 or i % 5 == 0:
            f = f + i
            print(i)
    return f
# sum123(10000) = 23331668 

#%%      

def fib1(n):
    if (n == 1):
        return(1)
    if (n == 2):
        return(2)
    return(fib1(n-1)+fib1(n-2))
#%%

F = {1:1,2:2} # dictionary  for values

def fib2(n):
    if n in F:
        return F[n]
    F[n] = fib2(n - 1) + fib2(n - 2)
    return F[n]

#%% Task3

f = open("/Users/alenasemanina/Desktop/nespython2017hw2-master/words-list-russian.txt", "r", encoding = "utf-8") 

line = f.readlines()
words = []
wsort = []
Dict = {} 

for elements in line:
    words.append(elements.strip())

for i in words:
    Dict[''.join(sorted(i))] = []
     
for j in words:
    wsort = ''.join(sorted(j))
    if wsort in Dict:
        Dict[wsort].append(j)
    else:
        Dict[wsort] = j
        
for i in Dict:
    if len(Dict[i])>3:
        print(Dict[i])
            
#%% import
import itertools as it

#%% Task 4
#делаем для слова лекарство, поэтому выкинем все слова которые больше чем n-1 символ, почему не n? 
#потому что для слова лекарстов нету аннограм
dict1 = {}
nabor = []

for i in words:
   if len(i) > 9:
       words.remove(i)
       
#смотрим комбинации различных размеров с помощью библиотеки itertools, permulations выдают 
#все возможные комбинации в которые каждая буква входит по одному разу       
s = 'лекарство'      
perm = []
for i in range(len(s)+1):
    for j in it.permutations(s,i):
        #добавляем в пустой лист perm строки с комбинациями букв с помощью append
        perm.append(''.join(j))

for i in words:
    dict1[i] = i
for i in perm:
    if i in dict1:
        nabor.append(i)
        
print(nabor)
print(len(nabor))

#%%
import random
#%% Task 5

all_five = []
game_word = []
letters = []   


playing = True 

#Выбираем слова дял игры из списка слов words из программы 3(пять букв)

for i in words:
    if len(i) == 5:
        all_five.append(i)
#print(all_five)

#Выбираем слово

rand = random.randint(0,len(all_five))
game_word.append(all_five[rand])
print(game_word)

#Разбиваем слово  на буквы

letters.append(list(game_word[0])) #list() разбивает на буквы
#print(letters)
        
# спрашиваем юзера о его слове

while playing:
    a = 0
    guess = input("Enter the word:")
    guess_letters = list(guess)
    if guess_letters != letters[0]:
        for j in set(guess_letters):
            if j in letters[0]:
                a = a+1
        print("угадано : %d" %a)
    else:
        playing = False
        print("You win!")
            
 #%% Task 6   

all_five = []
game_word = []
letters = []   
game_word1 = []

playing = True 

#Выбираем слова дял игры из списка слов words из программы 3(пять букв)

for i in words:
    if len(i) == 5:
        all_five.append(i)
#print(all_five)

while playing:
    game_word = []
    number = 0
    for j in all_five:
        for k in letters:
            if k in list(j):
               game_word1.append(j) 
    rand = random.randint(0,len(all_five))
    game_word.append(all_five[rand])
    print(game_word)
    number = input("Число совпад:")
    if number != '6':
        if number != 0:
            letters.append(list(all_five[rand]))
            
    else:
        playing = False
        print("Победа!")   
            
#%% Task 7

import re
import urllib.request
from bs4 import BeautifulSoup

#%%
url = 'http://www.belstat.gov.by/ofitsialnaya-statistika/makroekonomika-i-okruzhayushchaya-sreda/natsionalnye-scheta/godovye-dannye_11/proizvodstvo-valovogo-vnutrennego-produkta/'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser') #class object creation

tags = soup.find_all('p')

#pattern = '.*\/active\/researchers\/contact.*'
#tags = soup.find_all('a', href=re.compile(pattern))


pattern=[]
for i in tags:
    pattern.append(re.findall(r'\d+|[А-Яа-я]+',str(i)))

for i in pattern:
    if len(i) == 0 and i == '':
        pattern.remove(i)
        
    





   
                        
    
    
   
    


