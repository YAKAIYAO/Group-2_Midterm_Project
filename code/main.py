import pandas as pd
import os
from scrape_ranking import exe_scrape_ranking
from scrape_player import exe_scrape_player

# 1. Execute two scraping
exe_scrape_ranking()
exe_scrape_player()

# 2. Merge two csv files(results_player and results_ranking)
BASE_DIR = "artifacts"
Ranking_CSV_PATH = os.path.join(BASE_DIR, "results_ranking.csv")
Player_CSV_PATH = os.path.join(BASE_DIR, "results_player.csv")
Integrated_CSV_PATH = os.path.join(BASE_DIR, "results_integrated.csv")

ranking_data = pd.read_csv(Ranking_CSV_PATH, index_col = "id")
player_data = pd.read_csv(Player_CSV_PATH, index_col = "id")
integrated_data=pd.concat([ranking_data,player_data],axis=1)

integrated_data.to_csv(Integrated_CSV_PATH,header=True)
print("Complete")