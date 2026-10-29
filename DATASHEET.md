# Comparing Democracies data documentation

Documentation checked on October 28, 2026. This describes the files in repository snapshot `1df27520ba457fbffcc17d68b6f019fec29487d8` and the processing code added for this checkpoint. The original download dates were not recorded. The date above is our documentation check date, not a claim about when the group downloaded the data.

## Summary data card

| Item | EIU democracy panel | HDI and IHDI country file |
| --- | --- | --- |
| File | `democracy-index-eiu.csv` | `hdi-ihdi-democracy-by-country.csv` |
| Source chain | EIU, then Gapminder or Our World in Data, then Kaggle | UNDP and Our World in Data, combined by marksverdhei on Hugging Face |
| One row | One country or territory in one year, or one published geographic average | One country or territory with development measures and an optional democracy score |
| Raw size | 2,765 rows and 4 columns | 194 rows and 8 columns |
| Coverage in our copy | 167 countries and territories, plus 7 geographic aggregates | 194 countries and territories |
| Years | 2006, 2008, and 2010 through 2023 | File label is 2023. Development values match 2022 in the 2023/24 UNDP report |
| Main analysis | 2006 through 2022 for trends. Use 2022 for the development comparison | 165 usable HDI pairs and 150 complete HDI and IHDI pairs after joining to EIU 2022 |
| Main warning | Only 148 countries have 2023 scores in this file | The 2022 IHDI analysis has 150 complete countries. Of 15 matched countries with HDI but no IHDI, 12 have EIU scores of 4 or lower |
| Reuse status | Kaggle declares CC0, but current upstream EIU terms restrict redistribution | Hugging Face declares CC BY-SA 3.0. UNDP and EIU components have separate terms |

All counts in this document come from running [build_data.py](build_data.py). The generated [audit](data/audit.md) and [JSON report](data/audit.json) record the checks. We use the word country below to include territories listed separately by the sources.

### Decisions for this checkpoint

We keep two datasets. We use `democracy-index-eiu.csv` as the democracy source and join it to the development file. The older `democracy-eiu.csv` repeats the historical panel, so we do not stack both files. The archived `elections.csv` contains U.S. presidential candidate results. It cannot answer a question about national turnout across countries, so it is outside our current analysis.

We use EIU 2022 for the main development comparison. The development file says `Year=2023`, but its values match the 2022 columns in UNDP's 2023/24 report. For example, Switzerland has HDI 0.967 and IHDI 0.891, and Norway has 0.966 and 0.903. We keep the original label in `hdi_file_year` and assign the report reference year in `development_reference_year=2022`. This is an explicitly documented correction based on [UNDP Table 3, PDF page 297](https://hdr.undp.org/system/files/documents/global-report-document/hdr2023-24reporten.pdf#page=297). The Hugging Face card does not explain the year label, and some underlying IHDI surveys use earlier available years.

The 2023 EIU data stay available as a separate sensitivity comparison. We do not use the changing 2023 sample to measure overall backsliding. All 19 countries missing in 2023 had authoritarian-range scores in 2022. Using the full available sample each year would make the mean rise from 5.293 to 5.687. Using the same 148 countries in both years shows a decline from 5.756 to 5.687 instead. This is a coverage problem in our stored file, not evidence that EIU stopped assessing those countries.

## 1. Datasheet for the EIU democracy panel

### Motivation

