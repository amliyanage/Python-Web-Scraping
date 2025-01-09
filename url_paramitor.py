import requests

url = 'http://example.com'

params = { 'q' : 'python' , 'catogery' : 'books' }
response = requests.get(url,params=params)

if response.status_code == 200 :
    print(response.url)
    print(response.text)
else : 
    print('Error ')


# use auth
user_name = "user"
password = "1234"
response = requests.get(url,auth = (user_name,password))

if response.status_code == 200 : 
    print("Okay")
else : 
    print("Not Okay")