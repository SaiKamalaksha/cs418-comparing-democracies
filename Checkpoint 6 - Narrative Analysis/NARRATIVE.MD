# Main Findings (Narrative Analysis)

- **Finding 1 (Democracy & Human Development Threshold):** Across 150 countries with complete 2022 EIU and UNDP records, human development exhibits no statistically significant relationship with democracy below an EIU score of 6.0, but rises sharply above the 6.0 threshold—a divergence that widens when accounting for inequality via IHDI.
- **Finding 2 (2006–2022 Democracy Decline — Don):** *[Insert Don's one-sentence falsifiable claim here.]*
- **Finding 3 (Hybrid-Regime Annual Variation — Daniel):** *[Insert Daniel's one-sentence falsifiable claim here.]*

---

## 1. Democracy Score Thresholds and Human Development (2022)
**Author:** Sai  
**Notebook:** `Checkpoint 6 - Narrative Analysis/sai_narrative.ipynb`

In 2022, countries with higher EIU democracy scores generally also had higher human-development scores. This pattern appears for both the regular Human Development Index (HDI; $r = 0.698, p = 2.91 \times 10^{-23}$) and the inequality-adjusted HDI (IHDI; $r = 0.671, p = 6.16 \times 10^{-21}$). These correlations use the 150 countries with complete records. However, the relationship changes around a democracy score of 6.0.

Below 6.0, countries are generally classified as hybrid or authoritarian regimes. In this group, a higher democracy score was not clearly linked to higher HDI or IHDI: each one-point increase corresponded to only a $+0.019$ HDI change ($95\%\text{ CI } [-0.001, 0.039], p = 0.065$) and a $+0.018$ IHDI change ($95\%\text{ CI } [-0.007, 0.042], p = 0.153$). The confidence ranges include zero, so these results do not show a reliable increase.

Countries with scores of 6.0 or higher had a much higher average HDI: $0.837$ ($95\%\text{ CI } [0.811, 0.862], n = 71$), compared with $0.639$ ($95\%\text{ CI } [0.611, 0.667], n = 94$) for countries below 6.0. Above the threshold, the relationship between democracy and development also became steeper. The increase in the HDI trend was $+0.049$ per democracy point, and the increase in the IHDI trend was $+0.069$; both were statistically significant ($p < 0.001$).

Inequality makes the difference between the two groups larger. The average HDI gap across the 6.0 threshold was $+0.198$, while the IHDI gap was $+0.265$. This is because inequality reduced development scores more in non-democracies ($0.154$) than in democracies ($0.107$). Across countries, greater inequality-related losses were also associated with lower democracy scores ($r = -0.433, p = 3.07 \times 10^{-8}$).

Some wealthy countries with low democracy scores could affect this pattern. Twelve countries below 6.0 had high HDI scores ($\ge 0.80$), including six Gulf oil-rich states and Hong Kong. Also, 15 countries—including Bahrain, Qatar, Saudi Arabia, and Kuwait—had no IHDI data. To check whether these wealthy countries explain the results, the analysis was repeated for all 165 countries with HDI and EIU scores after removing the 12 high-HDI countries. The relationship below 6.0 remained weak ($+0.015$, $p = 0.087$), while the jump at 6.0 became clearer ($+0.085$, $p = 0.007$). The relationship above 6.0 also remained steeper ($+0.054$, $p < 0.001$). So, these wealthy countries do not appear to explain the threshold pattern.

These results show that democracy scores and human development are associated, especially above a score of 6.0. But because the data cover only one year, they cannot tell us whether democracy improves living standards or whether higher, more equal living standards help democracy grow. The findings show a relationship, not proof of cause and effect.

![Human Development Gains Accelerate Above a Democracy Score of 6.0](Checkpoint%206%20-%20Narrative%20Analysis/fig_sai_democracy_hdi_threshold.png)

---

## 2. Democracy Score Declines and Geographic Patterns (2006–2022)
**Author:** Don  
**Notebook:** `Checkpoint 6 - Narrative Analysis/don_narrative.ipynb`

*[Paste Don's connected paragraph here.]*

![Don's Figure Title](Checkpoint%206%20-%20Narrative%20Analysis/fig_don_placeholder.png)

---

## 3. Hybrid Regimes and Annual Score Variation (2006–2022)
**Author:** Daniel  
**Notebook:** `Checkpoint 6 - Narrative Analysis/daniel_narrative.ipynb`

*[Paste Daniel's connected paragraph here.]*

![Daniel's Figure Title](Checkpoint%206%20-%20Narrative%20Analysis/fig_daniel_placeholder.png)