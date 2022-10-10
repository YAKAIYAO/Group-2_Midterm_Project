import os
from scrape_player_pages import scrape_page
import pandas as pd



def scrape(path):
    # Function: Scraping
    all_data = pd.DataFrame({"id":{},"name":{},"position":[], "height":[],"weight":[], "age":[],"assist":[],"pts":[]},index=[])
    # 1. read scrape ranking csv file
    print(path)
    ranking_data = pd.read_csv(path)
    # 2. all players scraping
    for e in ranking_data["player_url"]:
        all_data=pd.concat([scrape_page(e)])
    return all_data


def output_to_csv(all_data, path):
    # Funtion: Output to csv
    all_data.to_csv(path,header=True, index = False)
    return

def exe_scrape_player():
    # Execute

    # 1. initial value
    BASE_DIR = "artifacts"
    INPUT_PATH = os.path.join(BASE_DIR, "results_ranking.csv")
    OUTPUT_PATH = os.path.join(BASE_DIR, "results_player.csv")
    os.makedirs(BASE_DIR, exist_ok=True)

    # 2. scraping
    all_data = scrape(INPUT_PATH)

    # 3. output_to_csv
    output_to_csv(all_data, OUTPUT_PATH)


if __name__ == "__main__":
    # Execute

    # 1. initial value
    BASE_DIR = "artifacts"
    INPUT_PATH = os.path.join(BASE_DIR, "results_ranking.csv")
    OUTPUT_PATH = os.path.join(BASE_DIR, "results_player.csv")
    os.makedirs(BASE_DIR, exist_ok=True)

    # 2. scraping
    all_data = scrape(INPUT_PATH)

    # 3. output_to_csv
    output_to_csv(all_data, OUTPUT_PATH)