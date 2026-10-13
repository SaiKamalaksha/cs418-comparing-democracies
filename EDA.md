# Exploratory Data Analysis
The findings show relationships, not cause and effect.

## 1. Dataset Profiles

| Dataset | Profile | What stands out |
| --- | --- | --- |
| `democracy-eiu.csv` | Shape: 2,610 rows x 4 columns. `Entity` and `Code` are text; `Year` is integer; `democracy_eiu` is numeric. `null_count`: 90 missing codes; no other missing values. | It covers 174 entities from 2006 to 2022. The mean score is 5.49, median 5.78, standard deviation 2.20, and range 0.32-9.93. |
| `democracy-index-eiu.csv` | Shape: 2,765 rows x 4 columns. Fields are `Entity`, `Code`, `Year`, and `Democracy score`. `null_count`: 96 missing codes; no other missing values. | It covers the same 174 entities and adds scores for 2023 for 155 entities. The mean is 5.50, median 5.79, standard deviation 2.19, and range 0.32-9.93. |
| `hdi-ihdi-democracy-by-country.csv` | Shape: 194 rows x 8 columns. It has country codes/names, rank, year, HDI, IHDI, and two democracy-score fields. `null_count`: Rank 1, HDI 1, IHDI 29, and both democracy fields 46. | All rows are for 2023. HDI has mean 0.724 and median 0.740; IHDI has mean 0.590 and median 0.607. The charts that require all three main values use 139 countries. |

The schema and summary tables (`glimpse`, `null_count`, and `describe`) are in each notebook part. The two EIU files contain the same scores for all 2,610 shared rows; their largest difference is only 0.00000067 from rounding.

## 2. Anomalies and Actions

| Issue | Rows affected | Action |
| --- | ---: | --- |
| World and region averages mixed with country rows | 105 in `democracy-eiu.csv`; 112 in `democracy-index-eiu.csv` | Removed aggregate rows from country comparisons and kept them for region charts. The missing or `OWID_` codes identify these rows. |
| Missing years in the EIU panels | 2007 and 2009; 334 country-years for 167 countries | Left missing and noted the gap. Year-to-year changes use only adjacent available years. |
| Repeated EIU data across files | All 2,610 shared rows match | Treated `democracy-index-eiu.csv` as an extension with 2023 values, not a separate independent dataset. |
| Missing IHDI and other country values | IHDI is missing for 29 countries; democracy scores for 46; HDI and Rank for 1 each | Cast IHDI to a number and kept missing values as null. Complete-case charts leave out countries without the needed values. |
| Country/region codes and names | 90 or 96 missing codes in the EIU files; four country names differ between the EIU and HDI files | Removed aggregate rows and joined country data by code rather than name. |
| Different years and score scales in the join | EIU 2022 is compared with HDI 2023; EIU is 0-10 while HDI/IHDI are 0-1 | Left the year difference flagged and kept the measures on separate axes. |
| Duplicate-key check in Don's notebook | The exact-row check reports 0, but the key check uses `(Entity, Code)` while labeling it `(Entity, Year)` | Do not treat that key result as verified; rerun using `(Entity, Year)`. |
| Regional trend outputs disagree | Daniel's and Don's region plots give different directions for some regions | Left the mismatch flagged; rerun both from the same filtered data before drawing regional conclusions. |

The EIU checks found no out-of-range scores or extra spaces. Values with more than two decimal places occur in aggregate rows, not country rows. In the HDI join, North Korea and Taiwan have no HDI match, and 15 matched countries have no IHDI; 12 of those 15 have democracy scores of 4 or below.

## 3. Distributions

