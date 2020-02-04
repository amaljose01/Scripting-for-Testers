Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
>>> url = 'https://api.github.com/user'
>>> response = requests.get(url,auth=('amaljose01','###########'))
>>> response.json()
{'login': 'amaljose01', 'id': 22295032, 'node_id': 'MDQ6VXNlcjIyMjk1MDMy', 'avatar_url': 'https://avatars2.githubusercontent.com/u/22295032?v=4', 'gravatar_id': '', 'url': 'https://api.github.com/users/amaljose01', 'html_url': 'https://github.com/amaljose01', 'followers_url': 'https://api.github.com/users/amaljose01/followers', 'following_url': 'https://api.github.com/users/amaljose01/following{/other_user}', 'gists_url': 'https://api.github.com/users/amaljose01/gists{/gist_id}', 'starred_url': 'https://api.github.com/users/amaljose01/starred{/owner}{/repo}', 'subscriptions_url': 'https://api.github.com/users/amaljose01/subscriptions', 'organizations_url': 'https://api.github.com/users/amaljose01/orgs', 'repos_url': 'https://api.github.com/users/amaljose01/repos', 'events_url': 'https://api.github.com/users/amaljose01/events{/privacy}', 'received_events_url': 'https://api.github.com/users/amaljose01/received_events', 'type': 'User', 'site_admin': False, 'name': None, 'company': None, 'blog': '', 'location': None, 'email': None, 'hireable': None, 'bio': None, 'public_repos': 2, 'public_gists': 0, 'followers': 0, 'following': 2, 'created_at': '2016-09-19T12:14:49Z', 'updated_at': '2020-02-04T12:05:53Z', 'private_gists': 0, 'total_private_repos': 1, 'owned_private_repos': 1, 'disk_usage': 34, 'collaborators': 0, 'two_factor_authentication': False, 'plan': {'name': 'free', 'space': 976562499, 'collaborators': 0, 'private_repos': 10000}}
>>> my_json = response.json()
>>> for key in my_json.keys():
	print (key)

	
login
id
node_id
avatar_url
gravatar_id
url
html_url
followers_url
following_url
gists_url
starred_url
subscriptions_url
organizations_url
repos_url
events_url
received_events_url
type
site_admin
name
company
blog
location
email
hireable
bio
public_repos
public_gists
followers
following
created_at
updated_at
private_gists
total_private_repos
owned_private_repos
disk_usage
collaborators
two_factor_authentication
plan
>>> my_json['id']
22295032
>>> 
