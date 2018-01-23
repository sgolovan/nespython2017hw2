import pandas as pd

df = pd.read_csv('words-list-russian.txt', encoding='utf-8', names=['words'])

a = set('лекарство')
n = 0
for i in df['words']:
    b = set(i)
    if len(b) == len(i) and b & a == b:
        print(i)
        n += 1
print('number of words:', n)
