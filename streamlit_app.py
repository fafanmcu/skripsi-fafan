import streamlit as st
import pandas as pd

st.title('🎈 Analisis Sentimen Pemindahan Ibu Kota Negara ke Ibu Kota Nusantara Menggunakan Metode Naive Bayes')
st.info('Fafan Maulana Cahya Utama')

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
df
