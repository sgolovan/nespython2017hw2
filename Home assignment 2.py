# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 23:35:00 2018

@author: rkorotchin
"""

#%%
"""Task #1."""

def count(N):
    Sum = 0

    for i in range(1, N):
        if ( i % 3 == 0 ) or ( i % 5 == 0 ):
            Sum = Sum + i
        #print(i)
        #print(Sum)
    return(Sum)

N = 10000
print(count(N))

#%%
"""Task 2"""

def memorize(func):
    def g(N, memory = {1 : 1, 2 : 2}):
        r = memory.get(N)
        if r is None:
             r = func(N)
             memory[N] = r
        return r
    return g

@memorize
def Fibo(N):
    return Fibo(N - 1) + Fibo(N - 2)

N = 200
print(Fibo(N))

#%%
"""Task 3"""

import pandas
name = "words-list-russian.txt"
df = (pandas.read_table(name, header = None))[0].tolist()

def AnagramDiverse(String):
    Anagram = {}

    for i in String:

        if len(i) >= 1:
            List_new = list(i)
            List_new.sort()
            String_new = ''.join(List_new)

            if String_new in Anagram:
                Anagram[String_new].append(i)
            else:
                Anagram[String_new] = [i]
    
    for i in dict.keys(Anagram):
        if len(Anagram[i]) >= 4:
            print(i, ": ", ' '.join(Anagram[i]))
#    print(Anagram['ааклн'])
    return()

AnagramDiverse(df)

#%%
"""Task 4"""
import pandas
#import itertools
#from itertools import combinations_with_replacement

name = "words-list-russian.txt"
df = (pandas.read_table(name, header = None))[0].tolist()

def TypeSetter(String):
    Anagram = {} 

    for i in df:

        if len(i) >= 1:
            List_new = list(i)
            List_new.sort()
            String_new = ''.join(List_new)

            if String_new in Anagram:
                Anagram[String_new].append(i)
            else:
                Anagram[String_new] = [i]
    
    String_new = list(String)
    String_new.sort()
    
    Number = 0
    for i in dict.keys(Anagram):
        K = list(i)
        K.sort()

        a = list(set(K) & set(String_new))

        if len(a) == len(K):
            print(i, ": ", ' '.join(Anagram[i]))
            Number += len(dict.get(Anagram, i))
            
    print("Количество слов = ", Number)
    return()

TypeSetter('лекарство')

#%%
"""Task 5"""
import pandas
import random
name = "words-list-russian.txt"
df = (pandas.read_table(name, header = None))[0].tolist()

def WannaPlay(String):
    Anagram = {}
    Number = 0
    
    for i in df: 
        if len(i) >= 5:
            Number += 1
            
            List_new = list(i)
            List_new.sort()
            String_new = ''.join(List_new)

            if String_new in Anagram:
                Anagram[String_new].append(i)
            else:
                Anagram[String_new] = [i]
        
    NumberRandom = random.randint(1 , Number)
    
    NumberCount = 0
    Word = ""
    
    for i in dict.keys(Anagram):
        NumberCount += 1
        if NumberCount == NumberRandom:
            Word = ' '.join(Anagram[i])
    
#    print(Word)
    playing = True
#    number = 1
    
    guesses = 0
    
    while playing:
        user_guess = input("Введите слово\n")
        if user_guess == "Выход":
            break
        
        guesses += 1
#        number +=1
        
        Peresechenie = list(set(user_guess) & set(Word))
        
        if user_guess == Word:
            playing = False
            print('Угадали с попытки %s' % guesses)
        else:
            Observations = len(Peresechenie)
            print('Вы верно угадали %s' % Observations, "буквы.")

    return()

WannaPlay(df)
#%%
"""Task 6"""

import pandas
#import random
name = "words-list-russian.txt"
df = (pandas.read_table(name, header = None))[0].tolist()

def WannaPlayWithCo(String):
    Anagram = {}
    Number = 0
    
    for i in df: 
        if len(i) >= 5:
            Number += 1
            
            List_new = list(i)
            List_new.sort()
            String_new = ''.join(List_new)

            if String_new in Anagram:
                Anagram[String_new].append(i)
            else:
                Anagram[String_new] = [i]
        
    NumberRandom = random.randint(1 , Number)
    
    NumberCount = 0
    Word = ""
    
    for i in dict.keys(Anagram):
        NumberCount += 1
        if NumberCount == NumberRandom:
            Word = ' '.join(Anagram[i])
    
    playing = True
    
    guesses = 0
#    Count = 0
#    Ugadano = {}
    
    while playing:
#        print(Ugadano)
        print("Вы загадали слово %s", Word, "?")
        user_guess = input("Введите количество угаданных букв:\n")
#        user_guess = int(user_guess)
        
#        if user_guess > 0:
#            Ugadano[Word] = user_guess
#            Count += 1
            
        guesses += 1
        
        if user_guess == "Да!":
            playing = False
            print('Угадали с попытки %s' % guesses)
        else:
#        Word = RandSelect(Anagram)
            

            Word = list(Word)
            Word.sort()
            Word = ''.join(Word)
            
            AnagramAfter ={}
            
            if len(dict.keys(Anagram)) == 0:
                print("Я не знаб такого слова!")
                playing = False
                break
            
            
            for i in dict.keys(Anagram):
                Peresechenie = list(set(Word) & set(i))
                if len(Peresechenie) <= int(user_guess):
                    AnagramAfter[i] = Anagram[i]
            
            
            Anagram = AnagramAfter
            Word = RandSelect(Anagram)
               
    return()

def RandSelect(Anagram):
    Number = len(dict.keys(Anagram))
    
    NumberRandom = random.randint(1 , Number)
    
    NumberCount = 0
    Word = ""
    
    for i in dict.keys(Anagram):
        NumberCount += 1
        if NumberCount == NumberRandom:
            Word = ' '.join(Anagram[i])
            
    return(Word)
WannaPlayWithCo(df)
#%%
"""Task 7"""
import urllib.request
from bs4 import BeautifulSoup
url = 'http://www.belstat.gov.by/ofitsialnaya-statistika/makroekonomika-i-okruzhayushchaya-sreda/natsionalnye-scheta/godovye-dannye_11/proizvodstvo-valovogo-vnutrennego-produkta/'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser') #class object creation

table = soup.find('table', attrs={'class':'autotbl nohead'})
table_body = table.find('tbody')
data=[]
rows = table_body.find_all('tr')
for i in rows:
    year = i.find_all('th')
    year = [ele.text.strip()  for ele in year]
    if year!=[]:
        data.append(year) 
        
for i in rows:
    gdp = i.find_all('td')
    gdp = [ele.text.strip() for ele in gdp]
    data.append(gdp) 
data.pop(1)


for i in range(len(data)):
       for k in range(len(data[i])):
           data[i][k]=data[i][k].replace('\n\t\t\t\t','')
           data[i][k]=data[i][k].replace('\xa0','')
#           
for i in range(len(data)):
       for k in range(len(data[i])-1):
           n=k+1
           data[i][n]=data[i][n].replace(' ','')
           data[i][n]=data[i][n].replace(',','.')    
  
import numpy as np
d=np.array(data)
for i in d:
    print(*i, sep='\t')
