from common import get_soup
import pandas as pd

new_data = pd.DataFrame({"id":{},"year":{},"rank":[], "name":[], "team":[],"salary":[],"player_url":[]},index=[])
data = pd.DataFrame({"id":{},"year":{},"rank":[], "name":[], "team":[],"salary":[],"player_url":[]},index=[])

# Function scraping
def scrape_page(year, current_URL,page):
    global max_page
    soup = get_soup(current_URL)
    if(page==0):
        max_page = extract_max_page(soup)
    if int(max_page) < int(page+1):
        return
    else:
        print(current_URL)
        oddplayers_html= soup.find_all("tr", class_="oddrow")
        for oddplayer_html in oddplayers_html:
            player_scraping(oddplayer_html,year)

        evenplayers_html= soup.find_all("tr", class_="evenrow")
        for evenplayer_html in evenplayers_html:
            player_scraping(evenplayer_html,year)
    return data

# Function Input:HTML Output:Information
def player_scraping(player_html,year):
    year = year
    rank = int(player_html.find_all("td")[0].text)
    name = player_html.find_all("td")[1].text
    team = player_html.find_all("td")[2].text
    salary = int(player_html.find_all("td")[3].text.replace("$","").replace(",",""))
    player_url = player_html.find_all("td")[1].find('a').attrs['href'].replace("http://","https://")
    id = int(player_url.replace("https://www.espn.com/nba/player/_/id/","").split("/")[0])
    data.loc[id] = [id,year,rank,name,team,salary,player_url]
    return

# Function Input:HTML Output:Maxvalue
def extract_max_page(soup):
    temp =[]
    page = soup.find_all("div", class_="page-numbers")[0].text
    temp=page.split(" ")
    max_page=temp[2]
    return max_page

# Scraping All year all page 
def scrape_all_pages(url,all_years,top):
    for year in all_years: 
        for page in range(20):
            current_URL = url+"/_/year/"+str(year)+"/page/"+str(page+1)+"/seasontype/1"
            scrape_page(year, current_URL,page)
        new_data=top_saraly(data,top)
    return new_data

# Function Input: all data Output: top30(its number)
def top_saraly(data, top):
    if(top != ""):
        data.sort_values(["rank"],inplace=True)
        new_data = data.head(top)
    return new_data
