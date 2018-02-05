from urllib.request import urlopen
from bs4 import BeautifulSoup
response = urlopen("http://www.influx.io/");
html=response.read()

soup = BeautifulSoup(html, "html.parser");

datas = soup.html.body.select("div.container > div.product > div.product-content > div.product-content-inner > div.product-box > img")

for data in datas:
    print(data.get('src'))



# print(html)