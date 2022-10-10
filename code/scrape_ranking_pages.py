from common import get_soup
import pandas as pd

new_data = pd.DataFrame({"id":{},"year":{},"rank":[], "name":[], "team":[],"salary":[],"player_url":[]},index=[])
data = pd.DataFrame({"id":{},"year":{},"rank":[], "name":[], "team":[],"salary":[],"player_url":[]},index=[])

def scrape_page(year, current_URL,page):
    # Function scraping
    global max_page
    soup = get_soup(current_URL)
    # Maxpage means the max pages of the ranking each year(if page > maxpage, scraping will be stopped)
    if(page==0):
        max_page = extract_max_page(soup)
    if int(max_page) < int(page+1):
        return
    else:
        print(current_URL)
        # Get information
        oddplayers_html= soup.find_all("tr", class_="oddrow")
        for oddplayer_html in oddplayers_html:
            player_scraping(oddplayer_html,year)

        evenplayers_html= soup.find_all("tr", class_="evenrow")
        for evenplayer_html in evenplayers_html:
            player_scraping(evenplayer_html,year)
    return data

def player_scraping(player_html,year):
    # Function Input:HTML Output:Information
    year = year
    rank = int(player_html.find_all("td")[0].text)
    name = player_html.find_all("td")[1].text
    team = player_html.find_all("td")[2].text
    salary = int(player_html.find_all("td")[3].text.replace("$","").replace(",",""))
    player_url = player_html.find_all("td")[1].find('a').attrs['href'].replace("http://","https://")
    id = int(player_url.replace("https://www.espn.com/nba/player/_/id/","").split("/")[0])
    data.loc[id] = [id,year,rank,name,team,salary,player_url]
    return

def extract_max_page(soup):
    # Function Input:HTML Output:Maxvalue
    temp =[]
    page = soup.find_all("div", class_="page-numbers")[0].text
    temp=page.split(" ")
    max_page=temp[2]
    return max_page

def scrape_all_pages(url,all_years,top):
    # Scraping All year all page 
    for year in all_years: 
        for page in range(20):
            current_URL = url+"/_/year/"+str(year)+"/page/"+str(page+1)+"/seasontype/1"
            scrape_page(year, current_URL,page)
        new_data=top_saraly(data,top)
    return new_data

def top_saraly(data, top):
    # Function Input: all data Output: top30(its number)
    if(top != ""):
        data.sort_values(["rank"],inplace=True)
        new_data = data.head(top)
    return new_data
