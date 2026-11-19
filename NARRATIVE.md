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

In 2022, countries with higher EIU democracy scores generally also had higher human-development scores. This pattern appears for both the regular Human Development Index (HDI; $r = 0.698, p = 2.91 \times 10^{-23}$) and the inequality-adjusted HDI (IHDI; $r = 0.671, p = 6.16 \times 10^{-21}$). These correlations use the 150 countries with complete records. However, the relationship changes around a democracy score of 6.0.

Below 6.0, countries are generally classified as hybrid or authoritarian regimes. In this group, a higher democracy score was not clearly linked to higher HDI or IHDI: each one-point increase corresponded to only a $+0.019$ HDI change ($95\%\text{ CI } [-0.001, 0.039], p = 0.065$) and a $+0.018$ IHDI change ($95\%\text{ CI } [-0.007, 0.042], p = 0.153$). The confidence ranges include zero, so these results do not show a reliable increase.

Countries with scores of 6.0 or higher had a much higher average HDI: $0.837$ ($95\%\text{ CI } [0.811, 0.862], n = 71$), compared with $0.639$ ($95\%\text{ CI } [0.611, 0.667], n = 94$) for countries below 6.0. Above the threshold, the relationship between democracy and development also became steeper. The increase in the HDI trend was $+0.049$ per democracy point, and the increase in the IHDI trend was $+0.069$; both were statistically significant ($p < 0.001$).

Inequality makes the difference between the two groups larger. The average HDI gap across the 6.0 threshold was $+0.198$, while the IHDI gap was $+0.265$. This is because inequality reduced development scores more in non-democracies ($0.154$) than in democracies ($0.107$). Across countries, greater inequality-related losses were also associated with lower democracy scores ($r = -0.433, p = 3.07 \times 10^{-8}$).

Some wealthy countries with low democracy scores could affect this pattern. Twelve countries below 6.0 had high HDI scores ($\ge 0.80$), including six Gulf oil-rich states and Hong Kong. Also, 15 countries—including Bahrain, Qatar, Saudi Arabia, and Kuwait—had no IHDI data. To check whether these wealthy countries explain the results, the analysis was repeated for all 165 countries with HDI and EIU scores after removing the 12 high-HDI countries. The relationship below 6.0 remained weak ($+0.015$, $p = 0.087$), while the jump at 6.0 became clearer ($+0.085$, $p = 0.007$). The relationship above 6.0 also remained steeper ($+0.054$, $p < 0.001$). So, these wealthy countries do not appear to explain the threshold pattern.

These results show that democracy scores and human development are associated, especially above a score of 6.0. But because the data cover only one year, they cannot tell us whether democracy improves living standards or whether higher, more equal living standards help democracy grow. The findings show a relationship, not proof of cause and effect.

![Human Development Gains Accelerate Above a Democracy Score of 6.0](Checkpoint%206%20-%20Narrative%20Analysis/fig_sai_democracy_hdi_threshold.png)

### Daniel’s Finding: Hybrid-Regime Variation

To compare how much democracy scores changed from year to year, I calculated each country's average yearly movement from 2011 to 2022. Increases and decreases both count as movement. Countries were grouped by their EIU regime type in 2010, before the years being compared, and each country counted once. Hybrid regimes had the largest typical movement: their median was 0.150 points (31 countries), compared with 0.090 points for all other regime types combined. The difference was 0.060 points (95% bootstrap confidence interval: [0.011, 0.098]; p = 0.00015). The hybrid-regime median was about 2.4 times the full-democracy median of 0.063. The difference was statistically clear compared with flawed and full democracies, but not quite compared with authoritarian regimes (p = 0.0535).

More movement does not necessarily mean improvement. For countries classed as hybrid in 2010, the median total score change over the period was -0.42 points, and 58.1% had a net decline. Of the 37 one-year changes of at least 0.5 points that occurred while a country was classed as hybrid, 22 were declines.

The pattern remained when the six countries with a one-year change of at least 1.5 points were excluded: the hybrid-regime median stayed at 0.150. It was also present after excluding 2020 and 2021, when the median was 0.132. In separate periods, the median was 0.110 in 2011–2016 and 0.148 in 2017–2022. However, score movement was also greater for countries whose 2010 scores were closer to 5 (Spearman correlation: $\rho = -0.48$, $p = 3.7 \times 10^{-11}$). Since 5 is near the middle of the EIU scale, this suggests that a country's starting score may help explain why hybrid regimes showed more movement. These results describe score changes, but do not by themselves explain what caused them.

![Typical Year-to-Year Democracy Score Movement by 2010 Regime Type](Checkpoint%206%20-%20Narrative%20Analysis/figures/daniel_hybrid_variation.png)