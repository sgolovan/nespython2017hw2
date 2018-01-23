import re
import urllib.request
from bs4 import BeautifulSoup

url = 'http://www.belstat.gov.by/ofitsialnaya-statistika/makroekonomika-i-okruzhayushchaya-sreda/natsionalnye-scheta/godovye-dannye_11/proizvodstvo-valovogo-vnutrennego-produkta/'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

tags = soup.find_all('p')

n = 0
aa = []
for i in tags:
    n += 1
    if n > 47:
        break
    aa.append(i.getText())

a = len(aa)
for i in range(a):
    aa[i] = aa[i].replace('\t', '')
    aa[i] = aa[i].replace('\n', '')
    aa[i] = aa[i].replace('\xa0', '')
    aa[i] = aa[i].replace(' ', '', 1)
    if 30 < i < 38:
        aa[i] = aa[i].replace(',', '.', 1)
aa[21] = aa[21].replace(' ', '', 1)

for i in range(2, 11):
    print(aa[i], end='\t')
print()
for i in range(11, 20):
    print(aa[i], end='\t')
print()
for i in range(20, 29):
    print(aa[i], end='\t')
print()
for i in range(29, 38):
    print(aa[i], end='\t')
print()
for i in range(38, a):
    print(aa[i], end='\t')
