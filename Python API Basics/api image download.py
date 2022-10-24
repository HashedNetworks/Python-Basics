import requests

url_2 = 'https://imgs.xkcd.com/comics/python.png'


r = requests.get(url_2)

with open('comic.png', 'wb') as f:
    f.write(r.content)
    