The Economist Intelligence Unit, part of The Economist Group, created the index to compare democracy across countries and track changes. Our copy came from [Shreya Sur965's Global Democracy Index dataset on Kaggle](https://www.kaggle.com/datasets/shreyasur965/democracy-index). That listing identifies [Our World in Data](https://ourworldindata.org/grapher/democracy-index-eiu) as its source. Funding for this particular index and the Kaggle upload is **not documented by the publisher** in the sources we checked.

### Composition

Our CSV has 2,653 country-year rows and 112 aggregate-year rows. The aggregates are Africa, Asia, Europe, North America, Oceania, South America, and World. Each of the 15 observed years through 2022 has 167 countries. In 2023 there are 148. Scores in the country panel range from 0.32 to 9.93. No country scores or years are blank. The 96 blank codes belong to continents. World uses `OWID_WRL`.

This is broad country coverage, not a random sample of countries or people. The [official EIU description](https://www.eiu.com/n/campaigns/democracy-index-2023/) describes coverage of 165 states and two territories and excludes microstates. Our file does not contain indicator-level answers, demographic groups, or sub-scores. The absence of 2007 and 2009 reflects the earlier publication schedule. The reason for the additional 19 missing country rows in the 2023 copy is **not documented by the publisher**. Their names are in the generated audit.

### Collection process

EIU combines expert assessments with public opinion surveys. Its [2022 methodology, printed pages 66 through 68](https://www.eiu.com/n/wp-content/uploads/2023/02/Democracy-Index-2022_FV2.pdf) describes 60 indicators covering elections, government, participation, political culture, and civil liberties. It uses the World Values Survey and other regional or national polls. When survey evidence is unavailable, experts and information from similar countries may fill gaps. These are annual country assessments rather than direct readings of every resident's experience. The publisher materials do not provide respondent-level consent records for this file. Those details are **not documented by the publisher** here.

### Preprocessing

EIU scores the indicators and combines them into category indices and an overall index. OWID's [processing notes](https://ourworldindata.org/grapher/democracy-index-eiu) identify Gapminder as its source through 2020 and direct EIU releases afterward. OWID also supplies geographic averages. We keep those averages separate because the CSV alone does not fully preserve the historical membership and weighting metadata.

The Kaggle uploader says, "The data was downloaded from the website and no alterations were made." We did not recover a separate transformation script for that upload. This CSV is a published score table, not raw survey or expert response data. Those underlying records are not included in our repository, and we did not find an openly downloadable respondent-level source.

### Uses

EIU uses the index in its democracy reports, and our group used the scores in the [earlier EDA](EDA.md). We use it for descriptive country comparisons, changes over time, and associations with development. We should not use it to claim that democracy causes higher HDI, rank individual people, or describe every group's political rights within a country. A change in a country average also does not establish which policy caused it.

### Distribution

The source is distributed as reports and online indicators. Our copy is UTF-8 CSV from Kaggle. The Kaggle listing declares CC0. However, [OWID's current download notice](https://ourworldindata.org/grapher/democracy-index-eiu) states, "The data is published under a license that doesn't allow us to redistribute it." Its chart has separate CC BY-NC-ND terms. These statements do not establish unrestricted reuse of the data. We record the conflict rather than treating the uploader's license as permission from EIU. Processed files containing EIU scores need the upstream rights checked before redistribution.

### Maintenance

EIU maintains the original index. OWID maintains its indicator and processing pipeline. Shreya Sur965 maintains the Kaggle copy, whose version 2 was updated October 20, 2024 and lists future updates as never. Our group maintains this project snapshot. A newer OWID page can cover more years than our file. To detect changes, compare the source release information and local file hashes in [source_manifest.json](data/source_manifest.json), then rerun the audit. Do not silently replace the files or combine releases.

## 2. Datasheet for the HDI and IHDI country file

### Motivation

The [Hugging Face dataset card](https://huggingface.co/datasets/marksverdhei/hdi-ihdi-democracy-by-country) credits marksverdhei with combining UNDP development data and OWID democracy scores. It gives no detailed account of the uploader's purpose or funding, so these are **not documented by the publisher**. UNDP's Human Development Report Office produces the underlying development measures. [UNDP explains](https://hdr.undp.org/data-center/human-development-index) that HDI was created to assess development through people's health, education, and living standards. The [2023/24 report acknowledgments](https://hdr.undp.org/hdr-202324-acknowledgements) identify financial contributions from the Republic of Korea, Japan, and Portugal. Funding for this particular combined file is not documented.

### Composition

There are 194 rows, one per country or territory, with no aggregate rows. All raw `Year` values are 2023. We treat that as the package's label, while the development reference year is 2022 as explained above. This is a combination of available country records, not a random sample.

Rank and HDI each have one missing value, for Taiwan. IHDI has 165 values and 29 missing entries: 28 are coded `..` and one is blank for Taiwan. Both embedded democracy columns have 46 blanks. There are 148 embedded democracy scores, and every one matches the EIU panel's 2023 score. Those columns are repeated source measurements, so agreement is not independent validation. For the 2022 EIU join, 166 country codes match and 150 have both HDI and IHDI. Of the 15 matched countries with HDI but no IHDI, 12 have EIU scores of 4 or lower. The file gives no country-by-country explanation for missing values. Those reasons are **not documented by the publisher**. It also leaves out individual records and all demographic breakdowns.

### Collection process

The uploader combined published tables rather than collecting new information from people. HDI summarizes health, education, and income. The [2023/24 report's statistical annex](https://hdr.undp.org/system/files/documents/global-report-document/hdr2023-24reporten.pdf) identifies the underlying statistical sources. [IHDI](https://hdr.undp.org/inequality-adjusted-human-development-index) adjusts these same three dimensions to account for inequality across people. The year of an underlying household survey can differ from the report's reference year. The packaged CSV does not identify respondents or document their consent. Consent procedures for all upstream sources are **not documented by the publisher** of this combined file.

### Preprocessing

UNDP scales health, education, and income measures and combines them to calculate HDI. For IHDI, it first adjusts each dimension for inequality across people, then combines them. IHDI equals HDI when no inequality is measured and is lower when inequality reduces the adjusted value. In all 165 rows with both measures, IHDI is no higher than HDI. The derived `inequality_loss_pct` shows the relative reduction from HDI to IHDI: `100 * (1 - IHDI / HDI)`. It ranges from 4.752% to 43.003% in this file. The Hugging Face file adds country codes, a shared year label, democracy scores, and a normalized democracy field. In our copy, normalization equals `democracy_eiu / 10` within floating point tolerance. The uploader's merge code, matching key, and detailed cleaning decisions are **not documented by the publisher**.

The card links a UNDP Table 1 spreadsheet. That citation is incomplete for IHDI, which is shown in Table 3 of the report. The original published report is available, but this repository does not contain the underlying household surveys or the uploader's exact construction code. We preserve the downloaded combined CSV as the input to our reproducible processing.

### Uses

UNDP uses these indicators to compare development and inequality. Our group used the combined file in the EDA. We use HDI and IHDI to study country-level associations with democracy. The difference between HDI and IHDI summarizes the effect of inequality on the overall index. It does not show which groups face unequal outcomes or identify the cause. Neither measure captures all parts of well-being. We should not use these country averages to make claims about individuals, prove a causal effect, or decide that countries with missing values have low or high development.

### Distribution

The combined file is a CSV on Hugging Face with a CC BY-SA 3.0 tag. The [HDR website terms](https://hdr.undp.org/terms-use) identify CC BY 3.0 IGO for UNDP materials and require attribution, a license link, and an indication of changes. Those terms do not resolve the EIU restrictions on the democracy fields. We therefore cannot describe the combined or joined data as freely reusable under one clear license. A new development-only extract should be taken directly from UNDP with its terms recorded.

### Maintenance

marksverdhei maintains the packaged file. Its [history](https://huggingface.co/datasets/marksverdhei/hdi-ihdi-democracy-by-country/commits/main) records an upload on November 23, 2024. No regular update schedule or long-term maintenance commitment is documented by the publisher. UNDP maintains and revises the underlying development series. A newer report can revise past values, so the 2023/24 edition matters. Our group should preserve the pinned file revision and audit any replacement before changing the analysis.

## 3. Research questions and data scope

We use target population, access frame, and sample as described in [Learning Data Science, Section 2.2](https://learningds.org/ch/02/data_scope_construct.html). These samples come from available records and missing-value filters. They were not randomly selected.

| Research question | Target population | Access frame | Actual analyzed sample | Limits |
| --- | --- | --- | --- | --- |
| RQ1. How are EIU democracy scores related to HDI and IHDI in 2022, including differences around score 6? | Countries and territories worldwide in the 2022 reference period | The 167 EIU country records for 2022 and 194 records in the packaged development file | 166 matching codes. The HDI analysis uses 165 countries. The IHDI and inequality-loss analysis uses 150 complete countries | North Korea has no development row. Taiwan matches but has no development values. Missing IHDI reduces coverage. Results describe country averages, not individuals or causal effects |
| RQ2. Which countries and published geographic averages declined from 2006 through 2022, and do hybrid regimes show greater annual score variation? | Countries worldwide and their geographic groupings over that period | The EIU panel's 167 countries at 15 observed time points, plus 105 published aggregate rows | 2,505 country-year records, 167 endpoint pairs, and 2,004 consecutive-year changes. Regional descriptions use the separate aggregate table through 2022 | No observations in 2007 or 2009. Microstates and within-country differences are outside the frame. Published region averages do not reveal which residents experienced a change |
| RQ1 sensitivity. What changes if we use the available 2023 EIU scores? | The same worldwide country population, with democracy measured in 2023 | 148 EIU countries for 2023 and the same 194 development records | 148 matching codes, 147 HDI pairs, and 139 complete HDI and IHDI cases | Democracy is from 2023 while development refers to 2022. The 19 missing EIU countries were all in the authoritarian range in 2022 |

For the volatility part of RQ2, the output supplies annual changes and regime categories. Compare the standard deviation of consecutive-year changes, state the regime grouping used, and report group sizes. If grouping by the previous year's regime, use `regime_previous`. Do not call an endpoint change a measure of annual volatility. The score-6 comparison is descriptive. The cutoff does not create an experiment or establish a causal threshold.

The stored files do not supply a country-to-region mapping. We can describe the published region trends, but regional RQ1 models need another documented source and join. We do not claim to have performed that join.

## 4. Codebook

The raw CSV names and types are below. Numeric columns are parsed rather than left as text. Missing numeric values become `None` in Python and empty cells in generated CSVs. No missing values are replaced with zero. A zero score would be a valid score, not a missing code. Boolean values in generated CSVs are `True` and `False`.

### EIU input columns

| Name | Parsed type | Units | Meaning | Allowed or observed values | Missing coding | Source |
| --- | --- | --- | --- | --- | --- | --- |
| `Entity` | string | none | Country, territory, continent, or World name | 174 distinct labels in this file | No missing values | EIU CSV |
| `Code` | nullable string | none | Country identifier or OWID aggregate code | Three capital letters for countries, `OWID_WRL` for World | Empty for 96 continent-year rows | EIU CSV |
| `Year` | integer | calendar year | Democracy assessment year | 2006, 2008, 2010 through 2023 | None missing | EIU CSV |
| `Democracy score` | float | index points | Overall democracy score | Allowed 0 to 10. Observed country range 0.32 to 9.93 | None missing | EIU CSV, with index meaning from the EIU methodology |

### Development input columns

| Name | Parsed type | Units | Meaning | Allowed or observed values | Missing coding | Source |
| --- | --- | --- | --- | --- | --- | --- |
| `country_code` | string | none | Country or territory identifier | 194 distinct three-letter codes | None missing | Hugging Face CSV |
| `Rank` | nullable integer | rank | UNDP HDI rank in this report edition | 1 to 193, with ties | One empty cell | Hugging Face CSV and UNDP report |
| `HDI` | nullable float | index | Human Development Index | Allowed 0 to 1. Observed 0.380 to 0.967 | One empty cell | UNDP values in Hugging Face CSV |
| `IHDI` | nullable float | index | HDI adjusted for inequality in health, education, and income | Allowed 0 to 1. Observed 0.222 to 0.910 | 28 `..` entries and one empty cell for Taiwan | UNDP values in Hugging Face CSV |
| `Country` | string | none | Development source's country label | 194 distinct labels | None missing | Hugging Face CSV |
| `Year` | integer | package year label | Year assigned to all rows by the uploader, not the verified development reference year | Always 2023 | None missing | Hugging Face CSV |
| `democracy_eiu` | nullable float | index points | Embedded democracy score, matching EIU 2023 | Allowed 0 to 10. Observed 2.12 to 9.81 | 46 empty cells | OWID data packaged on Hugging Face |
| `democracy_eiu_normalized` | nullable float | normalized index | Embedded democracy score divided by 10 | Allowed 0 to 1. Observed 0.212 to 0.981 | 46 empty cells | Hugging Face CSV. Formula checked by our code |

### Output columns and created variables

The following table is completed against the generated file headers. Source fields copied to more than one output keep the same meaning.

| Name | Type | Units | Meaning | Allowed or observed values | Missing coding | Source or derivation |
| --- | --- | --- | --- | --- | --- | --- |
| `country_code` | string | none | Shared country join key | Three capital letters | None | Raw `Code` or `country_code`, trimmed and capitalized by `standardize_code` |
| `country_name` | string | none | EIU country name | 167 labels | None | Raw `Entity` in `clean_eiu` |
| `year` | integer | calendar year | EIU score year | 2006, 2008, 2010 through 2023. Changes use 2011 through 2022 | None | Raw EIU `Year` in `clean_eiu` |
| `democracy_score` | float | index points | Current country score, or published average in the aggregate table | Allowed 0 to 10. Country range 0.32 to 9.93 | None | Raw `Democracy score` in `clean_eiu` |
| `regime` | string | category | Regime based on the current score | Authoritarian for 0 to 4, Hybrid regime for greater than 4 through 6, Flawed democracy for greater than 6 through 8, Full democracy for greater than 8 through 10 | None | `regime` uses EIU cutoffs |
| `score_above_6` | boolean | none | Whether the score exceeds the descriptive threshold | `True` if score > 6, otherwise `False` | None | `clean_eiu` |
| `is_partial_coverage_year` | boolean | none | Whether the year has fewer country rows than the largest year in this snapshot | `True` only for 2023 in this file | None | `clean_eiu` compares per-year counts |
| `aggregate_name` | string | none | Published geographic group | Africa, Asia, Europe, North America, Oceania, South America, World | None | EIU `Entity` in `clean_eiu` |
| `aggregate_code` | nullable string | none | Source's aggregate identifier | `OWID_WRL` for World | Empty for continents | EIU `Code` in `clean_eiu` |
| `development_country_name` | nullable string | none | Country name in the development source | 194 source labels | Empty for an unmatched EIU row | Raw `Country` in `clean_development` |
| `hdi_rank` | nullable integer | rank | Published HDI rank | 1 to 193, ties allowed | Empty for Taiwan or an unmatched row | Raw `Rank`, parsed in `clean_development` |
| `hdi` | nullable float | index | Human Development Index | Allowed 0 to 1. Observed 0.380 to 0.967 | Empty for missing source values or an unmatched row | Raw `HDI` in `clean_development` |
| `ihdi` | nullable float | index | HDI adjusted for inequality in health, education, and income | Allowed 0 to 1. Observed 0.222 to 0.910 | Raw blank and `..` become empty. Also empty for unmatched rows | Raw `IHDI` in `clean_development` |
| `hdi_file_year` | nullable integer | package year label | Preserved uploader label | 2023 | Empty for an unmatched row | Raw development `Year` in `clean_development` |
| `development_reference_year` | nullable integer | reference year | Development estimate year identified from the UNDP report | 2022 | Empty for an unmatched row | Set in `clean_development`, with the Table 3 evidence above |
| `embedded_democracy_score` | nullable float | index points | Democracy score copied inside the development input, retained for auditing | Allowed 0 to 10. Observed 2.12 to 9.81 | Empty for source blanks or an unmatched row | Raw `democracy_eiu` in `clean_development`. Not the main 2022 score |
| `embedded_democracy_normalized` | nullable float | normalized index | Embedded democracy score divided by 10 | Allowed 0 to 1. Observed about 0.212 to 0.981 | Empty for source blanks or an unmatched row | Raw `democracy_eiu_normalized`. Formula checked in `clean_development` |
| `inequality_loss_pct` | nullable float | percent | Relative reduction from HDI to IHDI, summarizing the effect of inequality on the overall index | Allowed 0 to 100. Observed about 4.752 to 43.003 | Empty if either development value is missing or HDI is zero | `100 * (1 - ihdi / hdi)` in `clean_development` |
| `development_key_matched` | boolean | none | Whether a development row matched the EIU key | `True` or `False`, independent of missing measurements | None | `join_development` |
| `previous_year` | integer | calendar year | Year before the current annual change | 2010 through 2021, exactly `year - 1` | None | `historical_tables` |
| `previous_score` | float | index points | Score for the preceding calendar year | Allowed 0 to 10 | None | Previous country row in `historical_tables` |
| `score_change` | float | index points per one-year interval | Current score minus previous year's score | Allowed -10 to 10. Observed -2.53 to 2.74 | None. Intervals spanning a gap are excluded | `historical_tables`, rounded to 10 decimal places |
| `regime_previous` | string | category | Regime for the previous year | Same four categories as `regime` | None | Previous country row in `historical_tables` |
| `score_2006` | float | index points | Starting score for the endpoint comparison | Allowed 0 to 10. Observed 1.03 to 9.88 | None in this output | 2006 country row in `historical_tables` |
| `score_2022` | float | index points | Ending score for the endpoint comparison | Allowed 0 to 10. Observed 0.32 to 9.81 | None in this output | 2022 country row in `historical_tables` |
| `change_2006_2022` | float | index points over the full period | 2022 score minus 2006 score | Allowed -10 to 10. Observed -3.19 to 2.92 | None in this output | `historical_tables`, rounded to 10 decimal places |
| `regime_2006` | string | category | Starting regime for the endpoint comparison | Same four categories as `regime` | None | 2006 country row in `historical_tables` |

Function names refer to [build_data.py](build_data.py). The [machine-readable profiles](data/audit.json) give the exact observed range and missing count for every output column, including columns copied into several files.

## 5. Rebuild recipe and join audit

### Obtain the inputs

The repository includes the two original input CSVs. A fresh clone of the documented snapshot provides the exact input bytes without relying on a changing download page.

```sh
git clone https://github.com/SaiKamalaksha/cs418-comparing-democracies.git
cd cs418-comparing-democracies
python3 build_data.py
```

The build uses only the Python standard library and works without internet access after the clone. It writes tidy CSV tables plus audit reports under `data/`. For analysis in pandas, install pandas separately and load the selected output with `pd.read_csv`. The build itself does not require pandas.

To obtain the files from their publishers instead, download `democracy-index-eiu.csv` from version 2 of [the Kaggle listing](https://www.kaggle.com/datasets/shreyasur965/democracy-index/versions/2). Access may require a Kaggle account. Download [the pinned Hugging Face CSV](https://huggingface.co/datasets/marksverdhei/hdi-ihdi-democracy-by-country/raw/1355e41eb8dc16a949dbe63045abafbcaeebff28/hdi_ihdi_democracy.csv) and save it as `hdi-ihdi-democracy-by-country.csv`. Check both SHA-256 values before assuming the download is our snapshot.

| Local input | SHA-256 |
| --- | --- |
| `democracy-index-eiu.csv` | `90c752b0721a08848f18c247bf53e46308798babb0db9f7164c73d37647b4c01` |
| `hdi-ihdi-democracy-by-country.csv` | `11708c2a94e349ffaa25aed8f0e2ff200887d56d03111b2ab754a94c79518d30` |

If a publisher download no longer matches, the [EIU snapshot](https://raw.githubusercontent.com/SaiKamalaksha/cs418-comparing-democracies/1df27520ba457fbffcc17d68b6f019fec29487d8/democracy-index-eiu.csv) and [development snapshot](https://raw.githubusercontent.com/SaiKamalaksha/cs418-comparing-democracies/1df27520ba457fbffcc17d68b6f019fec29487d8/hdi-ihdi-democracy-by-country.csv) identify the repository's exact inputs. Availability of a snapshot does not settle permission to redistribute it.

This recipe rebuilds our analytical tables from the published input files. Rebuilding the original indices from household surveys and expert responses is not possible from this repository. Some upstream records and the combined file's original merge code are unavailable. We state that gap rather than claiming full upstream reproducibility.

### Ordered processing steps

1. Read the two CSVs and verify their SHA-256 hashes and exact headers with [`read_sources`](build_data.py#L46). The build stops if an input has changed. There are 2,765 EIU rows and 194 development rows before processing.
2. Parse numbers using [`numeric`](build_data.py#L72). Only blank cells and `..` count as missing. Reject unexpected nonnumeric text, nonfinite values, and scores outside their allowed ranges. Trim names and standardize country codes with [`standardize_code`](build_data.py#L84).
3. Split EIU rows in [`clean_eiu`](build_data.py#L109). Put blank-code continent rows and `OWID_` rows into `panel_aggregates.csv`. Keep 2,653 country rows in `panel_country.csv` and 112 aggregates separately. Create regime, score-threshold, and partial-coverage flags. No country rows are dropped at this step.
4. Parse the development file in [`clean_development`](build_data.py#L137). Preserve all 194 rows, both embedded democracy columns, and the original year label. Add the 2022 reference year and inequality loss. Convert the 29 missing IHDI entries to nulls. Check that normalized democracy equals the score divided by 10 and IHDI does not exceed HDI.
5. Check country-year and aggregate-name-year keys with [`require_unique`](build_data.py#L91). No duplicate keys occur. The build stops on duplicates rather than deleting or multiplying records. No code substitutions or fuzzy country-name corrections are needed.
6. Make the main join in [`join_development`](build_data.py#L166). Filter EIU to 2022 and development to reference year 2022. Left join on standardized `country_code`, preserving all 167 EIU rows in `rq1_2022_all.csv`. Save all match and nonmatch counts in the audit. Filter only missing HDI for `rq1_2022_hdi.csv`, leaving 165 rows. Require both HDI and IHDI for `rq1_2022_ihdi.csv`, leaving 150 rows. No imputation is used.
7. Run the same join function with EIU year 2023 for `rq1_2023_sensitivity.csv`. Keep its 148 EIU rows and the separate 2022 development reference year. All development rows have file label 2023, but the reference-year difference remains visible. When analyzing this output, keep 147 rows for HDI or 139 for HDI and IHDI together.
8. Build historical tables in [`historical_tables`](build_data.py#L214). Use only EIU years through 2022. Sort within country. Subtract scores only when the two observations are exactly one calendar year apart. This creates 2,004 annual-change rows. Separately look up 2006 and 2022 within each country to create 167 endpoint rows. The endpoint results are 99 declines, 66 increases, and 2 unchanged scores. This lookup is within the same EIU panel, with 167 complete endpoint pairs and no unmatched endpoints.
9. Keep published region rows separate. For RQ2, select `year <= 2022` from `panel_aggregates.csv`, giving 105 rows. No external region mapping or population-weighting join is performed.
10. Write outputs with [`write_csv`](build_data.py#L259) and [`write_reports`](build_data.py#L266). Row order is fixed, missing values stay blank, and CSVs use UTF-8. The audit records every join, excluded country list, range, and missing-value profile. The source manifest records the input hashes, byte sizes, and known provenance.

| Generated table | Rows | Purpose |
| --- | --- | --- |
| `data/panel_country.csv` | 2,653 | Full country panel, including flagged 2023 rows |
| `data/panel_aggregates.csv` | 112 | Published geographic averages kept apart from countries |
| `data/development_clean.csv` | 194 | Parsed development input with both year fields |
| `data/rq1_2022_all.csv` | 167 | Main left join before complete-case filters |
| `data/rq1_2022_hdi.csv` | 165 | Main HDI analysis |
| `data/rq1_2022_ihdi.csv` | 150 | Main IHDI and inequality-loss analysis |
| `data/rq1_2023_sensitivity.csv` | 148 | Available 2023 EIU frame, with missing development values retained |
| `data/rq2_changes.csv` | 2,004 | Consecutive annual score changes through 2022 |
| `data/rq2_endpoints.csv` | 167 | 2006 and 2022 scores and their net change |

For example, after running the build, these lines load the two main analysis dataframes if pandas is installed.

```python
import pandas as pd

hdi_analysis = pd.read_csv("data/rq1_2022_hdi.csv")
ihdi_analysis = pd.read_csv("data/rq1_2022_ihdi.csv")
regions = pd.read_csv("data/panel_aggregates.csv")
regions = regions.loc[regions["year"] <= 2022]
```

### Join results

Counts below distinguish a matching row from a usable measurement. Taiwan is matched even though its HDI is blank.

| Operation | EIU rows | Development rows | Matched pairs | EIU only | Development only | Output after left join | Usable HDI | Usable HDI and IHDI |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Main 2022 comparison | 167 | 194 | 166 | 1 | 28 | 167 | 165 | 150 |
| 2023 sensitivity | 148 | 194 | 148 | 0 | 46 | 148 | 147 | 139 |

The main join uses standardized country codes with EIU year 2022 and verified development reference year 2022. The sensitivity join uses country codes after filtering EIU to 2023 and the same development table to reference year 2022. It also retains the original development file label 2023. The year labels are not matched in this sensitivity comparison. All input keys are unique, so neither join multiplies rows. No fuzzy name matching is used.

North Korea is the only EIU record without a development row in the main join. Four matched countries have different source names: Iran, Laos, Syria, and Democratic Republic of Congo. Their codes match. Fifteen matched countries have HDI but lack IHDI, and 12 of those have democracy scores of 4 or below. The full unmatched lists from both sides are in the audit.

## 6. Access and reuse using FAIR

The checklist follows the [FAIR principles](https://doi.org/10.1038/sdata.2016.18). A public link and an uploader's license tag do not guarantee that every upstream component has the same reuse terms.

| Dataset | Findable | Accessible | Interoperable | Reusable |
| --- | --- | --- | --- | --- |
| EIU democracy panel | [Kaggle source](https://www.kaggle.com/datasets/shreyasur965/democracy-index), version 2, updated October 20, 2024. Exact repository snapshot and hash above | Input CSV is in this repository. Kaggle may require login. Documentation checked October 28, 2026. Original group download date unknown | UTF-8 CSV, country codes, integer assessment years, and a documented 0 to 10 scale | Kaggle declares CC0. Current OWID notice restricts EIU data redistribution. We do not grant an unrestricted license to scores or joined derivatives |
| HDI and IHDI package | [Hugging Face source](https://huggingface.co/datasets/marksverdhei/hdi-ihdi-democracy-by-country), pinned revision `1355e41eb8dc16a949dbe63045abafbcaeebff28`, uploaded November 23, 2024 | Public CSV and card. Documentation checked October 28, 2026. Original group download date unknown | UTF-8 CSV, country codes, parsed missing values, separate file label and development reference year | Package declares CC BY-SA 3.0. UNDP materials have CC BY 3.0 IGO terms. Embedded EIU fields retain unresolved upstream restrictions |

These publisher pages have stable identifiers, but neither packaged dataset has a DOI that we found. Git commit links and SHA-256 hashes make our exact inputs identifiable. They do not guarantee that hosting will last forever. A long-term archive would need to preserve the code, documentation, and permitted inputs together.

The processed CSV files inherit the source restrictions. They are generated locally and excluded from Git to avoid creating another copy of the score tables in this documentation change. The audit summaries, code, and manifest explain how to rebuild them. A future maintainer should review EIU permission before publishing a new combined dataset. This project does not override any publisher's terms.

## 7. People, representation, and CARE

These data describe people indirectly through national political conditions, health, schooling, income, and inequality. There are no names or individual identifiers in our files. That does not make representation problems disappear. A country with a high average can still have poor outcomes for women, Indigenous peoples, ethnic or religious minorities, migrants, rural communities, and people with low incomes. Our files do not separate those experiences. Territorial labels are source identifiers and do not settle questions of sovereignty or community identity.

Missingness also affects whose experiences appear. The 2023 democracy subset leaves out 19 countries with low 2022 democracy scores. In the main 2022 comparison, countries missing IHDI are also disproportionately in the authoritarian category. Complete-case plots can therefore describe the available countries more favorably than the whole target population. We report exclusions and sample sizes instead of filling gaps with invented values.

The [CARE principles](https://doi.org/10.5334/dsj-2020-043) were developed for Indigenous data governance. We use them as a lens and do not claim that this project has community approval or satisfies Indigenous governance requirements.

| Principle | How it applies to our project |
| --- | --- |
| Collective benefit | Use the results to discuss development and political conditions. Do not turn country rankings into judgments about the value of people or cultures |
| Authority to control | A national average does not represent consent from communities within the country. Our repository gives us no authority to speak for Indigenous nations or other groups |
| Responsibility | Keep the sources, years, missing values, and limits visible. Include affected communities' own evidence before making recommendations about them |
| Ethics | Avoid claims about individuals from country averages. Do not use these descriptive associations alone to allocate aid, deny services, or justify political interventions |

## References for the documentation format

The publisher links beside the statements above support the dataset facts. Our computed results are recorded in the audit. The following readings guide the format and scope.

- Gebru et al. [Datasheets for Datasets](https://doi.org/10.1145/3458723), 2021. The seven datasheet sections.
- Holland et al. [The Dataset Nutrition Label](https://arxiv.org/abs/1805.03677), 2018. The summary card format.
- Lau, Gonzalez, and Nolan. [Learning Data Science, Section 2.2](https://learningds.org/ch/02/data_scope_construct.html). Target population, access frame, and sample.
- Ellis and Leek. [How to Share Data for Collaboration](https://doi.org/10.1080/00031305.2017.1375987), 2018. The codebook and reproducible recipe.
- Wilkinson et al. [The FAIR Guiding Principles](https://doi.org/10.1038/sdata.2016.18), 2016. Access and reuse documentation.
- Carroll et al. [The CARE Principles for Indigenous Data Governance](https://doi.org/10.5334/dsj-2020-043), 2020. People and governance.
