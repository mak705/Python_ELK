 import urllib.request
 import urllib.parse
 from bs4 import BeautifulSoup
 import time 
 import os
 import timeit
 from joblib import Parallel, delayed
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
 def extract_data(link):
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
        #print(dicto)
        return dicto
 if __name__ == '__main__':
    print ("Start")
    start = timeit.default_timer()
    print ("Process ID: ",os.getpid())
    print (start)
    links = ['https://health.usnews.com' + do.get('href', None) for do in doc]
    Parallel(n_jobs=4, verbose=1)(delayed(extract_data)(link) for link in (links))
    extraction_time = timeit.default_timer()
    exectime = extraction_time - start
    print("Time for Cropping is -", (exectime), "seconds or",(exectime)/60, "minutes")
    print ("End")
     
