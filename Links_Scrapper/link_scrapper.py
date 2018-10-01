import requests
import re

url = input('Enter an URL (include "http://""): ') #Takes an input link

website = requests.get(url)
html = website.text

links = re.findall('"((http|ftp)s?://.*?)"', html) #Scrape all links from that page


for link in links:
    print(link[0]) #prints all output links from that page
