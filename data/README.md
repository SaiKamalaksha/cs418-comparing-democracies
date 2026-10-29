# Generated analysis tables

Rebuild with `python3 build_data.py` from the repository root (Python 3.9+, standard library only). Do not hand-edit these outputs. See `audit.md`, `audit.json`, `source_manifest.json` and the repository datasheet for provenance, schemas and limitations.

Empty CSV fields represent missing values; booleans are `True`/`False`. The CSVs can be loaded into a dataframe with `pandas.read_csv`, if pandas is installed. `rq1_2022_all.csv` preserves all 167 EIU countries, `rq1_2022_hdi.csv` requires HDI, and `rq1_2022_ihdi.csv` requires both HDI and IHDI. `rq1_2023_sensitivity.csv` preserves the smaller 2023 EIU frame; filter its missing measures explicitly.

The 2023 development file label is preserved as `hdi_file_year`; `development_reference_year=2022` identifies the UNDP report estimates. `embedded_democracy_score` is retained only for source auditing; the joined `democracy_score` comes from the EIU panel.

**Reuse:** Derived data retain upstream restrictions. No new data license or permission to redistribute EIU values is granted here. This pipeline reconstructs tables from the preserved publisher CSV snapshots, not from proprietary assessments or original survey/administrative microdata.
