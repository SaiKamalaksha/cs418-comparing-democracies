# Data Acquisition Report
# Comparing Democracies
# By McCullough, Daunovan and Nimishakavi, SaiKamalaksha

### 1. Research Questions
Our group's primary research question investigates how strongly a country's level of democracy correlates with its Human Development Index (HDI) and inequality-adjusted development metrics across different global regions. Specifically, we aim to analyze whether higher democratic governance directly translates into superior human development outcomes, or if inequality plays a mediating role in this relationship. Secondarily, we are exploring whether specific national election dynamics—such as voter turnout trends and changes in electoral systems—can serve as early leading indicators for broader shifts or regressions in a country's overall democracy score over time.

### 2. Primary Datasets
To directly address our research questions, we are using two primary datasets focused on governance and elections. The first is the Economist Intelligence Unit Democracy Panel dataset (`democracy-eiu.csv` and `democracy-index-eiu.csv`), which offers continuous yearly scores and category breakdowns evaluating democratic health across the globe. The second primary dataset is the National Elections Dataset (`elections.csv`), which captures country-level electoral metadata, recorded voter turnout rates, and specific voting system classifications across different nations.

### 3. Secondary Datasets
To complement our governance metrics and introduce development perspectives, we selected two secondary datasets to join and compare against our primary sources. The first is the UNDP Human Development and Inequality Dataset (`hdi-ihdi-democracy-by-country.csv`), which supplies country-level scores for  the standard Human Development Index (HDI) and the Inequality-Adjusted Human Development Index (IHDI). The second is the  EIU Index dataset (`democracy-index-eiu.csv`), which serves as a cross-referencing  data set to pinpoint specific dimensions of democracy such as civil liberties or political participation against socioeconomic outcomes.

### 4. Data Acquisition Method
All four datasets were retrieved, downloaded, and compiled into our local repository structure. We created a dedicated Python execution script (`data_acquisition.py`) that uses the Pandas library to programmatically ingest each raw CSV file using `pd.read_csv()`, validating that the data sources load successfully into standard Pandas DataFrames without ingestion errors.

### 5. Dataset Shapes and Data Profile
Primary Datasets
`elections.csv` contains 187 rows and 6 columns, where a single row represents a country's recent election snapshot; its key variables are `country` (string), `year` (integer), `turnout` (float), and `electoral_system` (string), covering 187 countries globally. 

`democracy-eiu.csv` contains 2,610 rows and 4 columns, where each row represents a single country's democratic evaluation in a specific year; its primary columns are `Entity` (string), ISO country `Code` (string), `Year` (integer), and `democracy_eiu` score (float), spanning approximately 167 countries from 2006 through 2023. 

Secondary Datasets
`democracy-index-eiu.csv` contains 2,765 rows and 4 columns following an identical annual country-year observation structure with global coverage across the same time window. 

`hdi-ihdi-democracy-by-country.csv` consists of 194 rows and 8 columns, where one row represents an individual country's overall development profile; key columns include `country` (string), `code` (string), `hdi` (float), and `ihdi` (float), providing cross-sectional coverage across 194 countries.

## Dataset Sources:
https://www.kaggle.com/datasets/shreyasur965/democracy-index
https://huggingface.co/datasets/marksverdhei/hdi-ihdi-democracy-by-country
https://www.kaggle.com/datasets/volya1208/democracy-index-eiu
https://github.com/jackbandy/data-science-fun/tree/main/datasets/us-presidential-elections