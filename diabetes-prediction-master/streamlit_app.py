import streamlit as st
import pickle
import numpy as np

# ---------------- LOAD MODELS ---------------- #

models = {}
scalers = {}

# Load available models safely
try:
    models["Diabetes"] = pickle.load(open('models/diabetes_model.pkl', 'rb'))
    scalers["Diabetes"] = pickle.load(open('scalers/diabetes_scaler.pkl', 'rb'))
except:
    st.warning("Diabetes model not found")

try:
    models["Liver"] = pickle.load(open('models/liver_model.pkl', 'rb'))
    scalers["Liver"] = pickle.load(open('scalers/liver_scaler.pkl', 'rb'))
except:
    st.warning("Liver model not found")

# Placeholder for future
models["Heart"] = None
models["Kidney"] = None

# ---------------- UI ---------------- #

st.set_page_config(page_title="AI Health Predictor", layout="centered")

st.title("🧠 AI Multi Disease Prediction System")
st.markdown("### Select disease and enter details")

# Disease selection
disease = st.selectbox(
    "Select Disease",
    ["Diabetes", "Liver", "Heart (Coming Soon)", "Kidney (Coming Soon)"]
)

input_data = []

# ---------------- DIABETES ---------------- #

if disease == "Diabetes":
    st.subheader("🩸 Diabetes Prediction")

    col1, col2 = st.columns(2)

    with col1:
        pregs = st.number_input("Pregnancies", min_value=0)
        glucose = st.number_input("Glucose")
        bp = st.number_input("Blood Pressure")
        skin = st.number_input("Skin Thickness")

    with col2:
        insulin = st.number_input("Insulin")
        bmi = st.number_input("BMI")
        func = st.number_input("Diabetes Pedigree Function")
        age = st.number_input("Age")

    input_data = [pregs, glucose, bp, skin, insulin, bmi, func, age]

# ---------------- LIVER ---------------- #

elif disease == "Liver":
    st.subheader("🧪 Liver Disease Prediction")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age")
        gender = st.selectbox("Gender", ["Male", "Female"])
        total_bilirubin = st.number_input("Total Bilirubin")
        direct_bilirubin = st.number_input("Direct Bilirubin")
        alkphos = st.number_input("Alkaline Phosphotase")

    with col2:
        sgpt = st.number_input("SGPT")
        sgot = st.number_input("SGOT")
        proteins = st.number_input("Total Proteins")
        albumin = st.number_input("Albumin")
        ratio = st.number_input("A/G Ratio")

    # Encode gender
    gender = 1 if gender == "Male" else 0

    input_data = [
        age, gender, total_bilirubin, direct_bilirubin,
        alkphos, sgpt, sgot, proteins, albumin, ratio
    ]

# ---------------- HEART ---------------- #

elif disease == "Heart (Coming Soon)":
    st.info("🚧 Heart Prediction model not added yet")

# ---------------- KIDNEY ---------------- #

elif disease == "Kidney (Coming Soon)":
    st.info("🚧 Kidney Prediction model not added yet")

# ---------------- PREDICTION ---------------- #

if st.button("🔍 Predict"):

    if disease not in models or models[disease] is None:
        st.warning("Model not available for this disease yet")
    else:
        try:
            model = models[disease]
            scaler = scalers[disease]

            input_array = np.array(input_data).reshape(1, -1)
            input_scaled = scaler.transform(input_array)

            prediction = model.predict(input_scaled)

            if prediction[0] == 1:
                st.error(f"⚠ {disease} Detected")
            else:
                st.success(f"✅ No {disease} Detected")

        except Exception as e:
            st.error(f"Error: {e}")