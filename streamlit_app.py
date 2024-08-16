import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score, KFold, train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, precision_score, recall_score, f1_score
import seaborn as sns


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
    df['created_at'] = pd.to_datetime(df['created_at']).dt.date
    start = df['created_at'].min()
    finish = df['created_at'].max()
    start_date, end_date = st.date_input('Rentang Waktu',
                               (start, finish), 
                               start, 
                               finish,
                               format="YYYY.MM.DD")

# filter Tgl
output = (df['created_at'] >= start_date) & (df['created_at'] <= end_date)

# filter sumber, tamggal dan sentiment
df_selection = df.query("Sentimen == @jenis_sentimen").loc[output]

# Insert containers separated into tabs:
tab1, tab2 = st.tabs(["Ringkasan", "Dataset"])
with tab1:
    pos = df_selection['Sentimen'].loc[df_selection['Sentimen'] == 'Positif']
    neg = df_selection['Sentimen'].loc[df_selection['Sentimen'] == 'Negatif']
    count = len(df_selection)
    
    b1, b2, b3 = st.columns([0.45,0.45,0.45])
    b1.metric("Jumlah Komentar", len(pos), "+ Positif")
    b2.metric("Jumlah Komentar", len(neg), "- Negatif")
    b3.metric("Jumlah", count)

    # garis 
    st.markdown("""---""")
    
with tab2:
    df_selection

nav3, nav4 = st.columns(2)
with nav3:
    # Visualisasi hasil sentiment
    color_custom = ['#e14b32', '#3ca9ee']
    Sentimen = df_selection['Sentimen'].value_counts()
    fig_sentiment = go.Figure()

    neg_df = df_selection[df_selection['Sentimen'] == 'Negatif']
    pos_df = df_selection[df_selection['Sentimen'] == 'Positif']
        
    if not neg_df.empty:
        color = ['#e14b32']
        fig_sentiment.add_trace(go.Pie(labels=['Negatif'], values=neg_df['Sentimen'].value_counts(), 
                                        marker_colors=color, textinfo='label+percent', 
                                        hoverinfo='label+value', hole=0.3))
    if not pos_df.empty:
        color = ['#3ca9ee']
        fig_sentiment.add_trace(go.Pie(labels=['Positif'], values=pos_df['Sentimen'].value_counts(), 
                                        marker_colors=color, textinfo='label+percent', 
                                        hoverinfo='value', hole=0.3))
    if not neg_df.empty and not pos_df.empty:
        fig_sentiment.add_trace(go.Pie(labels=['Negatif','Positif'], values=Sentimen,
                                      marker_colors=color_custom, textinfo='label+percent',
                                      hoverinfo='value', hole=0.3))
        
    fig_sentiment.update_layout(title="Persentase Sentimen Twitter")
    st.plotly_chart(fig_sentiment, use_container_width=True)


with nav4:
    tgl_counts = df_selection['created_at'].value_counts().reset_index()
    tgl_counts.columns = ['created_at', 'Count']
    custom_colors = ['#dc6e55']
    fig_tgl = px.area(tgl_counts, x='created_at', y='Count', title="Rentang Waktu Komentar", color_discrete_sequence=custom_colors)
    st.plotly_chart(fig_tgl, use_container_width=True)

st.markdown("""---""")
kf_fold = st.selectbox("Pilih Jumlah Lipatan","1","2","3","4","5")
tab3, tab4 = st.tabs(["TF", "TF-IDF"])
with tab3:
    st.write("TF")
with tab4:
    st.write("TF-IDF")