The 2022 EIU score histogram ([Daniel's plot](Checkpoint%204%20-%20EDA/figures/daniel_d1_score_2022.png)) covers 167 countries. Scores range from 0.32 to 9.81; the mean is 5.29, median 5.54, standard deviation 2.38, and IQR 3.12-7.13. The distribution is broad and roughly balanced overall, with clusters rather than one smooth bell shape.

The 2022 category chart ([category counts](Checkpoint%204%20-%20EDA/figures/daniel_d2_category_2022.png)) has 59 authoritarian, 36 hybrid, 48 flawed-democracy, and 24 full-democracy countries. Authoritarian is the largest group and full democracy the smallest.

The EIU year-to-year change histogram ([Daniel's change plot](Checkpoint%204%20-%20EDA/figures/daniel_d3_annual_change.png)) has a large spike at zero: 679 of 2,004 changes (33.9%) are unchanged. The middle half is -0.07 to 0.05 points, but rare changes extend from -2.53 to +2.74; the mean change is -0.014.

For the 139 complete HDI cases, the HDI histogram has mean 0.735 and median 0.758; IHDI has mean 0.603 and median 0.627 ([HDI/IHDI distributions](Checkpoint%204%20-%20EDA/figures/kamalaksha_hdi_ihdi_distribution.png)). Inequality loss has a median of 17.6%, an IQR of 9.5%-31.2%, and a range of 4.8%-43.0% ([inequality-loss distribution](Checkpoint%204%20-%20EDA/figures/kamalaksha_hdi_inequality_loss.png)).

## 4-5. Relationships, Meaning, and Next Questions

| Plot | What it shows and why it matters | What to ask next |
| --- | --- | --- |
| Democracy by continent over time ([Daniel](Checkpoint%204%20-%20EDA/figures/daniel_r1_continents_over_time.png), [Don](Checkpoint%204%20-%20EDA/figures/daunovan_r1_continents_over_time.png)) | Both outputs show the world score falling from about 5.52 in 2006 to 5.29 in 2022, which fits the expected broad decline. Their regional results conflict, so the size and direction of regional differences are not yet reliable. | Rebuild both plots from the same rows, then split North America into the United States/Canada and Central America/Caribbean and test population weighting. |
| Democracy score vs. HDI ([Daniel's joined plot](Checkpoint%204%20-%20EDA/figures/daniel_r2_score_vs_hdi.png)) | The joined sample has 165 countries and a positive link (Pearson 0.64, Spearman 0.65). The step between regime groups and the high-HDI outliers was less expected than a simple straight-line relationship. | Compare HDI across the four democracy groups, split by region, and check whether resource wealth explains high-HDI autocracies. |
| Democracy score vs. inequality loss ([Daniel's plot](Checkpoint%204%20-%20EDA/figures/daniel_r3_score_vs_inequality_loss.png)) | Democracy and inequality loss have a raw correlation of -0.56, but the link is +0.22 after removing HDI, while HDI and loss correlate at -0.90. This is weaker evidence for a direct democracy-inequality link than expected. | Test mediation with a model and seek IHDI or Gini data for the countries missing IHDI. |
| Change from 2006 to 2022 vs. starting score ([Daniel](Checkpoint%204%20-%20EDA/figures/daniel_r4_change_vs_start.png), [Don](Checkpoint%204%20-%20EDA/figures/daunovan_r4_change_vs_start.png)) | 99 countries declined, 66 improved, and 2 stayed the same; the overall decline was expected, but the weak link to starting score and greater movement in hybrid regimes stood out. | Add cross-country election and turnout data, then check whether large score changes happen near elections. `elections.csv` contains U.S. presidential results only, so it cannot answer this across countries. |
| Democracy score vs. HDI ([Kamalaksha's plot](Checkpoint%204%20-%20EDA/figures/kamalaksha_hdi_vs_democracy.png)) | In the 139 complete cases, the correlation is 0.697: higher democracy scores tend to appear with higher HDI, though not for every country. This matches the expected positive pattern but does not show cause. | Compare the pattern across regions and democracy groups, and check how missing cases affect it. |
| Democracy score vs. IHDI ([Kamalaksha's plot](Checkpoint%204%20-%20EDA/figures/kamalaksha_ihdi_vs_democracy.png)) | The correlation is 0.674, a positive link that was expected from the HDI pattern. It is based on fewer countries because many IHDI values are missing. | Find IHDI values for missing countries and see whether the relationship changes. |
| HDI vs. IHDI ([Kamalaksha's plot](Checkpoint%204%20-%20EDA/figures/kamalaksha_hdi_vs_ihdi.png)) | The measures move closely together (r = 0.984), and IHDI is generally below HDI. This is expected because IHDI adjusts for inequality. | Compare the size of the gap across regions and development levels. |
| HDI-IHDI country gaps ([Kamalaksha's inequality-loss chart](Checkpoint%204%20-%20EDA/figures/kamalaksha_hdi_inequality_loss.png)) | A gap was expected because IHDI adjusts for inequality, but the size of the gap varies widely: about 43.0% for Comoros and 4.8% for Slovenia in the country-gap table. | Look at country context and compare gaps by region and income group. |

## 6. Revised Research Questions

**RQ1:** How is EIU democracy score related to HDI and IHDI, and does the pattern change around the EIU threshold of 6? The analysis is a 2022-to-2023 comparison because EIU ends in 2022 for the broad panel and the HDI file contains 2023 only; the category step and the role of HDI in the inequality result make group comparisons and a mediation model more useful than one correlation.

**RQ2:** Which countries and regions backslid from 2006 to 2022, and are hybrid regimes more volatile than established democracies? The original election-turnout question needs a cross-country election dataset; the available `elections.csv` is U.S. presidential data and cannot be joined to the EIU country panel.
