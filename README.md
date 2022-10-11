# Group 2 Midterm Project Report

## Goal

The main goal of our analysis is three-folds. One is to scrape data of the top 30 NBA players that earned the highest salary during 2021-2022 season from the ESPN website. Second, we use the data we extracted to see if there are any interesting findings/trends between different variables: age, assists per game, points scored per game, height and weight. Lastly, we run a regression analysis to see if there are any correlation between salary and the said variables.

## Data

### Sources

We collected data from the ESPN website in the following order:

1. Ranking of the NBA players' salaries 
	http://www.espn.com/nba/salaries/_/year/2022/seasontype/1

2. Bio pages of individual NBA players' detailed inforamtion.	
	For example, Stephen Curry's detailed information can be found below:
	https://www.espn.com/nba/player/bio/_/id/3975/stephen-curry

### Collection Methods

Our collection methods can be divided into three main steps.
Note: You only need to execute *main.py*, which will run below three steps.


1. Collect the ranking of the NBA players salaries and the each player [scrape_ranking.py/scrape_ranking_pages.py]
	- Using request package, we got the html data from the page of ranking of salaries 2021-2022
	  For example, http://www.espn.com/nba/salaries/_/year/2022/seasontype/1
	- Using beatuiful soup package, we got *ranking, name, team, salarly, the link of player'S detailed*
	- Also, from the player's link, we got players' *id* which was given by ESPN website. This will be used to merge data later. 
	- Finally, we created CSV.file named **results_players.csv** that contains these data.


2. Collect each player's detailed information from each bio pages [scrape_player.py/scrape_player_pages.py]
	- Using request package, we got the html data from each player's site
	  For example, https://www.espn.com/nba/player/_/id/3975/stephen-curry
	- Using beautiful soup package, we got *name, position, height, weight, age, assist, pts*
	- Similar to step 1, we got players' *id* from the player's link, which was given by the ESPN website. 
	- Finally, we created CSV.file named **results_player.csv**

3. Merge the ranking data and detailed player's data [main.py]
	- After steps 1 and 2, we read csv files **results_players.csv** and **results_players.csv**.
	- We set *id* as the index for both of the datasets and merged them.
	- Finally, we created CSV.file named **results_integrated.csv** from the merged data.

Note: We used pandas package to handle the datasets more easily.

## Analysis

### Methodology

After scraping all the data, we used matplotlib to visualize them. We used a combination of bar graph (to show the player salary) and scatter plots to display a few chosen variables: age, assists per game, points scored per game, height and weight. We wanted to see if there are any interesting trends that could be observed.

### Description and Findings (and lack of findings)

- Plot 1 - Salary
	![](plots/age.png)
	Plot 1 simply shows the top 30 earners in the descending order. We can see that most players in the top 10 are either point guards(PG) or small forwards(SF). The average salary is around $36m. In the 20-30 range, most players are centers. Those that have similar salaries have similar contract lengths. For example, Andrew Wiggins and Joel Embiid both have five-year contracts.

- Plot 2 - Salary and Age
	![](plots/age.png)
	Among the top 30, we can see that only Lebron James is older than 36. Most players are between age 30-34. It seems like 35+ may have hard time maintainig high salary, perhaps because they have shorter contracts as they get older.

- Plot 3 - Salary and Assists per Game
	![](plots/assist.png)
	We can see that most of the top 30 players have 5+ assists. Stephen Curry has 10+ assists, while Rudy Gobert only has one.

- Plot 4 - Salary and Points per Game
	![](plots/point.png)
	Average points scored per game is around 22.

- Plot 5 - Salary and Height
	![](plots/height.png)
	Most players that made the top 30 are at least 6ft tall.

- Plot 6 - Salary and Weight
	![](plots/weight.png)

- Hanwen's Regression
	![](plots/regression1.png)
	We found that the most correlated variables are: 1. Age 2. Assists 3. Points.
	(More details to be added by Hanwen)


### Limitations

Players in their first season will lack performance data compared to those who played longer seasons. Incomplete data may have been obtained for such players. Salary is often based on contract length. Star players that have longer contracts will inevitabily have higher salaries. Also, both assists and points per game somewhat depends on the players' poistion. For example, point guards and shooting guards will have more assists and points than centers and power forwards (need to confir with Oscar!). Every team has a different salary cap as well. As such, there may be inherent limitations on salary based on the teams and poistions.


### Extensions

In regards to extensions of our analysis, we could collect larger sample size (100 instead of 30) as well as over longer period of time (multiple seasons instead of one). To strengthen our regression analysis, we could also add more variables such as race, turnover rates, steals, blocks, rebounds, etc. To compensate for some of the salary limitation mentioned above, we could analayze salary by team and position, which will yield stronger and more accurate comparison.


### Reproducibility

- Set the current directory to the top of the repo (Same place where this README.md is located).
- Before executing the code, install requirement.txt or packages if you do not have them already, by running "pip3 install -r requirements.txt" 
- Open the **main.py** under the directory of the code and Execute it.
- After running above code, you can get three csv files in the artifacts directory.
- **result_integrated.csv** file is the final result file.



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
