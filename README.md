# Group 2 Midterm Project Report (30 points)

## GOAL

The main goal of our analysis is three-folds. One is to scrape data of the top 30 NBA players that earned the highest salary during 2021-2022 season from the ESPN website. Second, we use the data we extracted to see if there are any interesting findings/trends between different variables: age, assists per game, points scored per game, height and weight. Lastly, we run a regression analysis to see if there are any correlation between salary and the said variables.


## DATA

If you only execute *main.py*, you can get all datas which is the samea as what we can get.

### Sources

We collected datas from ESPN website in the following.
*1. The ranking of the NBA players salaries 
	http://www.espn.com/nba/salaries/_/year/2022/seasontype/1
*2. The bio pages of each NBA players' detailed inforamtion.	
	For example, Stephen Curry'S detailed information is there.
	https://www.espn.com/nba/player/bio/_/id/3975/stephen-curry

### Collection Methods
We adopted three steps through collecting datas.
As we mentioned above, you only execute *main.py* if you want to execute three steps.


1. Collect the ranking of the NBA players salaries and the each player [scrape_ranking.py/scrape_ranking_pages.py]
	- Using request package, we got the html data from the page of ranking of salaries 2021-2022
	  For example, http://www.espn.com/nba/salaries/_/year/2022/seasontype/1
	- Using beatuiful soup package, we got *ranking, name, team, salarly, the link of player'S detailed*
	- Also, from the player's link, we got players' *id* which was given by ESPN website. This will be used to merge datas later. 
	- Finally, we created CSV.file named **results_players.csv** from these data.


2. Collect each player's detailed information from each bio pages [scrape_player.py/scrape_player_pages.py]
	- Using request package, we got the html data from each player's site
	  For example, https://www.espn.com/nba/player/_/id/3975/stephen-curry
	- Using beautiful soup package, we got *name, position, height, weight, age, assist, pts*
	- Similarly to 1.m, from the player's link, we got players' *id* which was given by ESPN website. 
	- Finally, we created CSV.file named **results_player.csv**

3. Merged between ranking data and player's detailed data[main.py]
	- After 1. 2. steps, we read csv files **results_players.csv** and **results_players.csv**.
	- We set these two datas's index is *id*, which means two data will be consistent in merge.
	- And, we merged two datas into one data based on *id*.
	- Finally, we created CSV.file named **results_integrated.csv** from merged data.


Note: when we dealt with datas, we used pandas package to do this easier.

### Limitation of the data
### Extension of data

## ANALYSIS

### Methodology

### Description and Findings (or lack of findings)
- Plot 1 - description
	* ![](plots/plot1.png)
- Plot 2 - description
	* ![](plots/plot2.png)
- Plot 3 - description
	* ![](plots/plot3.png)
- Plot 4 - description
	* ![](plots/plot4.png)
- Hanwen's Regression - description (From hanwen)
	* ![](plots/regression1.png)

	Equation:
		(SALARY_i ) ̂=β_0+β_1 AGE_i+β_2 PPG_i+β_3 APG_i+β_4 Height_i+β_5 Weight_i+ϵ_i


### Limitations of analysis

### Extension of our analysis
1. extend number of players 30 -> 100 or possibly more
2. extend to multiple seasons instead of one.
3. add more variables: team, weight, rebounds, experience (# of seasons), draft info, etc
3. run various regression analyses and possibly use STATA or R, or even python package if there is one (instead of excel)


## REPRODUCIBILITY
- Please set the current directory to the top or the repo(which is the same as the place of this README.md).
- Before running the code, please install requirement.txt or packages if you do not have them.  
- Open the **main.py** under the directory of the code and Execute it.
- After the above running code, you can get three csv files in the artifacts directory.
- Rhe **result_integrated.csv** file out of three csv files in the artifacts directory is the final result file.



--------------------------------------------------------------------------------------------

# (TO BE DELETED LATER)
# Checklist for presentation and readme report

* Prensentation: goal, methodology, findings, limitations and potential extensions


Reporting about DATA
* Source(s) of dataset(s)
* Data collection methods
* Limitations of the data
* A discussion of extensions of data that would be required to improve the analysis

Reporting your ANALAYSIS
* goal of the analysis -check-
* include methodology
* description of your project and its findings (or lack of findings)
* Your findings (or non-findings)
* The limitations of the analysis
* Extensions of your analysis or areas for more research
* should not include analysis, plots, discoveries, that aren’t directly related to your finding
