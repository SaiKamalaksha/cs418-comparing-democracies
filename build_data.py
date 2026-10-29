import csv
import hashlib
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "data"
SOURCES = {
    "democracy-index-eiu.csv": {
        "sha256": "90c752b0721a08848f18c247bf53e46308798babb0db9f7164c73d37647b4c01",
        "source_page": "https://www.kaggle.com/datasets/shreyasur965/democracy-index",
        "upstream_documentation": "https://ourworldindata.org/grapher/democracy-index-eiu",
        "original_download_date": None,
        "original_publisher_version": None,
        "source_version_observed": "Kaggle version 2, updated October 20, 2024",
        "documentation_checked_date": "2026-10-28",
        "declared_distributor_license": "CC0; upstream EIU redistribution restrictions remain unresolved",
    },
    "hdi-ihdi-democracy-by-country.csv": {
        "sha256": "11708c2a94e349ffaa25aed8f0e2ff200887d56d03111b2ab754a94c79518d30",
        "source_page": "https://huggingface.co/datasets/marksverdhei/hdi-ihdi-democracy-by-country",
        "upstream_documentation": "https://hdr.undp.org/content/human-development-report-2023-24",
        "original_download_date": None,
        "original_publisher_version": None,
        "source_revision_observed": "1355e41eb8dc16a949dbe63045abafbcaeebff28",
        "pinned_download": "https://huggingface.co/datasets/marksverdhei/hdi-ihdi-democracy-by-country/raw/1355e41eb8dc16a949dbe63045abafbcaeebff28/hdi_ihdi_democracy.csv",
        "documentation_checked_date": "2026-10-28",
        "declared_distributor_license": "CC BY-SA 3.0; UNDP and EIU components have separate terms",
    },
}

YEAR_NOTE = (
    "The development file stores Year=2023. Its HDI/IHDI values match the "
    "2022 estimates in UNDP HDR 2023-24 Tables 1 and 3 (Table 3, PDF page 297). "
    "We preserve hdi_file_year and annotate development_reference_year=2022. "
    "IHDI component surveys may be from earlier years; this is not a claim "
    "that all underlying measurements occurred in 2022."
)


def read_sources():
    schemas = {
        "democracy-index-eiu.csv": ["Entity", "Code", "Year", "Democracy score"],
        "hdi-ihdi-democracy-by-country.csv": [
            "country_code", "Rank", "HDI", "IHDI", "Country", "Year",
            "democracy_eiu", "democracy_eiu_normalized",
        ],
    }
    tables, manifest = {}, {}
    for name, metadata in SOURCES.items():
        path = ROOT / name
        blob = path.read_bytes()
        digest = hashlib.sha256(blob).hexdigest()
        if digest != metadata["sha256"]:
            raise ValueError(f"Source changed: {name}; review its new version before updating the hash")
        with path.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames != schemas[name]:
                raise ValueError(f"Unexpected schema in {name}: {reader.fieldnames}")
            rows = list(reader)
        tables[name] = rows
        manifest[name] = dict(metadata, file_bytes=len(blob), rows=len(rows),
                              format="UTF-8 CSV", missing_provenance="Original download date/version not recorded")
    return tables, manifest


def numeric(value, label, lower=None, upper=None, integer=False):
    text = value.strip()
    if text in ("", ".."):
        return None
    result = int(text) if integer else float(text)
    if not math.isfinite(result):
        raise ValueError(f"Non-finite {label}: {value!r}")
    if lower is not None and result < lower or upper is not None and result > upper:
        raise ValueError(f"Out-of-range {label}: {value!r}")
    return result


def standardize_code(value):
    code = value.strip().upper()
    if not re.fullmatch(r"[A-Z]{3}", code):
        raise ValueError(f"Invalid country key: {value!r}")
    return code


def require_unique(rows, fields, label):
    keys = [tuple(row[field] for field in fields) for row in rows]
    duplicates = [key for key, count in Counter(keys).items() if count > 1]
    if duplicates:
        raise ValueError(f"Duplicate keys in {label}: {duplicates}")
    return 0


def regime(score):
    if score <= 4:
        return "Authoritarian"
    if score <= 6:
        return "Hybrid regime"
    if score <= 8:
        return "Flawed democracy"
    return "Full democracy"


