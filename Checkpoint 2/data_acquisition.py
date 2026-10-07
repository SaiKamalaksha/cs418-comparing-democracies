import pandas as pd

electionsDf = pd.read_csv("elections.csv")
eiuDf = pd.read_csv("democracy-eiu.csv")
indexEiusDf = pd.read_csv("democracy-index-eiu.csv")
hdiDf = pd.read_csv("hdi-ihdi-democracy-by-country.csv")

print(electionsDf.shape)
print(eiuDf.shape)
print(indexEiusDf.shape)
print(hdiDf.shape)
