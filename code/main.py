import pandas as pd
import os
from scrape_ranking import exe_scrape_ranking
from scrape_player import exe_scrape_player

# Do the scarpe_ranking.py and make the results_ranking.csv
exe_scrape_player()
# Do the scarpe_ranking.py and make the results_player.csv
exe_scrape_player()

# Merge results_player.csv and results_ranking.csv
# 1. Basic Setup
BASE_DIR = "artifacts"
Ranking_CSV_PATH = os.path.join(BASE_DIR, "results_ranking.csv")
Player_CSV_PATH = os.path.join(BASE_DIR, "results_player.csv")
Integrated_CSV_PATH = os.path.join(BASE_DIR, "results_integrated.csv")

# 2. Integrated data
ranking_data = pd.read_csv(Ranking_CSV_PATH, index_col = "id")
player_data = pd.read_csv(Player_CSV_PATH, index_col = "id")
integrated_data=pd.concat([ranking_data,player_data],axis=1)
