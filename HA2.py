# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 18:46:18 2018

@author: Vladimir
"""
#%%
import numpy as np
import random as rd
import pandas as pd
import requests
import urllib.request
from bs4 import BeautifulSoup
#%%
# Задача 1
def sumThreeFive(n):
                    res = sum(i for i in range(n) if i%3 ==0 or i%5 ==0)
                    return res
# Check
sumThreeFive(100)
#%%
# Задача 2
def f(n):
    if n==1:
        return(1)
    elif n==2:
        return(2)
    else:
        a=f(n-1)
        a=(a+np.sqrt(5*(a**2)+4*((-1)**(n))))/2
        return(a)       
# Check
%time int(f(200))
#%%
# Задача 3
name = 'words-list-russian.txt' 
df = (pd.read_table(name, header = None))[0].tolist()
df1 = [] 
df1.append([sorted(df[0]),df[0]])
df1
for i in df:
    if sorted(i) in [j[0] for j in df1]:
        index = [j[0] for j in df1].index(sorted(i))
        df1[index].append(i)
    else:
        df1.append([sorted(i),i])
for i in df1:
    if len(i)>4:
        print(i[1:])
#%%
# Задача 4
df2 = []
df3 = []
for i in df:
        if len(set(i)) == len(sorted(i)):
            df2.append(i)   
for i in df2:
    if set(i).issubset('лекарство') == True:
        df3.append(i) 
print(len(df3))
df3
#%%
# Задача 5
j = 0
df4 = []
for i in df2:
        if len(set(i)) == 5:
            df4.append(i)  
df4
word = rd.choice(df4)
#print(word)
for i1 in range(100):
    j = 0
    myword = input('Введите слово:')
    for i in word:
        if set(i).issubset(myword) == True:
            j=j+1
    if j == 5:
        print('Угадали с попытки номер:',j)
        break
    print(j)
    if j == 5:
        print()
#%%
# Задача 7
url = 'http://www.belstat.gov.by/ofitsialnaya-statistika/makroekonomika-i-okruzhayushchaya-sreda/natsionalnye-scheta/godovye-dannye_11/proizvodstvo-valovogo-vnutrennego-produkta/'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

table = soup.find('table')
dfa = pd.read_html(str(table)) 
print(dfa)
