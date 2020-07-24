# from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
# driver = webdriver.Chrome()

class_pub="relative ember-view"
class_text="break-words"


content = open("lnkdhtml.html").read()#driver.page_source
soup = BeautifulSoup(content)
r=soup.findAll('div', attrs={'class':class_pub})

T=[]
for a in soup.findAll('div',href=True, attrs={'class':class_pub}):
	name=a.find('span', attrs={'class':class_text})
	print(name)
	# price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
	# rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
	T.append(name.text)
	# prices.append(price.text)
	# ratings.append(rating.text) 


# df = pd.DataFrame({'ok1':T}) 
# df.to_csv('okay.csv', index=False, encoding='utf-8')