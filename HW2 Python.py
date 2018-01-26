#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 15:35:17 2018

@author: marana
"""
#%%
def sumthreefiv(g):
      g =[i for i in range(1,g) if i%5==0 or i%3==0]
      k=sum(g)
      return k
g=100
print (sumthreefiv(g))
#%%2
"""функция очень долго считает для большего члена последовательности, поэтому
ниже предложен альтернативный способ"""
def fibo(f):
    if (f==1):
        return (1)
    if (f==2):
        return (1)
    return (fibo(f-1)+fibo(f-2))
f=10
print(fibo (f))
#%%2
from math import sqrt
def f(n):
    return ((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5))
print (f(10))
#%%4
import pandas
m = "/Users/marana/Downloads/nespython2017hw2-c5da2e89bd854b8726e2e8904098a7a07fed447b/words-list-russian.txt"
df =(pandas.read_table(m, header = None))[0].tolist()
file=open("/Users/marana/Downloads/nespython2017hw2-c5da2e89bd854b8726e2e8904098a7a07fed447b/words-list-russian.txt")
text=file.read()
import itertools 
from itertools import combinations
def anagrams(word):
    for permutation in itertools.permutations(word):
        yield ''.join(permutation)
for word in anagrams('лекарство'):
    if word in text:
        print (word)
#%%5
import pandas
m = "/Users/marana/Downloads/nespython2017hw2-c5da2e89bd854b8726e2e8904098a7a07fed447b/words-list-russian.txt"
t =(pandas.read_table(m, header = None))[0].tolist()
t = [i for i in t if len(i) == 5]
import random
def guessword(list):        
    playing = True
    word = random.sample(t,1)
    guesses = 0
    print (word)
    while playing:
        count = 0
        user_guess = input('Введи слово -')
        if user_guess == 'конец':
            break
        elif user_guess not in t:
            print('нет данного слова')
            continue
        for element in user_guess:
            if element in [i for i in str(word)]:
                count += 1
        guesses += 1
        if count == 5:
            playing = False
            print('Правильно угадали с %s попытки' %guesses)
        else: print(count)
    return word
guessword('t')       
#%%6
import pandas
m = "/Users/marana/Downloads/nespython2017hw2-c5da2e89bd854b8726e2e8904098a7a07fed447b/words-list-russian.txt"
t =(pandas.read_table(m, header = None))[0].tolist()
t = [i for i in t if len(i) == 5]
import random
def pythonguess(list):
    myword = input('загадай слово:')
    playing = True
    guesses = 0
    while playing:
        count = 0
        user_guess = random.sample(t,1)
        print (user_guess)
        continue
    for element in user_guess:
        if element in [i for i in str(myword)]:
            count (i in str (myword))
        guesses+=1
        if count == 5:
            playing = False
            print('Правильно угадали с %s попытки' %guesses)
        else: print ('число совпадающих букв:' %count)
    return word  