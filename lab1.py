import requests

response = requests.get('https://github.com/wrflemin/CMPUT404Lab1/raw/master/lab1.py')
print response.text
