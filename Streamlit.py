#pip install streamlit
import streamlit as st
import pandas as pd
import joblib


pipeline_path = "artifacts/preprocessor/preprocessor.pkl"
model_path = "artifacts/model/SVM.pkl"
encoder_path = "artifacts/preprocessor/label_encoder.pkl"


with open(pipeline_path, "rb") as file1:
    print(file1.read(100))
    

try:
    pipeline= joblib.load(pipeline_path)
    print("pipeline cargada")
    st.write("pipeline cargada")
except Exception as e:
    print(f"Error al cargar el pipeline {e}")
    



with open(model_path, "rb") as file2:
    print(file2.read(100))
try:
    model = joblib.load(model_path)
    print("modelo Cargado")
    st.write("modelo cargado")
except Exception as e:
    print("error al cargar modelo {e}")



with open(encoder_path, "rb") as file3:
    print(file3.read(100))
try:
    encoder = joblib.load(encoder_path)
    print("codificador cargado")
    st.write("encoder cargado")
except Exception as e:
    print("fallo al cargar el encoder {e}")