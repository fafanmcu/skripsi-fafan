import streamlit as st
import pandas as pd

st.title('🎈 Analisis Sentimen Pemindahan Ibu Kota Negara ke Ibu Kota Nusantara Menggunakan Metode Naive Bayes')
st.info('Fafan Maulana Cahya Utama')

data = pd.read_excel('ikn-maret-juni-dengan-label.xlsx')

mapping = {1: 'Positif', 2: 'Negatif'}
# mengubah nilai kolom dan menghapus sentimen yang kosong
df = data.dropna(subset=['Sentimen'])
df['Sentimen'] = df['Sentimen'].map(mapping)
df = df.reset_index(drop=True)
df
