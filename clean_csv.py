import pandas as pd
csv = pd.read_csv("ARK_dino.csv")
print(csv.head())
csv = csv.drop(columns= ['Unnamed: 0'])
csv= csv.drop(columns=['Unnamed: 0.1','Released','Unnamed: 0.2','Unnamed: 0','Id'])
print(csv.head())
csv.to_csv("ARK_dino.csv")
