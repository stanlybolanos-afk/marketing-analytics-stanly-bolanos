# Archivo base para el despliegue del Agente en Streamlit
# Librerias
import streamlit as st
from sklearn.linear_model import LinearRegression
import numpy as np

# En streamlit vamos a agregar un titulo para la pagina web
st.title("Configuracion inicial")
# Agregaremos un textbox en nuestra pagina web
st.write("Primera prueba de uso de streamlit y ambiente de MA2026")

# El slider de streamlit me permite ingresar por un slider el parametro inversion
gasto=st.slider("Seleccine nivel de gasto en publicicdad", 10,200,50)

# variables de nuestro modelo
variable_x = np.array([[10], [20], [30], [40],[50]])
variable_y = np.array([15,25,35,45,55])
modelo_lr = LinearRegression()

# entrenamiento de nuestro modelo LR
modelo_lr.fit(variable_x,variable_y)

# En streamlit, tenemos un boton que dice Predecir y al dar click activara las lineas de codigo del if
if st.button("Predecir"):
    resultado = modelo_lr.predict([[gasto]])

    # streamlit muestra un mensaje de exito en verde bonito usando success
    st.success(f"Las ventas proyectadas para una inversion de ${gasto} son:${resultado[0]}")