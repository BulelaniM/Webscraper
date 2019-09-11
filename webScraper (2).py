from bs4 import BeautifulSoup
from lxml import html
import requests
import csv

site = requests.get('https://website.com/').text#opens website to parse
								#uses correct supported encoding for site

soup = BeautifulSoup(site, 'lxml')

csv_file = open('file.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['title','content','primary_download','link_download'])


for article in soup.find_all('div', class_="latestPost-inner"):
	title = article.h2.a.text #grabs title
	print(title)


	for tag in article.find_all('h2', class_='title front-view-title'):
		for link in tag.find_all('a',href = True):
			if link['href'] != "#":
			    request_href = requests.get(link["href"]).text
			    soup2 = BeautifulSoup(request_href, 'lxml')
			    body = soup2.find('div', class_='thecontent')
			    paras = [x for x in body.findAllNext("p")]
			    start = body.text
			    middle2 = "\n\n".join(["".join(x.findAll(text=True)) for x in paras[:-2]])
			    last = paras[-1].contents[0]
			    print (middle2)
			    print()

			    media = body.find('a',href = True)
			    primary_dnw = media.text
			    link_dnw = (media['href'])
			    print(primary_dnw)
			    print(link_dnw)
	print()
	csv_writer.writerow([title,middle2,primary_dnw,link_dnw])

csv_file.close()

