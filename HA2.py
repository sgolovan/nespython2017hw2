
# coding: utf-8

# In[285]:

def sumThreefive (n):
    k=0
    if type(n)==int:
        n=n
    elif type(n)==float:
        n=int(n)+1
    else:
        return "Must be integer or float"
    if n<4:
        return k
    for i in range(n):
        if i%3==0 or i%5==0:
            k=k+i
    return k      


# In[286]:

sumThreefive (100)


# In[287]:

sumThreefive (10000)


# In[13]:

list1=[1,1,]
def fibo(n):
    if n < len(list1):
        return list1[n]
    list1.append(fibo(n - 1) + fibo(n - 2))
    return list1[n]


# In[14]:

fibo(10) 


# In[15]:

fibo(200)


# In[290]:

import pandas
a = "words-list-russian.txt"
def amagrams(name):    
    list1 = (pandas.read_table(name, header = None))[0].tolist()
    list2=[]
    output=[]
#create a list with sorted sets of letters
    for i in range(len(list1)):
        k=sorted(list(list1[i]))
        list2.append(''.join(k))
#Create a dictionary in which keys are sorted sets of letters, values are lists of all words with corresponding sets
    dict1={}
    for i in range(1,len(list1)):
        if list2[i] not in dict1.keys():
            dict1[list2[i]]=[list1[i],]
        else:
            dict1[list2[i]].append(list1[i])
#Joine lists with lengths greater than 3 in strings using a comma as a separator. 
#Print strings and save them in output list.           
    for i in dict1.keys():
        if len(dict1[i])>3:
            k=(', '.join(dict1[i]))
            output.append(k)
            print(k)


# In[291]:

amagrams("words-list-russian.txt") 


# In[292]:

import pandas
a = "words-list-russian.txt"
#len(set(a))==len(a)
b='лекарство'
def typesetter (name,target):
    list1 = (pandas.read_table(name, header = None))[0].tolist()
    output=[]
    for i in list1:
        if (len(set(i)-set(target))==0) and (len(set(i))==len(i)):
            output.append(i)
            print(i)
    print("Удалось найти: %s" % len(output))


# In[293]:

typesetter("words-list-russian.txt",'лекарство')


# In[296]:

import random
def otgadai():
    name = "words-list-russian.txt"
    list1 = (pandas.read_table(name, header = None))[0].tolist()
#create a list of all words with five letters, each of which is unique
    list2=[]
    for i in range(len(list1)):
        if len(list1[i])==5 and len(set(list1[i]))==5:
            list2.append(list1[i])
#chose random word
    i=random.randint(0,len(list2))
    guess=list2[i]
    print("подскака: загаданное слово - ", guess)
    fl=True
    k=0
    while fl==True:
        word=str(input('Введите слово из 5 букв: '))
        if (word not in list1) or len(word)!=5:
            print('Не знаю такого слова или <> 5-ти букв')
            continue
        else:
#add an attempt, check the match and calculate the amount of similar letters with repetitions
            k=k+1
            sum=0
            for i in range(len(guess)):
                for j in range(len(word)):
                    if word[j]==guess[i]:
                        sum=sum+1
            if sum==len(word):
                    print("!")
                    print("угадали с попытки номер %s" % k)
                    fl=False
            else:
                print(sum)


# In[295]:

otgadai()


# In[274]:

def otgadai2():
    name = "words-list-russian.txt"
    list1 = (pandas.read_table(name, header = None))[0].tolist()
#create a list of all words with five letters, each of which is unique
    list2=[]
    for i in list1:
        if len(i)==5 and len(set(i))==5:
            list2.append(i)   
    fl=True
    k=0
    while fl==True:
        target=str(input('Введите слово: '))
        if target not in list2:
            print('Слово должно быть из 5 разных букв')
            continue
        else:
            for word in list1:
                if len(word)!=5:
                    continue
                else:
                    sum=0
                    k=k+1
                    print(word)
                    for i in range(len(target)):
                        for j in range(len(word)):
                            if word[j]==target[i]:
                                sum=sum+1
                    if word==target:
                        print("!")
                        print("Я угадала с попытки номер",k)
                        fl=False
                        break
                    else:
                        print(sum)


# In[275]:

otgadai2() 


# In[57]:

import re
import urllib.request
from bs4 import BeautifulSoup
def PRGDP():
    url = 'http://www.belstat.gov.by/ofitsialnaya-statistika/makroekonomika-i-okruzhayushchaya-sreda/natsionalnye-scheta/godovye-dannye_11/proizvodstvo-valovogo-vnutrennego-produkta/'
    data=urllib.request.urlopen(url).read()
    soup = BeautifulSoup(data, 'html.parser')
    output=[]
    i=0
    for tr in soup.find_all('tr'):
        i=i+1
        rows=tr.text.split('\n\n\n\n\t\t\t\t')
        for i in range(len(rows)):
            rows[i]=rows[i].strip()
            rows[i]
            rows[i]=rows[i].replace('\n','')
            rows[i]=rows[i].replace('\t','')
            if rows[i][0:1].isdigit():
                rows[i]=rows[i].replace('\xa0','')
                rows[i]=rows[i].replace(' ','')
                rows[i]=rows[i].replace(',','.')
        output.append(rows)
    for i in range(len(output)):
        output[i]='\t'.join(output[i])
        print(output[i])   

# following piece of code can be placed instead of last two rows and    
#is to make output match exactly with HA examle output, where first row 
#values seems are equal to '', not 't\'

#        if output[i][3][0:1].isdigit():
#            output[i]='\t'.join(output[i])
#        else:
#            output[i]=''.join(output[i])
#        print(output[i]) 


# In[58]:

PRGDP()

