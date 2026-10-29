# Comparing Democracies

This project looks at how democracy relates to human development and how democracy scores changed over time.

## Research questions

- How are EIU democracy scores related to HDI and IHDI in 2022, including differences around a democracy score of 6?
- Which countries and published geographic averages declined from 2006 through 2022, and do hybrid regimes show greater annual score variation?

The [earlier EDA report](EDA.md) and [combined notebook](Checkpoint%204%20-%20EDA/EDA.ipynb) show our exploratory work. The data documentation below corrects some earlier descriptions, especially the development reference year and the smaller 2023 country sample. The current analysis uses two datasets. The older democracy file and the U.S. elections file are archived in `Data Files No Longer In Use/`.

## Data documentation

Read [DATASHEET.md](DATASHEET.md) for the seven-section datasheets, research scope, full codebook, rebuild recipe, join counts, and discussion of access and representation.

| Dataset | Source | License and reuse |
| --- | --- | --- |
| `democracy-index-eiu.csv` | [Kaggle copy](https://www.kaggle.com/datasets/shreyasur965/democracy-index) of EIU data through [Our World in Data](https://ourworldindata.org/grapher/democracy-index-eiu) | Kaggle declares CC0, but current upstream EIU terms restrict redistribution. Unrestricted reuse is not established |
| `hdi-ihdi-democracy-by-country.csv` | [marksverdhei on Hugging Face](https://huggingface.co/datasets/marksverdhei/hdi-ihdi-democracy-by-country), combining UNDP and OWID | The package declares CC BY-SA 3.0. UNDP materials use [CC BY 3.0 IGO](https://hdr.undp.org/terms-use). The embedded EIU scores have separate restrictions |

Our biggest limitation is that missing countries can change the pattern we see, especially because the 2023 democracy file leaves out 19 countries with low 2022 scores and the IHDI analysis excludes some authoritarian countries. These are country averages, so they cannot establish cause and effect or describe every group within a country.

## Rebuild the data

From the repository root, run this command with Python 3.9 or newer. No extra packages are needed for the build.

```sh
python3 build_data.py
```

The script verifies the input hashes, cleans the columns, separates geographic averages, checks unique keys, and writes analysis tables under `data/`. The main 2022 comparison has 165 countries with HDI and 150 with both HDI and IHDI. See the generated [audit](data/audit.md) and [source manifest](data/source_manifest.json).

The development file labels every row 2023, but its values match the 2022 estimates in UNDP's 2023/24 report. The script preserves both year fields. It also creates a separate 2023 democracy comparison and keeps the historical trend analysis through 2022.

Processed CSVs are generated locally and ignored by Git. They retain the source restrictions. The code, documentation, and audit reports are included in the repository.
