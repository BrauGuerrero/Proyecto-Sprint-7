import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

# título de la aplicación
st.header('Análisis de venta de coches usados')

hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches'
    )

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# crear una casilla de verificación
scatter_button = st.checkbox('Construir un diagrama de dispersión')

if scatter_button:  # si la casilla de verificación está seleccionada
    st.write(
        'Construir un diagrama de dispersión para comparar el preciode un coche con su odómetro')

    # crear un histograma
    fig = px.scatter(car_data, x="odometer", y="price",)

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
