import requests
from bs4 import BeautifulSoup


#page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
page = requests.get('https://tp.uio.no/uib/timeplan/calendar2.php?id=INFO212&sem=17h&sort=cal')

soup = BeautifulSoup(page.content, 'html.parser')

#Prints all the page content
#print (page.content)

#print(soup.prettify())

print(list(soup.children))
[type(item) for item in list(soup.children)]

html = list(soup.children[2])
list(html.children)

print(page.content)
