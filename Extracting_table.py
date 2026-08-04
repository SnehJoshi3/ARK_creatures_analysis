import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
from io import StringIO
from bs4 import BeautifulSoup
import streamlit as st

html_content = """ html_content for extracting the table"""

dfs = pd.read_html(StringIO(html_content))

df = dfs[1]
print(df.head(5))
df.to_excel('ARK_dino.xlsx')

# Unique Temparaments to list
li = df['Temperament'].unique().tolist()
print(li)
