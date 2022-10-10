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
    

def player_scraping(soup,id):
    # scrpaing data
    id = int(id)
    # if error, igonore this player
    try: 
        name = soup.title.text.replace(" Stats, News, Bio | ESPN","")
        position = soup.find_all("div", class_="PlayerHeader__Team n8 mt3 mb4 flex items-center mt3 mb4 clr-gray-01")[0].find_all("li", class_="")[1].text    
        height = soup.find_all("div", class_="fw-medium clr-black")[0].text.split(",")[0]
        weight = int(soup.find_all("div", class_="fw-medium clr-black")[0].text.split(",")[1].replace(" ","").replace("lbs",""))
        age = int(soup.find_all("ul", class_="PlayerHeader__Bio_List flex flex-column list clr-gray-04")[0].find_all("div", class_="fw-medium clr-black")[1].text.split(" ")[1].replace("(","").replace(")",""))
        assist = float(soup.find_all("ul", class_="StatBlock__Content flex list ph4 pv3 justify-between")[0].find_all("div",class_="StatBlockInner__Value tc fw-medium n2 clr-gray-02")[2].text)
        pts = float(soup.find_all("ul", class_="StatBlock__Content flex list ph4 pv3 justify-between")[0].find_all("div",class_="StatBlockInner__Value tc fw-medium n2 clr-gray-02")[0].text)

        height = feet_change(height)
    except:
        name=""
        position=""
        height=""
        weight=""
        age=""
        assist=""
        pts=""
    data.loc[id] = [id,name,position,height,weight,age,assist,pts]
    return

def feet_change(feet):
    # 6' 2'' -> 6.2feet
    changed_feet = float(feet.split(" ")[0].replace("'",""))+1/100*float(feet.split(" ")[1][:-1])
    return changed_feet

if __name__ == "__main__":
    url = "https://www.espn.com/nba/player/_/id/4238/eric-bledsoe"
    scrape_page(url)