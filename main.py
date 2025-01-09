import requests

response = requests.get("http://api.github.com/events")
print(response)

# get response status_code
print(response.status_code)

# get response headers
print(response.headers)

# if response.status_code == 200 :
#     print("Successfully fetched the page")
#     # get Content-Type as jsonfile
#     # print(response.headers['Content-Type'])
#     print(response.text)
# else : 
#     print("some error on fetched the page")

if 'application/json' in response.headers['Content-Type'] : 
    data = response.json()
    print(data)
else : 
    print("Something went wrong !!!!!!")

data = {'username' : 'user' , 'password' : "pass"}
url = "http://httpbin.org/post"
response = requests.post(url,data)

if response.status_code == 200 :
    print("login Successful !")
    print(response.text)
else : 
    print("login failed",response.status_code)


