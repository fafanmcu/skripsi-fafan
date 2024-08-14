import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Dashboard Sentimen Analisis Pemindahan Ibu Kota Negara ke Ibu kota Nusantara",
    page_icon=":eyes:",
    layout="wide",  # Use "wide" layout for a full-size dashboard
)

st.header('Sentimen Analisis Pemindahan Ibu Kota Negara ke Ibu Kota Nusantara')
st.markdown("""---""")

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

nav1, nav2 = st.columns(2)
with nav1:
    jenis_sentimen = st.multiselect("Jenis Sentimen", options = df["Sentimen"].unique(), default = df["Sentimen"].unique())
with nav2:
    df['Tgl'] = pd.to_datetime(df['created_at']).dt.date
    start = df['Tgl'].min()
    finish = df['Tgl'].max()
    start_date, end_date = st.date_input('Rentang Waktu',
                               (start, finish), 
                               start, 
                               finish,
                               format="YYYY.MM.DD")

# filter Tgl
output = (df['Tgl'] >= start_date) & (df['Tgl'] <= end_date)

# filter sumber, tamggal dan sentiment
df_selection = df.query("Sentimen == @jenis_sentimen").loc[output]

# Insert containers separated into tabs:
tab1, tab2 = st.tabs(["Ringkasan", "Dataset"])
with tab1:
    st.write('test')
with tab2:
    df