def clean_eiu(raw):
    countries, aggregates = [], []
    for source in raw:
        year = numeric(source["Year"], "Year", integer=True)
        score = numeric(source["Democracy score"], "Democracy score", 0, 10)
        if year is None or score is None or not source["Entity"].strip():
            raise ValueError("EIU year, name and score are required")
        code = source["Code"].strip().upper()
        if not code or code.startswith("OWID_"):
            aggregates.append({"aggregate_name": source["Entity"].strip(),
                               "aggregate_code": code or None, "year": year,
                               "democracy_score": score})
        else:
            countries.append({"country_code": standardize_code(code),
                              "country_name": source["Entity"].strip(),
                              "year": year, "democracy_score": score,
                              "regime": regime(score), "score_above_6": score > 6})
    require_unique(countries, ["country_code", "year"], "EIU countries")
    require_unique(aggregates, ["aggregate_name", "year"], "EIU aggregates")
    counts = Counter(row["year"] for row in countries)
    maximum = max(counts.values())
    for row in countries:
        row["is_partial_coverage_year"] = counts[row["year"]] < maximum
    countries.sort(key=lambda row: (row["country_code"], row["year"]))
    aggregates.sort(key=lambda row: (row["aggregate_name"], row["year"]))
    return countries, aggregates


def clean_development(raw):
    rows = []
    for source in raw:
        hdi = numeric(source["HDI"], "HDI", 0, 1)
        ihdi = numeric(source["IHDI"], "IHDI", 0, 1)
        score = numeric(source["democracy_eiu"], "embedded democracy", 0, 10)
        normalized = numeric(source["democracy_eiu_normalized"], "normalized democracy", 0, 1)
        if score is not None and (normalized is None or abs(score / 10 - normalized) > 1e-12):
            raise ValueError("Embedded normalized democracy score disagrees with score / 10")
        if hdi is not None and ihdi is not None and ihdi > hdi:
            raise ValueError("IHDI exceeds HDI")
        file_year = numeric(source["Year"], "HDI file year", integer=True)
        if file_year != 2023:
            raise ValueError("New development year requires a new provenance review")
        rows.append({
            "country_code": standardize_code(source["country_code"]),
            "development_country_name": source["Country"].strip(),
            "hdi_rank": numeric(source["Rank"], "HDI rank", 1, 193, integer=True),
            "hdi": hdi, "ihdi": ihdi, "hdi_file_year": file_year,
            "development_reference_year": 2022,
            "embedded_democracy_score": score,
            "embedded_democracy_normalized": normalized,
            "inequality_loss_pct": 100 * (1 - ihdi / hdi) if hdi and ihdi is not None else None,
        })
    require_unique(rows, ["country_code", "hdi_file_year"], "development file")
    require_unique(rows, ["country_code", "development_reference_year"], "development reference years")
    return sorted(rows, key=lambda row: row["country_code"])


def join_development(countries, development, democracy_year):
    left = [row for row in countries if row["year"] == democracy_year]
    right = [row for row in development if row["development_reference_year"] == 2022]
    require_unique(left, ["country_code"], f"EIU {democracy_year}")
    require_unique(right, ["country_code"], "development join")
    lookup = {row["country_code"]: row for row in right}
    left_keys, right_keys = {row["country_code"] for row in left}, set(lookup)
    columns = [name for name in development[0] if name != "country_code"]
    joined = []
    for source in left:
        match = lookup.get(source["country_code"])
        row = dict(source, development_key_matched=match is not None)
        row.update({name: match[name] if match else None for name in columns})
        joined.append(row)
    hdi_complete = [row for row in joined if row["hdi"] is not None]
    ihdi_complete = [row for row in hdi_complete if row["ihdi"] is not None]
    names = lambda rows, keys, name: [
        {"country_code": row["country_code"], "country_name": row[name]}
        for row in rows if row["country_code"] in keys
    ]
    audit = {
        "key": ["country_code"], "democracy_year_filter": democracy_year,
        "development_reference_year_filter": 2022,
        "hdi_file_year": 2023, "eiu_rows_before": len(left),
        "development_rows_before": len(right), "left_join_rows_after": len(joined),
        "matched_from_eiu": len(left_keys & right_keys),
        "matched_from_development": len(left_keys & right_keys),
        "eiu_unmatched_count": len(left_keys - right_keys),
        "development_unmatched_count": len(right_keys - left_keys),
        "eiu_unmatched": names(left, left_keys - right_keys, "country_name"),
        "development_unmatched": names(right, right_keys - left_keys, "development_country_name"),
        "usable_hdi_rows": len(hdi_complete), "usable_hdi_ihdi_rows": len(ihdi_complete),
        "matched_but_missing_hdi": [row["country_code"] for row in joined
                                   if row["development_key_matched"] and row["hdi"] is None],
        "matched_but_missing_ihdi": [row["country_code"] for row in joined
                                    if row["development_key_matched"] and row["ihdi"] is None],
        "hdi_present_ihdi_missing": [row["country_code"] for row in joined
                                    if row["hdi"] is not None and row["ihdi"] is None],
        "name_disagreements": [
            {"country_code": row["country_code"], "eiu_name": row["country_name"],
             "development_name": row["development_country_name"]}
            for row in joined if row["development_key_matched"]
            and row["country_name"] != row["development_country_name"]
        ],
    }
    return joined, hdi_complete, ihdi_complete, audit


