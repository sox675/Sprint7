import streamlit as st
import pandas as pd
import plotly.express as px

# Leer los datos
car_data = pd.read_csv('../datasets/vehicles_us.csv')

# Encabezado
st.header('Análisis interactivo de vehículos usados 🚗')

# Botón para crear histograma
hist_button = st.button('Construir histograma')

if hist_button:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x='odometer', title='Distribución del kilometraje')
    st.plotly_chart(fig, use_container_width=True)

# Botón para crear gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

if scatter_button:
    st.write('Creación de un gráfico de dispersión: precio vs kilometraje')
    fig2 = px.scatter(car_data, x='odometer', y='price', title='Relación entre kilometraje y precio')
    st.plotly_chart(fig2, use_container_width=True)
