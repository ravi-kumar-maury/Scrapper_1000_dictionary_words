import requests
import json
from bs4 import BeautifulSoup as bs
url ="https://www.vocabulary.com/lists/52473"
new_dict = dict()
val = requests.get(url)
# print(val)
soup = bs(val.text,'html.parser')
#print(soup.prettify())
p = "dictionary"
for _ in soup.find_all('li'):
	#if( _.a and _.a.href.contains("/dictionary/")):
	if(_.a):
		print(_.a.text)
		if(_.find('div')):
			print(_.find('div').text)
			new_dict[_.a.text] = _.find('div').text
print(new_dict)
f = open("dictionary.txt", "a")
result = json.dumps(new_dict)
f.write(result)
f.close()
	
	
        
     
