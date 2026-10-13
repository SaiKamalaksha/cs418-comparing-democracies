# Comparing Democracies
# By McCullough, Daunovan, Nimishakavi, and Kamalaksha
#
# Checkpoint 4
#
# Democracy-index-eiu.csv - Daunovan
# democracy-eiu.csv - Kamalaksha
# elections.csv - Kamalaksha
# hdi-ihdi-democracy-by-country.csv - Kamalaksha

## Exploratory analysis

The [EDA report](EDA.md) summarizes the profiles, data checks, distributions, and relationships in the [combined EDA notebook](Checkpoint%204%20-%20EDA/EDA.ipynb). The EIU files contain democracy scores from 0 to 10; `democracy-eiu.csv` covers 2006-2022, while `democracy-index-eiu.csv` has the same 2,610 shared rows plus 2023 values for 155 entities. The HDI/IHDI file has 194 country rows for 2023.

**Revised research questions**

- How are EIU democracy scores related to HDI and IHDI, and does the pattern change around the EIU score threshold of 6?
- Which countries and regions backslid from 2006 to 2022, and are hybrid regimes more volatile than established democracies?

**Main data issues**

| Issue | Action or note |
| --- | --- |
| EIU files include World and region averages, and omit 2007 and 2009. | Excluded aggregate rows from country comparisons, kept them for region plots, and flagged the missing years. |
| The two EIU files repeat all 2,610 shared rows. | Treated the index file as an extension with 2023 data, not a separate dataset. |
| HDI data has 29 missing IHDI values and 46 missing democracy scores; its IHDI values include `..`. | Cast IHDI to numeric, keep missing values, and use complete cases for plots that need all variables. |
| Country labels differ across files, and the EIU/HDI years are 2022/2023 with different score scales. | Join by country code, flag the year difference, and keep the 0-10 and 0-1 measures on separate axes. |
| Don's duplicate-key check tests `(Entity, Code)` but labels it `(Entity, Year)`; the region plots also disagree. | These checks need to be rerun on consistent rows before relying on the results. |

**Key findings:** The joined EIU/HDI sample shows a positive democracy-HDI relationship (Pearson r = 0.64), with a step between regime groups. In Kamalaksha's 139 complete cases, democracy is positively related to HDI (r = 0.697) and IHDI (r = 0.674), while inequality loss has a weaker link after accounting for HDI. From 2006 to 2022, 99 countries declined and 66 improved; these associations do not prove cause and effect.

