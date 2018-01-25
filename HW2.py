#HW2 

#Problem 1
def one(k):
    a=0
    i=0
    while i < k:
        if i % 3 == 0 or i % 5 == 0:
            a = a + i
        i = i + 1
    print(a)
#%%
one(100)



#%%
#Problem 2

#Самым оптимальным способом нахождения чисел Фибоначчи является метод 
#возведения матрицы 11 10 в степень n, где n порядковый номер числа Фибоначчи. 
#Тогда на месте (1,1) в полученной матрице будет n-ое число Фибоначчи.
import numpy as np
def two(n):
    M=np.array([[1, 1], [1, 0]], dtype='object')
    l = np.linalg.matrix_power(M, n)
    print (" N-ое число Фибоначчи равно: %d" % l[0,0])
#%%
two(10)
#%%
two(200)



#%%
#Problem 3

data=open("words-list-russian.txt","r", encoding="utf-8")
lines=data.readlines()

t=list( map(lambda x: x.strip(),lines))
r=list( map(lambda x: list(x.strip()),lines))
p=list( map(lambda x: sorted(x),r))
k=""
w=list(map(lambda x: k.join(x), p))

import collections

j=0
collections.Counter(w).most_common(7)
x=['аворт', 'аборт', 'аакр', 'ааклн', 'корт', 'орст', 'аекст']
y=[]
#list(x[0])
for q in range (0,len(x)):
    for j in range (0,len(t)):
        if len(set(list(t[j])) & set(list(x[q]))) == len(t[j]) and len(t[j]) == len(x[q]):
            y.append(t[j])
        j = j+1
    print(y)
    y=[]
    q=q+1

    
    
    
    #%%
#Problem 4
f=list('лекарство')
m=0
e=[]
for m in range (0, len(r)):
    if len(list(set(r[m]) & set(f))) == len(r[m]):
        e.append(t[m]) 
    m=m+1
print(e)
len(e)





 #%%
#Problem 5
h=0
b=[]
for h in range (0, len(t)):
    if len(t[h]) == 5:
        b.append(t[h])
#print(b)
#len(b)

m=0
s=[]
for m in range (0, len(b)-1):
    if b[m][0] != b[m][1] and b[m][1] != b[m][2] and b[m][2] != b[m][3] and \
       b[m][3] != b[m][4] and b[m][0] != b[m][2] and b[m][0] != b[m][3] and \
       b[m][0] != b[m][4] and b[m][1] != b[m][3] and b[m][1] != b[m][4] and \
       b[m][2] != b[m][3] and b[m][2] != b[m][4] and b[m][3] != b[m][4]:
        s.append(b[m])
#print(s)
#len(s)

import random



def compare_numbers(word, user_guess):
    cowbull = [0, 0]
    for correct, guess in zip(word, user_guess):
        if correct == guess:
            cowbull[1] += 1
        elif guess in word:
            cowbull[0] += 1
    return tuple(cowbull)


playing = True
word = random.choice(s)
guesses = 0

print("Начнем")

print('Верное слово: %s' % word)


while playing:
    user_guess = input("Пробуй!\n")
    if user_guess == "exit":
        break
    cowbullcount = compare_numbers(word, user_guess)
    guesses += 1
    print(' %s верные буквы, и %s верные буквы на верных местах.' % cowbullcount)

    if cowbullcount[1] == 5:
        playing = False
        print("Ты победил после %s попыток! Верное слово %s "
              % (guesses, word))


 #%%
#Problem 6










