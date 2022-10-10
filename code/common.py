import requests
from bs4 import BeautifulSoup

def get_soup(url):

    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    return soup