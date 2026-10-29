# Dataset Facts — Democracy Index (EIU)

<!-- publisher page: https://www.eiu.com/n/campaigns/democracy-index-2023/ -->
<!-- where i got the report from: https://cdn2.opendemocracy.net/media/documents/EIU_Democracy_Index_2023.pdf -->

| **At a glance**                 | **Details**                                                                                                  |
|---------------------------------|--------------------------------------------------------------------------------------------------------------|
| Dataset / local file            | `democracy-index-eiu.csv`                                                                                    |
| Original publisher              | [Economist Intelligence Unit](https://www.eiu.com/n/campaigns/democracy-index-2023/)                         |
| Where *this CSV* was downloaded | [Global Democracy Index (2006-2023) on Kaggle](https://www.kaggle.com/datasets/shreyasur965/democracy-index) |
| Access date / version           | Accessed on 28 Oct 2026                                                                                      |
| File format                     | CSV                                                                                                          |
| Unit of observation (one row)   | Country-year and continent-year (for the continent aggregates)                                               |
| Rows × columns                  | 2765 rows by 4 columns                                                                                       |
| Countries / regions covered     | 165 countries and 2 territories across North America, South America, Africa, Europe, Asia, and Oceania       |
| Year range                      | 2006 -- 2022                                                                                                 |
| Missing values                  | Continent rows do not have a value for the `Code` column; years 2007 and 2009 are missing from the CSV.      |
| License / reuse terms           | Report: no open license specified; CSV from Kaggle: stated as public domain/CC0.                             |
| Main limitation                 | The actual CSV we were able to obtain doesn't have a breakdown of what goes into a country's democracy score |

---

## 1. Motivation

| Question                      | Answer                                                                                                     |
|-------------------------------|----------------------------------------------------------------------------------------------------------------------------|
| Why was this dataset created? | In order to provide a snapshot of the state of democracy worldwide in 2023 [Democracy Index 2023, p. 3]                    |
| Who created it?               | Economist Intelligence Unit [Democracy Index 2023, inside cover]                                                           |
| Who funded its creation?      | Not stated by publisher. The Economist Intelligence Unit is a commercially funded organization within The Economist Group, |
|                               | but we could not find a specific source of funding for the Democracy Index.                                                 |

## 2. Composition

| Question                                              | Answer                                                                                                                        |
|-------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| What does one row represent?                          | Democracy Index score of one country or territory in a specific year.                                                         |
| Total observations and columns                        | 2765 observations and 4 columns                                                                                               |
| Full population or sample?                            | Nearly full population. The EIU seeks to cover the vast majority of states [Democracy Index 2023, p. 3]                       |
| Years and geographic coverage                         | Covers all major world regions from 2006 to 2022, excluding 2007 and 2009.                                                    |
| Missing data and likely exclusions                    | Microstates explicitly excluded [Democracy Index 2023, p. 3]. Regional aggregate rows have no `Code` entry.                   |
| Sensitive information / people represented indirectly | Populations indirectly represented via measures of political participation, political culture,                                |
|                                                       | electoral processes, and civil liberties. Some underlying indicators use public opinion surveys [Democracy Index 2023, p. 8]. |
    
## 3. Collection process

| Question                                 | Answer                                                                                  |
|------------------------------------------|-----------------------------------------------------------------------------------------|
| How were values collected or calculated? | EIU uses expert assessments and public opinion surveys (mainly the World Values Survey) |
|                                          | Its 60 indicators are grouped into 5 catagories scored from 1 to 10, with the overall   |
|                                          | Democracy Index being the mean of the 5 category scores (with adjustments for critical  |
|                                          | indicators) [Democracy Index 2023, pp. 65--67].                                         |
| Collection period and frequency          | Collection began in 2006 and provides annual assessments, with historical scores        |
|                                          | published through to 2023 (though our data file omits 2023). The report does not        |
|                                          | specify the exact dates on which underlying surveys and expert assessments were         |
|                                          | collected for every country [Democracy Index 2023, pp. 3, 17--22, 65--67].              |
| Consent / ethical review, if applicable  | The published dataset contains country-level aggregated scores rather than              |
|                                          | individual-level records. Some indicators rely on public-opinion surveys. The           |
|                                          | report does not document individual participant consent procedures or                   |
|                                          | institutional ethical review [Democracy Index 2023, pp. 65--67].                        |

## 4. Preprocessing and labeling

| Question                                           | Answer                                                                                    |
|----------------------------------------------------|-------------------------------------------------------------------------------------------|
| What processing did the publisher perform?         | EIU scored 60 indicators, grouped them into five categories, converted category           |
|                                                    | totals to a 0–10 scale, applied adjustments for four critical indicators, and             |
|                                                    | averaged the five category scores into an overall Democracy Index. Countries              |
|                                                    | were also assigned one of four regime classifications [Democracy Index 2023, pp. 65--66]. |
| Did the download host transform the original data? | Not documented. The Kaggle source does not note any transformations of the original data, |
|                                                    | and it matches the format of the data in the [Democracy Index 2023].                      |
| Is original/raw data available?                    | The EIU report publishes final country scores, category scores for 2023, and              |
|                                                    | historical overall scores. It also publishes scoring criteria for the                     |
|                                                    | indicators. However, the report does not provide a complete raw dataset of                |
|                                                    | individual expert assessments or survey responses [Democracy Index 2023, pp. 65--67].     |
| What cleaning did **our group** perform?           | Our EDA notebook separates country observations from regional/world aggregates,           |
|                                                    | checks missing country codes, duplicate observations, score ranges, and                   |
|                                                    | formatting anomalies, and derives regime categories from the published score              |
|                                                    | thresholds. It also calculates year-to-year score changes for analysis                    |
|                                                    | [EDA.ipynb](../Checkpoint 4 - EDA/EDA.ipynb).                                             |
## 5. Uses and limitations

| Question                         | Answer                                                                           |
|----------------------------------|----------------------------------------------------------------------------------|
| Documented existing uses         | The Democracy Index is used to compare democratic conditions across countries,   |
|                                  | classify political regimes, and monitor changes in democracy over time. The 2023 |
|                                  | report also examines relationships between democracy and armed conflict.         |
|                                  | [Democracy Index 2023, pp. 3, 23--33]                                            |
| Appropriate uses for our project | Investigating associations between Democracy Index scores and HDI/IHDI;          |
|                                  | comparing democracy scores across countries and regime categories; examining     |
|                                  | democratic decline and score volatility over time. [Democracy Index 2023, pp. 3, |
|                                  | 17--22]                                                                          |
| Uses or conclusions to avoid     | Avoid claiming that democracy causes higher human development based solely on    |
|                                  | correlations. Avoid interpreting a country's aggregate score as a direct measure |
|                                  | of every individual's political experience. The index relies partly on expert    |
|                                  | assessments and survey data, and excludes microstates. [Democracy Index 2023,    |
|                                  | pp. 3, 65--67]                                                                   |

## 6. Distribution and access

| Question | Answer |
|---|---|
| Original source / persistent URL | [link] |
| Download location | [link] |
| Access date or version | [fill in] |
| License / terms | [link and verified summary] |
| Can our processed CSV be shared/reused? | [fill in after checking terms] |

## 7. Maintenance

| Question | Answer |
|---|---|
| Who maintains the dataset? | [fill in; cite] |
| Update frequency and latest included period | [fill in; cite] |
| Corrections / change log / contact | [fill in, or “not documented by the publisher”] |

---

## 8. Codebook: columns used in our analysis

> Add **one row per source or derived column actually used**. Use observed ranges from the selected data, and distinguish them from theoretically allowed values.

| Column name | Data type | Units | Meaning | Allowed values / observed range | Missing-value coding | Origin (source or derivation) |
|---|---|---|---|---|---|---|
| `[column]` | [e.g., integer/string/float] | [fill in] | [fill in; cite for meaning] | [fill in] | [fill in] | [source URL or code link] |
| `[column]` | [fill in] | [fill in] | [fill in] | [fill in] | [fill in] | [fill in] |

## 9. Reproducibility notes for Daniel

- **Raw file and acquisition:** [exact source link; file name; download date]
- **Source-to-local transformations:** [if known; cite any intermediary]
- **Selected common years for cross-dataset analysis:** [confirm with Daniel]
- **Filters / type changes / derived fields handled in EIU code:** [links to notebook cells or scripts]
- **Columns and join keys available:** [fill in]
- **Missing-value and coverage notes to pass to Daniel:** [fill in]
- **Join match/unmatched counts:** [Daniel to calculate and document in shared recipe]

## 10. FAIR / people represented (notes for shared datasheet)

| Topic | Findings / implications |
|---|---|
| Findable | [source + stable identifier] |
| Accessible | [download/access restrictions] |
| Interoperable | [CSV, country codes, year conventions, definitions] |
| Reusable | [license, provenance, processing recipe] |
| Representation / CARE | [who is represented indirectly; who may be omitted or affected; risks of misuse] |

## Sources consulted

- [Publisher methodology title](URL) — [page/section used; date accessed]
- [Dataset download / metadata page](URL) — [page/section used; date accessed]
- [License or terms page](URL) — [page/section used; date accessed]

> **Assignment checks:** Seven datasheet sections, codebook, reproducibility, access/reuse, and representation are required. Scope for each research question and full join counts belong in the group's integrated `DATASHEET.md`. The checkpoint's AI policy requires the actual answers to be written by students from publisher documents and code outputs.