def historical_tables(countries):
    grouped = defaultdict(list)
    for row in countries:
        if row["year"] <= 2022:
            grouped[row["country_code"]].append(row)
    changes, endpoints = [], []
    for code, rows in sorted(grouped.items()):
        rows.sort(key=lambda row: row["year"])
        for previous, current in zip(rows, rows[1:]):
            if current["year"] - previous["year"] == 1:
                changes.append({
                    "country_code": code, "country_name": current["country_name"],
                    "year": current["year"], "previous_year": previous["year"],
                    "democracy_score": current["democracy_score"],
                    "previous_score": previous["democracy_score"],
                    "score_change": round(current["democracy_score"] - previous["democracy_score"], 10),
                    "regime_previous": previous["regime"], "regime": current["regime"],
                })
        lookup = {row["year"]: row for row in rows}
        if 2006 in lookup and 2022 in lookup:
            first, last = lookup[2006], lookup[2022]
            endpoints.append({"country_code": code, "country_name": last["country_name"],
                              "score_2006": first["democracy_score"],
                              "score_2022": last["democracy_score"],
                              "change_2006_2022": round(last["democracy_score"] - first["democracy_score"], 10),
                              "regime_2006": first["regime"]})
    return changes, endpoints


def profile(rows):
    fields = {}
    for name in rows[0]:
        values = [row[name] for row in rows if row[name] is not None]
        result = {"missing": len(rows) - len(values)}
        if values:
            kind = type(values[0]).__name__
            result["type"] = kind
            if kind in ("int", "float"):
                result.update(min=min(values), max=max(values))
            else:
                result["distinct"] = len(set(values))
        fields[name] = result
    return {"rows": len(rows), "fields": fields}


def write_csv(name, rows):
    with (OUT / name).open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)


