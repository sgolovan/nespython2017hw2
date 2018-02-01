import numpy as np
import pandas as pd
from collections import Counter
import urllib.request
from bs4 import BeautifulSoup

def sumThreeFive(n):
    '''Returns sum of numbers less then n that are dividing by 3 or 5
    
    Attributes
    ----------
    n : int
        Number parameter
        
    Returns
    -------
    result : int
        Result sum
    '''
    numbers = np.arange(n)
    result = int(numbers[(numbers % 3 == 0) + (numbers % 5 == 0)].sum())
    return result


def fibo(n):
    '''Returns n-th Fibonacci  number
    
    Attributes
    ----------
    n : int
        Number parameter
        
    Returns
    -------
    number : int
        n-th Fibonacci number
    '''
    numbers = np.array([1,2], dtype='uint64')
    for i in range(2,n):
        numbers = np.append(numbers, numbers[-1]+numbers[-2])
    return numbers[n-1]
    

def anagrams(path):
    '''Reads text file from path with words in it and prints out all words from
    anagram classes, that consist of 4 or more words
    
    Attributes
    ----------
    path : string
        Path to file with words
        
    Returns
    -------
    None
    '''
    words = pd.read_csv(path, header=None).values.flatten()
    anagrams_dict = {}
    classes_with_4w = []
    for word in words:
        letters = ''.join(sorted(word))
        if letters not in anagrams_dict:
            anagrams_dict[letters] = [word]
        else:
            anagrams_dict[letters].append(word)
        if len(anagrams_dict[letters]) > 3 and (letters not in classes_with_4w):
            classes_with_4w.append(letters)
            
    for class_with_4w in classes_with_4w:
        print(', '.join(anagrams_dict[class_with_4w]))


def typesetter(path, word_to_type):
    '''Reads text file from path with words in it and prints out all words that
    can be constructed with letters of th word
    
    Attributes
    ----------
    path : string
        Path to file with words
    word_to_type : string
        Word to find words in
    
    Returns
    -------
    None
    '''
    words = pd.read_csv(path, header=None).values.flatten()
    for word in words:
        if sum((Counter(word_to_type) - Counter(word)).values()) == \
                                        len(word_to_type) - len(word):
            print(word)
    
    
def guess_the_word_leader(path):
    '''Plays the role of the leader in guess-the-word game. Selects a secret
    word from file path, requires words on input and prints out, how many
    letters in the input word are in the secret word.
    
    Attributes
    ----------
    path : string
        Path to file with words
    
    Returns
    -------
    None
    '''
    words = pd.read_csv(path, header=None)
    words = words[0][words[0].apply(lambda x: len(x)) == 5].values.flatten()
    secret_word = words[np.random.randint(0,len(words))]
    attempt_num = 0
    while True:
        guess = input('Enter a word: ')
        attempt_num += 1
        if len(guess) != 5:
            print('Wrong word! You need only 5-letters words!')
            continue
        if guess not in words:
            print('I don\'t know this word!')
            continue
        if guess == secret_word:
            print('!\nYou guessed after attempt number '+str(attempt_num))
            break
        print(sum([(letter in secret_word) for letter in guess]))
            
            
def guess_the_word_guesser(path):
    '''Plays the role of the guesser in guess-the-word game. User selects a 
    secret word from file path, function make a guess about the word and 
    requires on input how many letters in the guess are in the secret word.
    Type '!' if the word is guessed to exit.
    
    Attributes
    ----------
    path : string
        Path to file with words
    
    Returns
    -------
    None
    '''
    words = pd.read_csv(path, header=None)
    words = words[0][words[0].apply(lambda x: len(x)) == 5].values.flatten()
    np.random.shuffle(words)
    print('Starting to guess!')
    for word_num in range(len(words)):
        print(words[word_num])
        guessed_letters = input('Enter a number of guessed letters: ')
        if guessed_letters == '!':
            print('I guessed after attempt number '+str(word_num+1))
            return
    print('I don\'t know this word!')
    
 
def parse_table():
    '''Parses table from default url
    '''
    url = 'http://www.belstat.gov.by/ofitsialnaya-statistika/makroekonomika-i-okruzhayushchaya-sreda/natsionalnye-scheta/godovye-dannye_11/proizvodstvo-valovogo-vnutrennego-produkta/'
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'lxml')
    
    table = soup.find('table', {'class' : 'autotbl nohead'}).find('tbody')
    header = table.find('tr')
    column_names = [column.get_text().strip() for 
                    column in header.find_all('th')]
    table_data = []
    for row in table.find_all('tr')[1:]:
        table_data.append([])
        for value in row.find_all('td'):
            clear_value = value.get_text().strip()
            clear_value = clear_value.replace(',','.').replace(u'\xa0','').replace('\n\t\t\t\t','')
            try:
                clear_value = float(clear_value)
            except:
                pass
            table_data[-1].append(clear_value)
    final_table = pd.DataFrame(table_data, columns=column_names)
    final_table.index = final_table.iloc[:,0]
    print(final_table)