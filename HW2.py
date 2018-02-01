# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 15:18:33 2018

@author: Ruslan Safiullin
"""

##Exercise 1


#%% Ex 1
def summer(n):
    k=0   
    for i in range(n):
        if (i/3).is_integer() or (i/5).is_integer():
            k=k+i
    return(k)
               
print(summer(10000))
#%%Ex 2
#creating cache method 
memorize={}
def fibcache(n):
    if n not in memorize:   ##writing into cache
        memorize[n]=fibo(n)
    return memorize[n]    

def fibo(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
       return fibcache(n-1)+fibcache(n-2)
            
print(fibo(200))
#%%
##Ex 3 

#%%Ex 4
f=open("words-list-russian.txt", "r", encoding="UTF-8")
lines = f.readlines()
array=[]
for i in lines :
    array.append(i.strip())
outarray=[]

for i in array:
    if (len(set('лекарство') & set(i)) == len((i))):
        outarray.append(i)
print(len(outarray))
print(outarray)

#%%Ex 5
import random

f=open("words-list-russian.txt", "r", encoding="UTF-8")
lines = f.readlines()     
#обрезаем библиотеку только 5 букв       
array=[]
for i in lines :
    if len(i.strip())==5: 
        array.append(i.strip())
#загадаем слово
ck=random.choice(array)

playing = True

print("Let's play")   
print('Correct word: %s' % ck)   
corr=[]
##метод для сверки слов при этом если слова равны и буквы повторяются то нужно вернуть корректное значение
def compare_words(ck, user_guess):    
    corr=len(set(ck) & set(user_guess))
    if ck==user_guess:
        corr=len(user_guess)
    return corr
##ЗАПYСК ЦИКЛА ИГРЫ 
tried=0               
user_guess=[]
while playing:    
    user_guess = input("Give 5 letter word!\n")
    while len(user_guess) != 5:
        user_guess = input("Give 5 letter word!\n")  
    guess_count = compare_words(ck, user_guess)
    print('You have %s guesses' % guess_count)
    tried+=1
    if ck==user_guess:
        playing = False
        print("You win the game after %s guesses! The word was %s "
              % (tried, ck))
    if user_guess == "exit":
        break

#
#%%Ex 6
import random

f=open("words-list-russian.txt", "r", encoding="UTF-8")
lines = f.readlines()     
        
array=[]
for i in lines :##5 letter only words 
    if len(i.strip())==5: 
        array.append(i.strip())

##input data
user_input=[]
user_input = input("Give 5 letter word!\n")
while len(user_input) != 5:
     user_input = input("Give 5 letter word!\n")
     if user_input == "exit":
        break       
        
playing = True
print("Let's play")   
print('Correct word: %s' % user_input)  


#correct letters check function and interceprion definition
def compare_words(rand, user_input):   
    corr=[]
    corr=len(set(rand) & set(user_input))
    if ck==user_input:
        corr=len(user_input)
    return corr

tried=0  ##guesses counter             
user_guess=[]
not_in_list=len(array)#for words out of scanning range

while playing:    
    rand=array.pop(random.randrange(len(array)))##вытаскиваем рандомный элемент из массива чтобы не было повторении
    guess_count = compare_words(rand, user_input)##проверяем на схожесть и узнаем сколько совпало букв
    print('Program has %s guesses' % guess_count)
    tried+=1##фиксируем количество попыток
    if rand==user_input:##есди совпало меняем переключатель и пишем результат
            playing = False
            print("You win the game after %s guesses! The word was %s "
             % (tried, user_input))
    if tried==not_in_list:##если вдруг нет в списке то выходим из цикла
        print('Word not in list')
        break
#%%Ex 7
import urllib.request
from bs4 import BeautifulSoup
url = 'http://www.belstat.gov.by/ofitsialnaya-statistika/makroekonomika-i-okruzhayushchaya-sreda/natsionalnye-scheta/godovye-dannye_11/proizvodstvo-valovogo-vnutrennego-produkta/'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser') #class object creation
##ЗАПУСКАЕМ ПАРСЕР при этом обрезаем не используемые куски с помощью циклического стрипа, для поиска требуемых тегов сначала анализируем разметку таблички на странице
table = soup.find('table', attrs={'class':'autotbl nohead'})
table_body = table.find('tbody')
data=[]
rows = table_body.find_all('tr')
for i in rows:
    year = i.find_all('th')
    year = [ele.text.strip()  for ele in year]
    if year!=[]:
        data.append(year) 
       ##т.к. теги отличаются для заголовка то запускаем цикл поиска заного и прибавляем строки к тому же массиву 
for i in rows:
    gdp = i.find_all('td')
    gdp = [ele.text.strip() for ele in gdp]
    data.append(gdp) 
data.pop(1)

##пробегаемся по всем переменным, чтобы порезать ненужные элементы
for i in range(len(data)):
       for k in range(len(data[i])):
           data[i][k]=data[i][k].replace('\n\t\t\t\t','')
           data[i][k]=data[i][k].replace('\xa0','')
#заного пробегаемся но с пропуском первой уолонки, т.к. запятые и пробелы там нужно оставить         
for i in range(len(data)):
       for k in range(len(data[i])-1):
           n=k+1
           data[i][n]=data[i][n].replace(' ','')
           data[i][n]=data[i][n].replace(',','.')    
 ##для вывода в требумой форме конвертируем в массив нампи и выводим
import numpy as np
d=np.array(data)
for i in d:
    print(*i, sep='\t')


    
    