def write_reports(audit, manifest):
    for name, value in [("audit.json", audit), ("source_manifest.json", manifest)]:
        (OUT / name).write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    lines = ["# Rebuilt data audit", "", "Generated by `python3 build_data.py` from verified repository snapshots.",
             "", YEAR_NOTE, "", "## Source and coverage counts", "",
             f"- EIU raw rows: {audit['raw_eiu_rows']}; country rows: {audit['country_rows']}; aggregate rows: {audit['aggregate_rows']}.",
             f"- Development rows: {audit['development_rows']}; file-label years: {audit['common_file_label_years']}.",
             f"- Duplicate keys: {audit['duplicate_keys']}; unexpected numeric values stop the build.",
             "", "| EIU year | Country rows |", "| --- | ---: |"]
    lines.extend(f"| {year} | {count} |" for year, count in audit["country_rows_by_year"].items())
    lines += ["", "## Join audits", "",
              "A matched country code can still have missing HDI/IHDI. Counts below distinguish these cases.", "",
              "| Democracy year | EIU before | Development before | Matched per side | EIU unmatched | Development unmatched | Left-join rows | HDI usable | HDI + IHDI usable |",
              "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |"]
    for year, join in audit["joins"].items():
        lines.append(f"| {year} | {join['eiu_rows_before']} | {join['development_rows_before']} | {join['matched_from_eiu']} | {join['eiu_unmatched_count']} | {join['development_unmatched_count']} | {join['left_join_rows_after']} | {join['usable_hdi_rows']} | {join['usable_hdi_ihdi_rows']} |")
    coverage = audit["coverage_comparison"]
    lines += ["", "All joins use standardized `country_code` after the year filters described in `build_data.join_development`.",
              "Full unmatched country lists, missingness, name disagreements and observed ranges are in `audit.json`.",
              "", "## The 2023 coverage gap", "",
              f"The file omits {coverage['missing_2023_country_count']} countries in 2023 compared with 2022. All {coverage['missing_2023_authoritarian_in_2022']} had 2022 scores at or below 4.",
              f"Unbalanced mean: 2022 ({coverage['all_2022_country_count']} countries) = {coverage['all_2022_mean']:.6f}; 2023 ({coverage['all_2023_country_count']} countries) = {coverage['all_2023_mean']:.6f}.",
              f"Same {coverage['balanced_country_count']} countries in both years: 2022 = {coverage['balanced_2022_mean']:.6f}; 2023 = {coverage['balanced_2023_mean']:.6f}.",
              "The unbalanced change mixes real score changes with a change in which countries are present. The publisher's complete 2023 coverage cannot be inferred from this snapshot.",
              "", f"RQ2: {audit['rq2_annual_changes']} consecutive one-year changes; {audit['rq2_endpoint_rows']} endpoint countries.",
              "The two-year gaps before 2010 are excluded from annual-change calculations.", "",
              "## Reuse and provenance", "",
              "Original acquisition dates and acquired version IDs were not recorded. Currently observed source versions, byte counts and SHA-256 hashes are in `source_manifest.json`.",
              "These outputs inherit upstream restrictions; creating a processed CSV does not grant a new redistribution license.",
              "The build reproduces tables from repository CSVs, not EIU assessments or underlying UNDP survey microdata.", ""]
    (OUT / "audit.md").write_text("\n".join(lines), encoding="utf-8")
    (OUT / "README.md").write_text(
        "# Generated analysis tables\n\nRebuild with `python3 build_data.py` from the repository root (Python 3.9+, standard library only). "
        "Do not hand-edit these outputs. See `audit.md`, `audit.json`, `source_manifest.json` and the repository datasheet for provenance, schemas and limitations.\n\n"
        "Empty CSV fields represent missing values; booleans are `True`/`False`. "
        "The CSVs can be loaded into a dataframe with `pandas.read_csv`, if pandas is installed. "
        "`rq1_2022_all.csv` preserves all 167 EIU countries, `rq1_2022_hdi.csv` requires HDI, and `rq1_2022_ihdi.csv` requires both HDI and IHDI. "
        "`rq1_2023_sensitivity.csv` preserves the smaller 2023 EIU frame; filter its missing measures explicitly.\n\n"
        "The 2023 development file label is preserved as `hdi_file_year`; `development_reference_year=2022` identifies the UNDP report estimates. "
        "`embedded_democracy_score` is retained only for source auditing; the joined `democracy_score` comes from the EIU panel.\n\n"
        "**Reuse:** Derived data retain upstream restrictions. No new data license or permission to redistribute EIU values is granted here. "
        "This pipeline reconstructs tables from the preserved publisher CSV snapshots, not from proprietary assessments or original survey/administrative microdata.\n",
        encoding="utf-8")


