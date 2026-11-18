# Checkpoint 6 Narrative Analysis

This is the combined narrative for the group’s three findings. Each member contributes one completed finding from an individual notebook, including evidence, uncertainty, a break attempt, a figure, and a limitation. Sai performs final integration and ordering.

## Core Research Questions

1. How are 2022 EIU democracy scores related to HDI and IHDI, including differences around a democracy score of 6?
2. Which countries and published geographic averages declined from 2006 through 2022, and do hybrid regimes show greater annual score variation?

## Main Findings

### Don’s Finding: Democracy Decline

Among a transparent, country-level North American comparison, the 12 selected countries in `all_else` lost an average **0.89 EIU democracy-score points** from 2006 to 2022, compared with **0.28 points** for Canada and the United States (`usa_can`). Ten of the 12 `all_else` countries declined (while Costa Rica and the Dominican Republic improved); the two groups changed similarly through 2014 (mean changes −0.08 and −0.05), but the later 2014–2022 change was markedly more negative for `all_else` (−0.81 versus −0.23). This is a descriptive comparison reconstructed from country rows—not a published regional average—and a leave-one-country-out check keeps the `all_else` mean decline negative (**−0.99 to −0.68**) even when Nicaragua, its largest decline, is omitted. Thus the result is not solely an artifact of that country, but it does not establish that geography or any event caused the score changes. The groups are deliberately defined rather than exhaustive, the scores are country-level EIU measures rather than population-weighted regional estimates, and the panel lacks 2007 and 2009 observations; the data describe movement in the EIU measure and cannot explain why it occurred. The reproducible code, membership audit, endpoint tables, and checks are in `Checkpoint 6 - Narrative Analysis/don_narrative.ipynb`.

![Two-panel bars show the score changes, split into declining and improving countries.](Checkpoint%206%20-%20Narrative%20Analysis/figures/don_north_america_score_change_2006_2022.png)

### Sai’s Finding: HDI/IHDI Relationship

_Add the claim, evidence, uncertainty, alternative explanation, break attempt, interpretation, limitation, and figure from `sai_narrative.ipynb`._

### Daniel’s Finding: Hybrid-Regime Variation

_Add the claim, evidence, uncertainty, alternative explanation, break attempt, interpretation, limitation, and figure from `daniel_narrative.ipynb`._
