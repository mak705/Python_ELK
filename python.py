import urllib.request
import urllib.parse
from bs4 import BeautifulSoup



url = 'https://health.usnews.com/doctors/new-jersey'
#data = data.encode('utf-8')

headers = {}
headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)"

req = urllib.request.Request(url, headers=headers)
resp = urllib.request.urlopen(req)
resp_data = resp.read()

#print(resp_data)
import urllib.request
 import urllib.parse
 from bs4 import BeautifulSoup
 url = 'https://health.usnews.com/doctors/new-jersey'
 #data = data.encode('utf-8')
 headers = {}
 headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)"
 req = urllib.request.Request(url, headers=headers)
 resp = urllib.request.urlopen(req)
 resp_data = resp.read()
 #print(resp_data)
 soup = BeautifulSoup(resp_data, 'html.parser')
 doc = soup.findAll('a', {'class': 'search-result-link bar-tighter'})
 links = ['https://health.usnews.com' + do.get('href', None) for do in doc]
 for link in links:
    headers = {}
    doctor = []
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686)"
    doc_req = urllib.request.Request(link,headers=headers)
    doc_resp = urllib.request.urlopen(doc_req)
    doc_resp_data = doc_resp.read()
    doc_soup = BeautifulSoup(doc_resp_data, 'html.parser')
    doc_name = doc_soup.find('h1')
    doc_name_text =  (doc_name.text).strip()
    doc_name_text_mod = (re.sub('\s+', ' ', doc_name_text))
    doc_name_text_mod_1  = ('Name' ':' +doc_name_text_mod)
    doctor.append(doc_name_text_mod_1)
    doc_overview = doc_soup.find('p')
    doc_overview_text = (doc_overview.text).strip()
    doc_overview_text_mod = (re.sub('\n\| ', ', ', doc_overview_text))
    doc_overview_text_mod_1  = ('Specialised and Location' ':' + doc_overview_text_mod)
    doctor.append(doc_overview_text_mod_1)
    #print (doctor)
    dicto =  (dict(s.split(':') for s in doctor))
    print(dicto)
