import requests

url = 'https://ulvis.net/api.php'
short = input('URL: ')
custom = input('Custom URL(empty for none): ')
params = {'url': short, 'custom': custom, 'private': 1}
response = requests.get(url, params=params)
print(response.text)
input()