import streamlit as st
import pandas as pd
import plotly.express as px


st.title("Análisis de datos de vehiculos usados")

# Cargar el conjunto de datos
try:
    df = pd.read_csv('vehicles_us.csv')
except FileNotFoundError:
    st.error("No se encontró el archivo vehicles_us.csv. Asegúrese de que esté en el mismo directorio que app.py")
    st.stop()

# Opción 1: Botones
st.header("Visualizaciones con botones")

hist_button = st.button("Construir histograma")
if hist_button:
    st.write("Histograma de odómetro")
    fig_hist = px.histogram(df, x="odometer")
    st.plotly_chart(fig_hist)

scatter_button = st.button("Construir gráfico de dispersión")
if scatter_button:
    st.write("Gráfico de dispersión de millas vs. precio")
    fig_scatter = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig_scatter)

# Opción 2: Casillas de verificación (desafío adicional)
st.header("Visualizaciones con casillas de verificación")

build_histogram = st.checkbox("Construir histograma")
if build_histogram:
    st.write("Histograma de odómetro")
    fig_hist = px.histogram(df, x="odometer")
    st.plotly_chart(fig_hist)

build_scatter = st.checkbox("Construir gráfico de dispersión")
if build_scatter:
    st.write("Gráfico de dispersión de millas vs. precio")
    fig_scatter = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig_scatter)