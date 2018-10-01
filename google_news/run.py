import os
import bs4
import lxml
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

def news(xml_news_url):
	Client=urlopen(xml_news_url)
	xml_page=Client.read()
	Client.close()
	soup_page=soup(xml_page,"xml")
	news_list=soup_page.findAll("item")
	for news in news_list:
		result= news.title.text
		print(result)
		os.system("say " + result)
		print(news.link.text)
		print(news.pubDate.text)
		print("\n\n")

#you can add google news 'xml' URL here for any country/category
us_news_url="https://news.google.com/news/rss/?ned=us&gl=US&hl=en"
in_news_url="https://news.google.com/news/rss/?ned=in&gl=IN&hl=en"
sports_url="https://news.google.com/news/rss/headlines/section/topic/SPORTS.en_in/Sports?ned=in&hl=en-IN&gl=IN"

#now call news function with any of these url or BOTH

news(us_news_url)

os.system("say "+" would you like to listen some sports news? " + "if yes then press 1 else 0")
xx= int(input())
if xx !=0:
	news(sports_url)
else:
	os.system("say "+ "Have a nice day")

os.system("say "+" would you like to listen some Indian news? " + "if yes then press 1 else 0")
xx= int(input())
if xx !=0:
	news(in_news_url)
else:
	os.system("say "+ "Have a nice day")