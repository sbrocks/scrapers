
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

req = Request('https://www.google.co.in/search?q=food&tbm=isch&tbo=u&source=univ&sa=X&ved=0ahUKEwic7pzbkO7ZAhUS148KHbpOCSsQ7AkIjQE&biw=1094&bih=486', headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
#print(webpage)

soup = BeautifulSoup(webpage,'html.parser')
#print(soup.encode('utf-8'))
imgs = soup.find_all('img')
import requests
i=0

for img in imgs:
	path = 'images/food'+str(i)+'.jpg'
	f=open(path,'wb')
	print(img.parent.get('href'))
	url = img['src']
	#print(url)
	f.write(requests.get(url).content)
	f.close()
	i=i+1


