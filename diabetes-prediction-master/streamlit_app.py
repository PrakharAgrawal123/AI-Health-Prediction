import streamlit as st
import pickle
import numpy as np

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(page_title="AI Health Predictor", layout="centered")

# ---------------- LOAD MODELS ---------------- #

models = {}
scalers = {}

# Diabetes
try:
    models["Diabetes"] = pickle.load(open("diabetes-prediction-master/models/diabities_model.pkl", "rb"))
    scalers["Diabetes"] = pickle.load(open("diabetes-prediction-master/scalers/diabities_scaler.pkl", "rb"))
except Exception as e:
    st.warning(f"Diabetes model error: {e}")

# Liver
try:
    models["Liver"] = pickle.load(open("diabetes-prediction-master/models/liver_model.pkl", "rb"))
    scalers["Liver"] = pickle.load(open("diabetes-prediction-master/scalers/liver_scaler.pkl", "rb"))
except Exception as e:
    st.warning(f"Liver model error: {e}")

# Heart
try:
    models["Heart"] = pickle.load(open("diabetes-prediction-master/models/heart_model.pkl", "rb"))
    scalers["Heart"] = pickle.load(open("diabetes-prediction-master/scalers/heart_scaler.pkl", "rb"))
except Exception as e:
    st.warning(f"Heart model error: {e}")

# Kidney (not added yet)
models["Kidney"] = None

# ---------------- UI ---------------- #

st.title("🧠 AI Multi Disease Prediction System")
st.markdown("### Select disease and enter details")

disease = st.selectbox(
    "Select Disease",
    ["Diabetes", "Liver", "Heart", "Kidney"]
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

    gender = 1 if gender == "Male" else 0

    input_data = [
        age, gender, total_bilirubin, direct_bilirubin,
        alkphos, sgpt, sgot, proteins, albumin, ratio
    ]

# ---------------- HEART ---------------- #

elif disease == "Heart":

    st.subheader("❤️ Heart Disease Prediction")

    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=1)

        sex = st.selectbox("Sex", ["Male", "Female"])

        cp = st.selectbox(
            "Chest Pain Type",
            ["asymptomatic", "atypical angina", "non-anginal", "typical angina"]
        )

        trestbps = st.number_input("Resting Blood Pressure")

        chol = st.number_input("Cholesterol")

        fbs = st.selectbox(
            "Fasting Blood Sugar > 120 mg/dl",
            ["False", "True"]
        )

        ca = st.number_input("Major Vessels (0-3)", min_value=0, max_value=3)

    with col2:

        restecg = st.selectbox(
            "Rest ECG",
            ["lv hypertrophy", "normal", "st-t abnormality"]
        )

        thalach = st.number_input("Maximum Heart Rate")

        exang = st.selectbox(
            "Exercise Induced Angina",
            ["False", "True"]
        )

        oldpeak = st.number_input("Oldpeak")

        slope = st.selectbox(
            "Slope",
            ["downsloping", "flat", "upsloping"]
        )

        thal = st.selectbox(
            "Thal",
            ["fixed defect", "normal", "reversable defect"]
        )

    # Encoding
    sex = 1 if sex == "Male" else 0

    cp_mapping = {
        "asymptomatic": 0,
        "atypical angina": 1,
        "non-anginal": 2,
        "typical angina": 3
    }
    cp = cp_mapping[cp]

    fbs = 1 if fbs == "True" else 0

    restecg_mapping = {
        "lv hypertrophy": 0,
        "normal": 1,
        "st-t abnormality": 2
    }
    restecg = restecg_mapping[restecg]

    exang = 1 if exang == "True" else 0

    slope_mapping = {
        "downsloping": 0,
        "flat": 1,
        "upsloping": 2
    }
    slope = slope_mapping[slope]

    thal_mapping = {
        "fixed defect": 0,
        "normal": 1,
        "reversable defect": 2
    }
    thal = thal_mapping[thal]

    input_data = [
        age,
        sex,
        cp,
        trestbps,
        chol,
        fbs,
        restecg,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,
        thal
    ]

# ---------------- KIDNEY ---------------- #

elif disease == "Kidney":
    st.info("🚧 Kidney Prediction model not added yet")

# ---------------- PREDICTION ---------------- #

if st.button("🔍 Predict"):

    if disease not in models or models[disease] is None:
        st.warning(f"{disease} model not available yet")

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
            st.error(f"Prediction Error: {e}")