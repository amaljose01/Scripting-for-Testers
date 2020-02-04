##Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
##Type "help", "copyright", "credits" or "license()" for more information.

import requests
url = 'https://api.github.com/user'
response = requests.get(url)
response.json()

#{'message': 'Requires authentication', 'documentation_url': 'https://developer.github.com/v3/users/#get-the-authenticated-user'}

# in below method pass the credentials directly as plain text
response = requests.get(url,auth=('amaljose01','######'))
response.json()
## provides output in json here

# in below method pass the authentication key
# Login to GitHub account -> settings -> developer settings -> personal access token -> Generate new token -> select only user -> Generate
response = requests.get(url,headers= {'Authorization':'Bearer #############################'})
response.json()
## provides output in json here 
