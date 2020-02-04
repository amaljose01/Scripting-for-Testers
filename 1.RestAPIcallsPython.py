##Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
##Type "help", "copyright", "credits" or "license()" for more information.

##Below are not a single py script- Execute these are individual commands
## dummy json files are retrived from URL : https://jsonplaceholder.typicode.com

import requests
##PUT Request
url ='https://jsonplaceholder.typicode.com/photos'
response = requests.get(url)
print (response.json())

jsonPayload = {'albumId' :1,'title':'test','url':'nothing.com','thumbnailUrl':'nothing.com'}
##POST Request
response = requests.post(url,json=jsonPayload)
response.json()

##PUT Request
url = 'https://jsonplaceholder.typicode.com/photos/100'
response = requests.put(url,json=jsonPayload)
response.json()

##DELETE
response = requests.delete(url)
response.json()
