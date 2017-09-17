#Import lxml library
from lxml import etree
import requests
from lxml import html
from lxml.html import soupparser


#The page it scrapes from
page = requests.get('https://tp.uio.no/uib/timeplan/calendar2.php?id=INFO212&sem=17h&sort=cal')
tree = html.fromstring(page.content)

#Root?
root = etree.Element("root")

print(root.tag)
print(tree)
