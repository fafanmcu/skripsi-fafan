import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dashboard Sentimen Analisis Pemindahan Ibu Kota Negara ke Ibu kota Nusantara",
    page_icon=":glass:",
    layout="wide",  # Use "wide" layout for a full-size dashboard
)

data = pd.read_excel('ikn-maret-juni-dengan-label.xlsx')

# mengubah nilai kolom dan menghapus sentimen yang kosong
mapping = {1: 'Positif', 2: 'Negatif'}
df = data.dropna(subset=['Sentimen'])
df['Sentimen'] = df['Sentimen'].map(mapping)

# mengurutkan nomer index
df = df.reset_index(drop=True)
df.index = df.index + 1

# menghapus data duplikat
df = df.drop_duplicates(subset=['Stemming'])

# Insert containers separated into tabs:
tab1, tab2 = st.tabs(["Ringkasan", "Dataset"])
tab1.write("this is tab 1")
tab2.write(df)
