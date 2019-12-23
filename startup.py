import json
import urllib.request
from bs4 import BeautifulSoup
import requests

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

lat = -29.573
long = 152.648

ARR_url = 'https://data.arr-software.org/?lon_coord=' + str(long) + '&lat_coord=' + str(lat) + '&type=json&All=1'

ARR_req = urllib.request.Request(ARR_url, headers={'User-Agent': 'Mozille/5.0'})
ARR_data = json.loads(urllib.request.urlopen(ARR_req).read())

BOM_page = requests.get('http://www.bom.gov.au/water/designRainfalls/revised-ifd/?coordinate_type=dd&latitude=' + str(lat) + '&longitude=' + str(long) + '&user_label=&design=ifds&sdmin=true&sdhr=true&sdday=true#allDesign')
soup = BeautifulSoup(BOM_page.content, 'html.parser')

BOM_dl = str(soup.find_all('a', class_='ifdDownloadCsv seasonalitydata'))
BOM_dlt = BOM_dl[69:len(BOM_dl)-441]

print('http://www.bom.gov.au/water/designRainfalls/revised-ifd/?save=table&url=' + BOM_dlt)

