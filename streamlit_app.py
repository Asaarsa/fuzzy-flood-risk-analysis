import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Judul Utama
st.set_page_config(page_title="Analisis Risiko Banjir Fuzzy", layout="wide")
st.title("🌊 Dashboard Analisis Risiko Banjir")
st.markdown("### Metode: Fuzzy Logic (Curah Hujan & Wilayah Rawan)")

# --- SIDEBAR: INPUT DATA ---
st.sidebar.header("Input Parameter")
curah_hujan = st.sidebar.slider("Curah Hujan (mm/hari)", 0, 500, 150)
kerawanan = st.sidebar.slider("Skor Kerawanan Wilayah (1-10)", 1, 10, 5)

# --- LOGIKA FUZZY (Placeholder) ---
# Di sini nanti kamu masukkan fungsi skfuzzy milikmu
def hitung_risiko(hujan, rawan):
    # Contoh logika sederhana untuk simulasi visualisasi
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
    # Visualisasi Gauge atau Bar Sederhana menggunakan Plotly
    fig = px.bar(x=[kategori], y=[curah_hujan], color=[kategori],
                 color_discrete_map={"Rendah": "green", "Sedang": "orange", "Tinggi": "red"},
                 labels={'x': 'Kategori Risiko', 'y': 'Intensitas'},
                 title="Visualisasi Level Risiko")
    st.plotly_chart(fig, use_container_width=True)

# --- BAGIAN DATA WILAYAH (Contoh Dataframe) ---
st.divider()
st.subheader("📍 Peta Sebaran Risiko Wilayah")

# Contoh data dummy wilayah
df_wilayah = pd.DataFrame({
    'Kecamatan': ['A', 'B', 'C', 'D'],
    'Lat': [-6.2, -6.21, -6.19, -6.22],
    'Lon': [106.8, 106.81, 106.82, 106.79],
    'Risiko': [80, 40, 95, 20]
})

# Menampilkan Peta
st.map(df_wilayah)

# Menampilkan Tabel Data
st.dataframe(df_wilayah, use_container_width=True)
