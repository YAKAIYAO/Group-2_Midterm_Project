import requests
from bs4 import BeautifulSoup

''' Input: URL, Output: HTML(text) using requests and beautiful soup'''
def get_soup(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    return soup