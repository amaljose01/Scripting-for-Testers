>>> import requests
>>> url = 'https://jsonplaceholder.typicode.com/photos'

##get the data about photos
>>> response = requests.get(url)

##read that data into a variable
>>> json_data = response.json()

##cretae a list for storing the url of each photo
>>> url_list = []
>>> for photo in json_data:
	url_list.append(photo['url'])

##How many items are in the url list	
>>> print(len(url_list))
5000

##How many items are there if we turn that list into a set
>>> print(len(set(url_list)))
4996
>>> 
