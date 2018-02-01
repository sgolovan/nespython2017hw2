# -*- coding: utf-8 -*-
"""
Редактор Spyder

Это временный скриптовый файл.
"""
##Задание1
def sumthreefive(n):
   a=0
   for i in range(n):
        if i%3==0:
            a=a+i
        elif i%5==0:
            a=a+i
   return(a)
n=5
print(sumthreefive(n))               
#%%Задание2
def fibo(i,a={1:1,2:2}):
    if i not in a:
        a[i]=fibo(i-1,a)+fibo(i-2,a)
    return a[i]
print(fibo(200))
#%%Задание4
f=open("words-list-russian (1).txt",encoding='utf8')
a=f.readlines()
f.close()
aa = []
k=0
for i in a:
    aa.append(i)
for i in range(len(aa)):
    aa[i]=aa[i].replace("\n","")

for i in range(len(aa)):
   if len(set(aa[i])) == len(aa[i]) and set("лекарство")&set(aa[i])== set(aa[i]):
       print(aa[i])
       k=k+1
print(k)
#%%Задание5
f=open("words-list-russian (1).txt",encoding='utf8')
a=f.readlines()
f.close()

import random
aa = []
for i in range(len(a)):
    a[i]=a[i].replace("\n","")
for i in a:
    if len(i)== 5 and len(i)==len(set(i)):
        aa.append(i)
X=random.choice(aa)
print(X)
s=0
n=0
playing = True
while playing:
    user_guess = input("Ваш вариант загаданного слова\n")
    n=n+1
    if X==user_guess:
        print ("Вы выиграли! С попытки №",n)
        playing = False
    else:
        for i in list(X):
            c=user_guess.count(i)
            s=s+c
        print(s)
        s=0
#%%Задание6
f=open("words-list-russian (1).txt",encoding='utf8')
a=f.readlines()
f.close()

import random
aa = []
for i in range(len(a)):
    a[i]=a[i].replace("\n","")
for i in a:
    if len(i)== 5 and len(i)==len(set(i)):
        aa.append(i)
playing = True
print ("Начинаю угадывать!")
i=0
while playing:
   print(aa[i])
   user_answ=input("Введите число совпадающих букв:")
   if user_answ=="Stop":
       break
   if user_answ=="!":
       playing = False
       print ("Я угадала с попытки №",(i+1))
   elif len(aa)==(i+1):
       playing = False
       print ("Такого слова нет в списке")
       break
   else:
       i=i+1
#%%Задание7
import re
import urllib.request
from bs4 import BeautifulSoup
url = 'http://www.belstat.gov.by/ofitsialnaya-statistika/makroekonomika-i-okruzhayushchaya-sreda/natsionalnye-godovye-dannye_11/proizvodstvo-valovogo-vnutrennego-produkta/'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser') 
pattern = '/active/researchers/contact'
tags = soup.find_all('a', href=True)

data = {}
cnt = 0
#%%Задание3
f=open("words-list-russian (1).txt",encoding='utf8')
a=f.readlines()
f.close()
def is_anagram(L,B):
    return sorted([x for x in L])==sorted([y for y in B])

aa = []
bb=[]
for i in range(len(a)):
    a[i]=a[i].replace("\n","")
for i in a:
    if len(i)== 5:
        aa.append(i)
for i in range(len(aa)):
    if is_anagram(aa[649],aa[i])=="True":
         bb.append(i)


