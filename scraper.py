from lxml import html
import requests
from lxml import etree

page = requests.get('https://tp.uio.no/uib/timeplan/calendar2.php?id=INFO212&sem=17h&sort=cal')
tree = html.fromstring(page.content)

# Check if the code downloads (Gets code 200 if succesful)
# print (page.status_code)

# This will create a list of activities
aktivitet =  tree.xpath('//div[@id="cal-aktivitet"]/text()')
# This will create a list of date/time
dato = tree.xpath('//div[@id="cal-dato"]/text()')
# This will get the room number/name
rom = tree.xpath('//div[@id="cal-rom"]/text()')

print ('Aktivitet: ', aktivitet)
print ('Dato: ', dato)
print ('Rom: ', rom)

#root = etree.Element("root")

# print (root)

# soup = BeautifulSoup(page.content, 'html.parser')
