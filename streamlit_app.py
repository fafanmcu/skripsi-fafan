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

# Insert containers separated into tabs:
tab1, tab2 = st.tabs(["Tab 1", "Tab2"])
tab1.write("this is tab 1")
tab2.write("this is tab 2")

# You can also use "with" notation:
with tab1:
  st.radio('Select one:', [1, 2])

# Insert a chat message container.
with st.chat_message("user"):
  st.write("Hello 👋")
  st.line_chart(np.random.randn(30, 3))

# Display a chat input widget.
st.chat_input("Say something")
