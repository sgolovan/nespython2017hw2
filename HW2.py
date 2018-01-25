# -*- coding: utf-8 -*-
from collections import Counter, defaultdict
import pandas as pd
from random import shuffle, randint
import re
import urllib.request
from bs4 import BeautifulSoup
from tabulate import tabulate
import functools


def sumThreeFive(n):
    sum = 0
    for i in range(1, n):
        if (i % 3 == 0) or (i % 5 == 0):
            sum = sum + i
    return sum

@functools.lru_cache(None)
def fibo(n):
    if n == 2:
        return 2
    elif n == 1:
        return 1
    else:
        return (fibo(n-1) + fibo(n-2))
    
def anagrams(text):
    words = pd.read_table(text, header = None)[0].tolist()
    d = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        d[key].append(word)
    for value in d.values():
        if len(value) > 3:
            print(', '.join(value))

def typesetter(text, checkWord):
    words = pd.read_table(text, header = None)[0].tolist()
    for word in words:
        if not(Counter(word) - Counter(checkWord)):
            print(word)
    pass

def unique(word):
    c = Counter(word)
    for letter in word:
        if c[letter] > 1:
            return 0
    return 1

def play_guessed(text, numLetters):
    words = pd.read_table(text, header = None)
    condition = (words[0].map(unique) == 1) & (words[0].map(len) == numLetters)
    words = words.loc[condition].reset_index(drop = True)
    a = words.iloc[randint(0, len(words) - 1), 0]
    tries = 0
    while(True):
        tries += 1
        print('Введите слово: ', end = '')
        h = input().lower()
        if h == 'сдаюсь':
            break
        if (len(words.loc[words[0] == h]) == 0):
            print('Не знаю такого слова')
        else:
            m = Counter(a) - Counter(h)
            m = numLetters - len(m)
            if a == h:
                print('!')
                print('Угадали с попытки номер ', tries)
                break
            else:
                print(m)
    pass

def play_guesser(text, numLetters):
    words = pd.read_table(text, header = None)
    condition = (words[0].map(unique) == 1) & (words[0].map(len) == numLetters)
    words = words.loc[condition].reset_index(drop = True)
    pool = words[0].tolist()
    shuffle(pool)
    tries = 0
    print('Начинаю угадывать!')
    while True:
        tries += 1
        if len(pool) == 0:
            print('Я не знаю такого слова')
            break
        h = pool[0]
        print(h)
        print('Введите число совпадающих букв: ', end ='')
        a = input()
        if a == '!':
            print("Я угадал с попытки номер ", tries)
            break
        elif a == str(numLetters):
            pool.pop(0)
        pool = [w for w in pool if (len(Counter(h) - Counter(w)) == numLetters - int(a))]
    pass

def trim(x):
    if x != None:
        x = re.sub(r'(\d)\s+(\d)',r'\1\2', x)
        x = re.sub(r'(\d),(\d)',r'\1.\2', x)
        return x
    else:
        return x
        
def parseTable():
    url = 'http://www.belstat.gov.by/ofitsialnaya-statistika/makroekonomika-i-okruzhayushchaya-sreda/natsionalnye-scheta/godovye-dannye_11/proizvodstvo-valovogo-vnutrennego-produkta/'
    html = urllib.request.urlopen(url).read()
    table = []
    headers = []
    soup = BeautifulSoup(html, "html.parser")
    for tx in soup.findAll('th'):
        headers.append(tx.text.strip())
    for tr in soup.findAll('tr'):
        row = []
        for td in tr.findAll('td'):
            row.append(' '.join(td.text.split()))
        table.append(row)
    table = pd.DataFrame(table, columns = headers)
    for header in headers:
        table[header] = table[header].apply(trim)
    table.hide_index = True
    print(tabulate(table, headers = headers, tablefmt ='psql', showindex = False))
    pass

if __name__ == "__main__":
    print(sumThreeFive(10000))
    print(fibo(200))
    anagrams('words-list-russian.txt')
    typesetter('words-list-russian.txt', 'лекарство')
    play_guessed('words-list-russian.txt', 5)
    play_guesser('words-list-russian.txt', 5)
    parseTable()









            
