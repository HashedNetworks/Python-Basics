import requests

url_1 = 'https://httpbin.org/post'
url_2 = 'https://xkcd.com/353/'

payload = {
    'username': 'andres',
    'password': 'cisco123'
     }


r = requests.post(url_1, data= payload)
r_dict= r.json()
#print(r_dict)

for key, value in r_dict.items():
     print([key, value])

r_form = r_dict['form']
print(r_form)
for form__1, value_form in r_form.items():
    print(form__1, value_form)
