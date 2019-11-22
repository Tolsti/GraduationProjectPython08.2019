import requests

rates = requests.get('http://www.nbrb.by/API/ExRates/Rates?Periodicity=0').json()
