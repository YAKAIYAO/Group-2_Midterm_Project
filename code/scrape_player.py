import os
from scrape_player_pages import scrape_page
import pandas as pd


'''Input: Path, Output: Scraping data(player)'''
def scrape(path):
    all_data = pd.DataFrame({"id":{},"name":{},"position":[], "height":[],"weight":[], "age":[],"assist":[],"pts":[]},index=[])
    print(path)
    ranking_data = pd.read_csv(path)
    for e in ranking_data["player_url"]:
        all_data=pd.concat([scrape_page(e)])
    return all_data

''' Input: data and path, Output: CSV file'''
def output_to_csv(all_data, path):
    all_data.to_csv(path,header=True, index = False)
    return

''' Exectuion function from other file(Input: No, Output CSV)'''
def exe_scrape_player():
    BASE_DIR = "artifacts"
    INPUT_PATH = os.path.join(BASE_DIR, "results_ranking.csv")
    OUTPUT_PATH = os.path.join(BASE_DIR, "results_player.csv")
    os.makedirs(BASE_DIR, exist_ok=True)

    all_data = scrape(INPUT_PATH)

    output_to_csv(all_data, OUTPUT_PATH)
