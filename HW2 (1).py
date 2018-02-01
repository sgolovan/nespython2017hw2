#1
def sum(n):
    sum = 0
    for i in range(n):
        if i%3==0 or i%5==0:
            sum += i
    return sum        

#2
def fib1(n)  :  
    x =[1,2]     
    def fib(n):
        if n<3:
            return n
        else:
            if len(x)>=n:
                return x[n-1]
            else:
                fibb = fib(n-1)+fib(n-2)
                x.append(fibb)
                return fibb
    return fib(n) 
#3
def wordprog(n):
    f = open(n,'r', encoding = 'UTF-8')
    txt =  f.read()
    f.close()
    wor = txt.split('\n')
    dict1 =dict()
    slist = list()
    for i in range(len(wor)):
        temp = ''.join(sorted(wor[i]))
        if temp in dict1.keys():
            temp2 = dict1.pop(temp)
            temp2.append(wor[i])
            dict1[temp] = temp2
        else :
            dict1[temp] = [wor[i]]
            slist.append(temp)
    for i in range(len(slist)):
        if len(dict1[slist[i]])>=4:
            print(dict1[slist[i]])    
            
#4
def game(file, word):
    f = open(file,'r', encoding = 'UTF-8')
    txt =  f.read()
    f.close()
    wor = txt.split('\n')
    dict2 = dict()
    for i in range(len(word)):
        if word[i] in dict2.keys():
            temp = dict2.pop(word[i])+1
            dict2[word[i]]=temp
        else :
            dict2[word[i]]=1
    for i in range(len(wor)):
        t1 = wor[i]
        dict3 = dict()
        tlist = list()
        for j in range(len(t1)):
            if t1[j] in dict3.keys():
                temp = dict3.pop(t1[j])+1
                dict3[t1[j]]=temp
            else :
                dict3[t1[j]]=1
                tlist.append(t1[j])
        for j in range(len(tlist)):
            if tlist[j] not in dict2.keys() or dict2[tlist[j]]<dict3[tlist[j]]:
                break
            elif j==len(tlist)-1:
                print(wor[i]) 
    
#5
def game1(file):
    import random
    f = open(file,'r', encoding = 'UTF-8')
    txt =  f.read()
    f.close()
    wor = txt.split('\n')
    count1=0
    k = 0
    guess=''
    wlist=list()
    for i in range(len(wor)):
        if len(wor[i])==5:
            wlist.append(wor[i])
    xword =  random.choice(wlist)
    dict4 = dict()
    for i in range(len(xword)):
        if xword[i] in dict4.keys():
            temp = dict4.pop(xword[i])+1
            dict4[xword[i]]=temp
        else :
            dict4[xword[i]]=1   
    while guess !=xword:
        k +=1
        guess = input('Введите слово:')
        if len(guess)!=5:
            print('Слово должно быть из 5 букв')
            continue
        dict5 = dict()
        tlist2 = list()
        count1 = 0
        for i in range(len(guess)):
            if guess[i] in dict5.keys():
                temp = dict5.pop(guess[i])+1
                dict5[guess[i]]=temp
            else :
                dict5[guess[i]]=1
                tlist2.append(guess[i])
        for i in range(len(tlist2)):
            if tlist2[i] in dict4.keys():
                if dict4[tlist2[i]]>dict5[tlist2[i]]:
                    count1 += dict5[tlist2[i]]
                else:
                    count1 +=dict4[tlist2[i]]
        print(count1) 
        if guess==xword:
            print('Поздравляю!\nКоличество попыток:',k)
            
