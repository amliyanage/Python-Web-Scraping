from bs4 import BeautifulSoup
import requests

url = 'http://example.com'
response = requests.get(url)

if response.status_code == 200 :
    scoup = BeautifulSoup(response.text,'html.parser')
    title = scoup.h1
    print(title.text)

else :
    print("Error")