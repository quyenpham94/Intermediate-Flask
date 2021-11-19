import requests
from secrets import SECRET_KEY 

key=SECRET_KEY

response = requests.get('http://www.mapquestapi.com/geocoding/v1/address',
             params={'key': key, 'location': '123 Main St.'})