# Don — Checkpoint 6 Current Task

## Scope

Own the Checkpoint 6 finding about democracy decline/stability in the EIU panel from 2006 through 2022. This is the Don-specific assignment in `intake_NOCOMMIT/checkpoint-narrative-work-breakdown-draft.md`; the shared checkpoint requirements and rubric are also summarized there.

The finding must answer the second research question in a specific, falsifiable way: which countries and published geographic averages declined from 2006 through 2022, and what does that pattern mean?

Use association/description language only. The EIU country averages and the available time series cannot establish that a particular factor caused a decline.

## Required deliverables

Complete these in the Don branch and individual notebook `Checkpoint 6 - Narrative Analysis/don_narrative.ipynb`:

- State one specific finding about country-level decline, stability, or geographic averages between 2006 and 2022.
- Produce named evidence with interpretable metrics and uncertainty. At minimum, report the number/proportion of countries that declined, improved, or were unchanged and the size of the relevant change; use an interval, bootstrap result, subgroup spread, or another honest uncertainty measure where appropriate.
- Compare a meaningful subgroup or time window so the finding says more than simply “scores went down.” Possible checks include regime category, starting score, continent/geographic average, or early versus late period. Choose the comparison that is supported by the data and explain why.
- Include at least one plausible alternative explanation or data concern and run a check intended to break the finding. The known high-priority check is to rebuild regional results from the same country-only rows and definitions because prior EDA noted conflicting regional plots. Also consider whether missing years (2007 and 2009), country coverage, aggregate rows, or starting-score regression to the mean could change the result.
- Create one polished, story-oriented figure. Its title must state the point, not merely name the variables. Save it under `Checkpoint 6 - Narrative Analysis/figures/` with a Don-specific filename.
- Add one connected paragraph to the Don section of the root `NARRATIVE.md` under “Don’s Finding: Democracy Decline.” The paragraph must connect the claim, evidence, uncertainty, alternative explanation, break attempt, interpretation, and limitation. Do not leave the placeholder text in place.
- Make every number and figure in the narrative traceable to executable notebook code. Run the notebook from top to bottom after the analysis is complete and verify the saved figure.
- Commit the notebook, figure, and narrative contribution on the Don branch with a checkpoint-scoped message. Send Sai the commit hash and a short handoff note so the work can be merged and integrated.

## Current implementation status

Implemented the focused North America endpoint analysis in `Checkpoint 6 - Narrative Analysis/don_narrative.ipynb`: `build_country_split(eiu)` validates country rows, the 14-country membership, 2006/2014/2022 endpoints, score bounds, display exhaustion, and group assignment. The notebook saves `figures/don_north_america_score_change_2006_2022.png`; the completed narrative paragraph and figure link are in `NARRATIVE.md`. The original exploratory “Approach / Thoughts” and “P1” markdown cells have been restored ahead of the completed analysis. The notebook was rerun top-to-bottom after the implementation and is ready for the requested commit/handoff.

## Evidence and interpretation guidance

Start from the cleaned EIU panel in `democracy-index-eiu.csv`, excluding world/continent aggregate rows for country comparisons while retaining a separately documented geographic-average analysis if used. The panel has missing years 2007 and 2009, so define “2006–2022 change” explicitly and do not silently treat non-adjacent observations as adjacent annual changes. Use the repository’s existing cleaning conventions or reproduce them transparently in the notebook.

The prior EDA gives useful leads, not final claims: 99 countries declined, 66 improved, and 2 were unchanged from 2006 to 2022; the world score fell from about 5.52 to 5.29; and regional results previously conflicted. Recompute these quantities from the current source and document the exact country count, filters, and calculation before relying on them.

Explain what the score movement could mean substantively, what remains unexplained, and whether the pattern is robust to the chosen subgroup/time window. A score decline is evidence of a change in the EIU measure, not proof of democratic backsliding caused by a particular institution, election, income level, or geography. The available `elections.csv` is U.S.-presidential data and cannot support a cross-country voting explanation.

## Shared checkpoint obligations

The team must ultimately have two to four findings, one figure and one evidence paragraph per finding, alternative explanations and checks for each, a README narrative section, reproducible code, and at least one meaningful commit from each member. Sai owns final integration and ordering; Daniel owns the hybrid-regime annual-variation finding. Don should review the integrated narrative for consistency and verify that the final README numbers and figure links still match the notebook.

## Reference files

- Assignment, feedback, individual checklist, and rubric: `intake_NOCOMMIT/checkpoint-narrative-work-breakdown-draft.md`
- Checkpoint description and grading requirements: `intake_NOCOMMIT/checkpoint-5-description.md`
- Existing EDA caveats and leads: `EDA.md`
- Combined narrative placeholder: `NARRATIVE.md`
- Data definitions and provenance: `DATASHEET.md`
- Don’s working notebook: `Checkpoint 6 - Narrative Analysis/don_narrative.ipynb`
