
import time, urllib2, re
from bs4 import BeautifulSoup

url = 'http://www.kinopoisk.ru'
pattern = re.compile('/film/.*')
soup = BeautifulSoup(str(urllib2.urlopen(url+'/top/').read()), 'html.parser')
A = soup.find_all('a', {"class":"all"})
for i in A:
  link = i.get('href')
  r = re.match(pattern, link)
  if r:
    print link
    soup2 = BeautifulSoup(str(urllib2.urlopen(url+link).read()), 'html.parser')
    title = soup2.find('span', {"itemprop":"alternativeHeadline"})
    pos = soup2.find('li', {"class":"pos"})
    neg = soup2.find('li', {"class":"neg"})
    #if title.text and pos and neg:
    try:
      print 'title =', title.text
    except:
      pass
    print 'positiv =',pos.find('b').text
    print 'negative =', neg.find('b').text
    time.sleep(1)
