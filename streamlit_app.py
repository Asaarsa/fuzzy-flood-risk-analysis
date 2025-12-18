import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Judul Utama
st.set_page_config(page_title="Analisis Risiko Banjir Batam", layout="wide")
st.title("🌊 Dashboard Analisis Risiko Banjir Kota Batam")
st.markdown("### Metode: Fuzzy Logic & Analisis Dampak Ekonomi")

# --- SIDEBAR: INPUT DATA ---
st.sidebar.header("Input Parameter")
curah_hujan = st.sidebar.slider("Curah Hujan (mm/hari)", 0, 500, 150)
kerawanan = st.sidebar.slider("Skor Kerawanan Wilayah (1-10)", 1, 10, 5)

# --- LOGIKA FUZZY (Placeholder) ---
def hitung_risiko(hujan, rawan):
    skor = (hujan * 0.6) + (rawan * 4) 
    if skor < 100: return "Rendah", "green"
    elif skor < 200: return "Sedang", "orange"
    else: return "Tinggi", "red"

kategori, warna = hitung_risiko(curah_hujan, kerawanan)

# --- DISPLAY HASIL ---
col1, col2 = st.columns(2)

with col1:
    st.metric(label="Status Risiko", value=kategori)
    st.info(f"Berdasarkan input, wilayah ini masuk kategori risiko {kategori}.")

with col2:
    fig = px.bar(x=[kategori], y=[curah_hujan], color=[kategori],
                 color_discrete_map={"Rendah": "green", "Sedang": "orange", "Tinggi": "red"},
                 labels={'x': 'Kategori Risiko', 'y': 'Intensitas'},
                 title="Visualisasi Level Risiko")
    st.plotly_chart(fig, use_container_width=True)

# --- BAGIAN DATA WILAYAH KOTA BATAM ---
st.divider()
st.subheader("📍 Peta Sebaran Risiko Wilayah Kota Batam")

# Data koordinat kecamatan di Kota Batam
df_batam = pd.DataFrame({
    'Kecamatan': [
        'Batam Kota', 'Nagoya (Lubuk Baja)', 'Batu Ampar', 'Sekupang', 
        'Batu Aji', 'Sagulung', 'Nongsa', 'Bengkong'
    ],
    'lat': [
        1.1283, 1.1444, 1.1500, 1.1167, 
        1.0500, 1.0333, 1.1833, 1.1389
    ],
    'lon': [
        104.0525, 104.0147, 103.9833, 103.9333, 
        103.9500, 103.9667, 104.1000, 104.0278
    ],
    'Tingkat Risiko (%)': [85, 45, 90, 30, 75, 80, 20, 65]
})

# Menampilkan Peta (Streamlit otomatis memusatkan ke Batam berdasarkan data ini)
st.map(df_batam)

# Menampilkan Tabel Data
st.write("Data Detail Wilayah Batam:")
st.dataframe(df_batam, use_container_width=True)
