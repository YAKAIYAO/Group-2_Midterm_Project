from common import get_soup
import pandas as pd

data = pd.DataFrame({"id":{},"name":{},"position":[], "height":[],"weight":[], "age":[],"assist":[],"pts":[]},index=[])

def scrape_page(current_URL):
    # scraping each pages
    # 1. Go to Bio page(all data are there)
    print(current_URL)
    Bio_URL= "https://www.espn.com/nba/player/bio/"+ current_URL.replace("https://www.espn.com/nba/player/","")
    
    # 2. id data is extracted from url
    id = current_URL.replace("https://www.espn.com/nba/player/_/id/","").split("/")[0]
    # 3. get html and input them into data
    soup = get_soup(current_URL)
    player_scraping(soup, id)
    return data