#6
def game2(file):
    import random
    xword1 = input('Загадайте слово:')
    guess=''
    f = open(file,'r', encoding = 'UTF-8')
    txt =  f.read()
    f.close()
    wor = txt.split('\n')  
    wlist=list()
    n=''
    b=0
    for i in range(len(wor)):
        if len(wor[i])==5:
            wlist.append(wor[i])
    while n!= '!': 
        if len(wlist)==0:
            print('Не знаю такого слова')
            break
        b+=1
        guess = random.choice(wlist)
        print(guess) 
        n = input('Введите количество совпадений или ! если слово угадано:')
        if n !='!':
            n= int(n)
        if n=='!':
            print('Угадал с попытки',b)
        elif n==0:
            wlist.remove(guess)
            temp= list()
            for i in range(len(wlist)):
                if guess[0] not in wlist[i] and guess[1] not in wlist[i] and guess[2] not  in wlist[i] and guess[3] not in wlist[i] and guess[4] not in wlist[i]:
                    temp.append(wlist[i])
            wlist = temp        
        elif n==1:
            wlist.remove(guess)
            temp = list()
            for i in range(len(wlist)):
                if guess[0] in wlist[i] or guess[1] in wlist[i] or guess[2]  in wlist[i] or guess[3]  in wlist[i] or guess[4]  in wlist[i]:
                    temp.append(wlist[i])
            wlist = temp    
        elif n==2:    
            temp = list()
            wlist.remove(guess)
            for p in range(len(wlist)):
                k=0
                for i in range(4):
                    for j in range(i+1,5):
                        if guess[i] in wlist[p] and guess[j] in wlist[p].replace(guess[i],'',1):
                            temp.append(wlist[p])
                            k=1
                            break
                    if k==1:
                        break
            wlist = temp
        elif n==3:    
            temp = list()
            wlist.remove(guess)
            for p in range(len(wlist)):
                k=0
                for i in range(3):
                    for j in range(i+1,4):
                        for l in range(j+1,5):
                            if guess[i] in wlist[p] and guess[j] in wlist[p].replace(guess[i],'',1) and guess[l] in wlist[p].replace(guess[i],'',1).replace(guess[j],'',1):
                                temp.append(wlist[p])
                                k=1
                                break
                        if k==1:
                            break
                    if k==1:
                        break
            wlist = temp  
        elif n==4:    
            temp = list()
            wlist.remove(guess)
            for p in range(len(wlist)):
                k=0
                for i in range(2):
                    for j in range(i+1,3):
                        for l in range(j+1,4):
                            for m in range(l+1,5):
                                if guess[i] in wlist[p] and guess[j] in wlist[p].replace(guess[i],'',1) and guess[l] in wlist[p].replace(guess[i],'',1).replace(guess[j],'',1) and guess[m] in wlist[p].replace(guess[i],'',1).replace(guess[j],'',1).replace(guess[l],'',1):
                                    temp.append(wlist[p])
                                    k=1
                                    break
                            if k==1:
                                break
                        if k ==1:
                            break
                    if k==1:
                        break
            wlist = temp   
        elif n==5:
            temp = list()
            wlist.remove(guess)
            for i in range(len(wlist)):
                if guess[0] in wlist[i] and guess[1] in wlist[i] and guess[2]   in wlist[i] and guess[3] in wlist[i] and guess[4]  in wlist[i]:
                    temp.append(wlist[i])
            wlist = temp
        
#7
import re
import urllib.request
from bs4 import BeautifulSoup
x = 'http://www.belstat.gov.by/ofitsialnaya-statistika/makroekonomika-i-okruzhayushchaya-sreda/natsionalnye-scheta/godovye-dannye_11/proizvodstvo-valovogo-vnutrennego-produkta/'
site =  urllib.request.urlopen(x).read() 
soup = BeautifulSoup(site, 'html.parser')         
table = soup.find('table')       
rows = table.find_all('tr')
headings = table.find_all('th')
for i in range(len(headings)):
    headings[i] = headings[i].get_text().strip()
for i in range(len(rows)):
    temp = []
    data = rows[i].find_all('td')
    for j in range(len(data)):
        temp.append(re.sub(r'\xa0','',data[j].get_text().strip()))
        temp[j] = re.sub(r'\t','',temp[j])
        temp[j] = re.sub(r'\n','',temp[j])
    rows[i]=temp
for i in range(1,len(rows[3])):
    rows[3][i]=re.sub(',','.',rows[3][i])           
rows[2][1] = re.sub(' ','',rows[2][1]) 
print('\t'.join(headings),'\n') 
for i in range(1,len(rows)):
    print('\t'.join(rows[i]))         
            
            