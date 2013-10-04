import requests

r = requests.get('http://olinapps-dining.herokuapp.com/api')

print r.json()