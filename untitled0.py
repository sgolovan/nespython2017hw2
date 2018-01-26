#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 12:45:09 2018

@author: macbook
"""

#%%
#1 Task

def sumThreeFive(n):
    total_sum = 0
    for i in range(0,n):
        if (i % 3 == 0) or (i % 5 == 0):
            total_sum = total_sum + i
    print (total_sum)
    
    
    
#%%
#2 Task
        
dict_1 = {} #заводим словарь

dict_1[1] = 1
dict_1[2] = 2

for i in range(3,201):
    
    dict_1[i] = dict_1[i-1] + dict_1[i-2]    
     
dict_1[200]

 

#%%
#3 Task

import os;
print (os.getcwd())
os.chdir('/Users/macbook/Desktop/NES 2/8 module/python/hw2')
    
#%%
f = open("words-list-russian.txt", "r")
text = f.read()
print(text)
#%%

dict_2 = {}
dict_3 = {}
l = text.split('\n') #convert into list format

#sort words in l in alphabetic order
for itms in l:
    dict_2[itms] = ''.join(sorted(itms))

#now for anagrams we have the same values, but different keys. Let's then
#map each value to all of the keys it maps to
for key, value in dict_2.items():
    dict_3.setdefault(value, set()).add(key)

#now look for the keys in new dict that have 4 and more values
[values for key, values in dict_3.items() if len(values) > 3]

#%%
#5 Task
import random

data_1 = []

for fivelettersword in l:
    if len(fivelettersword) == 5:
        data_1.append(fivelettersword)

myword = random.choice(data_1)

playing = True
guesses = 0
count = 0

while playing:
    user_guess = input('Введите слово: ')
    if user_guess == 'стоп':
        break
    elif user_guess not in data_1:
        print('Не знаю такого слова')
        continue
    for letter in user_guess:
        if letter in [i for i in str(myword)]:
            count += 1
        guesses += 1
    if count == 5:
        playing = False
        print('Угадали с попытки номер %s' %guesses)
    else: print(count)
return myword
    
#%%
#7 Task

import re
import urllib.request
from bs4 import BeautifulSoup

url = 'http://www.belstat.gov.by/ofitsialnaya-statistika/makroekonomika-i-okruzhayushchaya-sreda/natsionalnye-scheta/godovye-dannye_11/proizvodstvo-valovogo-vnutrennego-produkta/'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

for row in soup.find_all('tr'): #находим строки
    for cell in row.find_all('td'):
        print(cell.text)
        
#%%
#in case it will be easier to format txt file
with open('belorussia.txt', 'w') as q:
    for row in soup.find_all('tr'):
        for cell in row.find_all('td'):
            q.write(cell.text)
        q.write('\n')

    

    
    
    
    
    
    
    
        