def main():
    raw, manifest = read_sources()
    countries, aggregates = clean_eiu(raw["democracy-index-eiu.csv"])
    development = clean_development(raw["hdi-ihdi-democracy-by-country.csv"])
    joined_2022, hdi_2022, ihdi_2022, audit_2022 = join_development(countries, development, 2022)
    joined_2023, _, _, audit_2023 = join_development(countries, development, 2023)
    changes, endpoints = historical_tables(countries)
    democracy_2023 = {row["country_code"]: row["democracy_score"] for row in countries if row["year"] == 2023}
    embedded = [row for row in development if row["embedded_democracy_score"] is not None]
    if any(row["country_code"] not in democracy_2023 or
           abs(democracy_2023[row["country_code"]] - row["embedded_democracy_score"]) > 1e-12 for row in embedded):
        raise ValueError("Embedded development democracy scores disagree with EIU 2023")
    outputs = {
        "panel_country.csv": countries, "panel_aggregates.csv": aggregates,
        "development_clean.csv": development,
        "rq1_2022_all.csv": joined_2022, "rq1_2022_hdi.csv": hdi_2022,
        "rq1_2022_ihdi.csv": ihdi_2022, "rq1_2023_sensitivity.csv": joined_2023,
        "rq2_changes.csv": changes, "rq2_endpoints.csv": endpoints,
    }
    counts = Counter(row["year"] for row in countries)
    keys_2022 = {row["country_code"] for row in countries if row["year"] == 2022}
    keys_2023 = {row["country_code"] for row in countries if row["year"] == 2023}
    names = {row["country_code"]: row["country_name"] for row in countries}
    scores_2022 = {row["country_code"]: row["democracy_score"] for row in countries if row["year"] == 2022}
    scores_2023 = {row["country_code"]: row["democracy_score"] for row in countries if row["year"] == 2023}
    balanced_keys = keys_2022 & keys_2023
    audit = {
        "raw_eiu_rows": len(raw["democracy-index-eiu.csv"]), "country_rows": len(countries),
        "aggregate_rows": len(aggregates), "development_rows": len(development),
        "country_rows_by_year": dict(sorted(counts.items())), "distinct_country_codes": len(names),
        "common_file_label_years": sorted(set(counts) & {row["hdi_file_year"] for row in development}),
        "year_semantics": YEAR_NOTE, "duplicate_keys": 0,
        "missing_calendar_years_in_eiu": sorted(set(range(min(counts), max(counts) + 1)) - set(counts)),
        "countries_missing_2023_vs_2022": [{"country_code": code, "country_name": names[code]}
                                            for code in sorted(keys_2022 - keys_2023)],
        "coverage_comparison": {
            "missing_2023_country_count": len(keys_2022 - keys_2023),
            "missing_2023_authoritarian_in_2022": sum(scores_2022[code] <= 4 for code in keys_2022 - keys_2023),
            "all_2022_country_count": len(keys_2022), "all_2023_country_count": len(keys_2023),
            "all_2022_mean": mean(scores_2022.values()), "all_2023_mean": mean(scores_2023.values()),
            "balanced_country_count": len(balanced_keys),
            "balanced_2022_mean": mean(scores_2022[code] for code in sorted(balanced_keys)),
            "balanced_2023_mean": mean(scores_2023[code] for code in sorted(balanced_keys)),
        },
        "joins": {"2022": audit_2022, "2023": audit_2023},
        "embedded_democracy_matches_2023": len(embedded),
        "rq2_annual_changes": len(changes), "rq2_endpoint_rows": len(endpoints),
        "rq2_declined": sum(row["change_2006_2022"] < 0 for row in endpoints),
        "rq2_improved": sum(row["change_2006_2022"] > 0 for row in endpoints),
        "rq2_unchanged": sum(row["change_2006_2022"] == 0 for row in endpoints),
        "raw_missing_tokens": {
            "development_IHDI": dict(sorted(Counter(row["IHDI"] for row in raw["hdi-ihdi-democracy-by-country.csv"] if row["IHDI"] in ("", "..")).items())),
            "eiu_Code_blank": sum(not row["Code"] for row in raw["democracy-index-eiu.csv"]),
        },
        "output_profiles": {name: profile(rows) for name, rows in outputs.items()},
    }
    OUT.mkdir(exist_ok=True)
    for name, rows in outputs.items():
        write_csv(name, rows)
    write_reports(audit, manifest)
    print(f"Built {len(outputs)} CSV tables in {OUT}")
    for year, join in audit["joins"].items():
        print(f"{year}: matched {join['matched_from_eiu']}; EIU unmatched {join['eiu_unmatched_count']}; "
              f"development unmatched {join['development_unmatched_count']}; "
              f"HDI usable {join['usable_hdi_rows']}; HDI/IHDI usable {join['usable_hdi_ihdi_rows']}")
    print(f"RQ2: {len(changes)} one-year changes; {len(endpoints)} endpoint countries")


if __name__ == "__main__":
    main()
