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
