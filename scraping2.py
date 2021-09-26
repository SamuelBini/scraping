import requests
from bs4 import BeautifulSoup
from csv import writer


response = requests.get("https://www.crummy.com/software/BeautifulSoup/bs4/doc/")

soup = BeautifulSoup(response.text, "html.parser")

posts = soup.find_all(class_="section")

for post in posts:
    print(post)