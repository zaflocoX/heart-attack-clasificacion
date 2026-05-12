import streamlit as st
import joblib
import pandas as pd
import time
from pathlib import Path

# --- CONFIGURACIÓN DE RUTA PARA CARPETAS HERMANAS ---
# 1. 'BASE_DIR' es la carpeta 'app' (donde está tu script)
BASE_DIR = Path(__file__).resolve().parent

# 2. Subimos UN nivel (llegamos a la raíz) y entramos a 'modelos'
MODEL_PATH = BASE_DIR.parent / "models" / "randomForest_model.joblib"
@st.cache_resource
def load_model(path):
    if path.exists():
        return joblib.load(path)
    else:
        # Esto te mostrará en pantalla qué está viendo Python realmente
        st.error(f"❌ No se encontró el modelo.")
        st.warning(f"Ruta intentada: {path}")
        return None

model = load_model(MODEL_PATH)

# --- INTERFAZ DE LA APLICACIÓN ---
if model:
    st.title("🏥 Predictor de Riesgo")

    with st.form("paciente_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            age = st.number_input("Edad", 1, 120, 30)
            gender = st.selectbox("Sexo", [0, 1], format_func=lambda x: "Femenino" if x == 0 else "Masculino")
            heart_rate = st.number_input("Frecuencia Cardíaca (PPM)", 40, 200, 75)
            
        with col2:
            systolic_bp = st.number_input("Presión Sistólica", 80, 200, 120)
            diastolic_bp = st.number_input("Presión Diastólica", 40, 130, 80)
            blood_sugar = st.number_input("Azúcar en Sangre", 50, 300, 100)

        submitted = st.form_submit_button("Realizar Diagnóstico")

    if submitted:
        # El DataFrame debe tener los mismos nombres de columnas que tu X_train
        input_df = pd.DataFrame([[
            age, gender, heart_rate, systolic_bp, diastolic_bp, blood_sugar
        ]], columns=['age', 'gender', 'heart_rate', 'systolic_bp', 'diastolic_bp', 'blood_sugar'])

        # Efecto de carga solicitado
        with st.spinner("⏳ Procesando biomarcadores..."):
            time.sleep(2) 
            prediction = model.predict(input_df)[0]
            probability = model.predict_proba(input_df)[0][1]

        # Resultado final
        st.divider()
        if prediction == 1:
            st.error(f"### RESULTADO: ALTO RIESGO")
            st.write(f"Probabilidad estimada por el modelo: **{probability:.2%}**")
        else:
            st.success(f"### RESULTADO: BAJO RIESGO")
            st.write(f"Probabilidad estimada por el modelo: **{probability:.2%}**")