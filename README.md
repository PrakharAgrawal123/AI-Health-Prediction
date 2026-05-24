# 🧠 AI Multi Disease Prediction System

A professional Machine Learning based healthcare web application that predicts the risk of multiple diseases using trained ML models and an interactive Streamlit interface.

## 🚀 Live Demo
🔗 **Live App:** [Add Your Streamlit Link Here]  
🔗 **GitHub Repository:** [Add Your GitHub Repo Link Here]

---

## 📌 Project Overview

The **AI Multi Disease Prediction System** is an intelligent healthcare prediction platform that allows users to check the probability of different diseases based on medical input parameters.

This project combines:

- **Machine Learning Models**
- **Data Analysis & Visualization**
- **Feature Engineering**
- **Model Deployment**
- **Interactive Streamlit UI**

Currently implemented disease prediction modules:

✅ Diabetes Prediction  
✅ Liver Disease Prediction  
✅ Heart Disease Prediction  
🚧 Kidney Disease Prediction (Coming Soon)

---

## ✨ Features

- 🔍 Predict multiple diseases in one platform
- 🧠 ML-based disease risk analysis
- 📊 Trained on real healthcare datasets
- 🎨 Professional and interactive UI using Streamlit
- ⚡ Fast predictions in real time
- 📈 Data preprocessing and feature scaling
- 💾 Pickle-based model deployment
- 🌐 Cloud deployed and publicly accessible

---

## 🏥 Supported Diseases

| Disease | Status |
|---------|--------|
| Diabetes | ✅ Completed |
| Liver Disease | ✅ Completed |
| Heart Disease | ✅ Completed |
| Kidney Disease | 🚧 In Progress |

---

## 🛠 Tech Stack

### Programming Language
- Python

### Libraries Used
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Pickle
- Streamlit

### Machine Learning Algorithms
- Logistic Regression
- K-Nearest Neighbors (KNN)
- Naive Bayes
- Support Vector Machine (SVM)
- Decision Tree
- Random Forest

---

## 📂 Project Structure

```plaintext
AI-Health-Prediction/
│
├── diabetes-prediction-master/
│   ├── models/
│   │   ├── diabities_model.pkl
│   │   ├── liver_model.pkl
│   │   ├── heart_model.pkl
│   │
│   ├── scalers/
│   │   ├── diabities_scaler.pkl
│   │   ├── liver_scaler.pkl
│   │   ├── heart_scaler.pkl
│   │
│   ├── datasets/
│   │   ├── diabetes.csv
│   │   ├── liver.csv
│   │   ├── heart.csv
│   │
│   ├── notebooks/
│   │   ├── diabetes_training.ipynb
│   │   ├── liver_training.ipynb
│   │   ├── heart_training.ipynb
│   │
│   ├── streamlit_app.py
│   ├── requirements.txt
│   └── README.md
```

---

## ⚙️ Machine Learning Workflow

### 1️⃣ Data Collection
Healthcare datasets collected for multiple diseases.

### 2️⃣ Data Cleaning
- Null value handling
- Duplicate removal
- Missing value treatment

### 3️⃣ Data Visualization
- Count plots
- Histograms
- Box plots
- Heatmaps
- Correlation analysis

### 4️⃣ Feature Engineering
- Label Encoding
- Feature Selection
- Standardization using `StandardScaler`

### 5️⃣ Model Training
Multiple ML models trained and compared.

### 6️⃣ Model Evaluation
Accuracy scores used to select the best-performing model.

### 7️⃣ Deployment
Best models saved using Pickle and deployed with Streamlit.

---

## 📊 Model Performance

Different ML algorithms were tested and compared:

- Logistic Regression
- KNN
- Naive Bayes
- SVM
- Decision Tree
- Random Forest

Best-performing model selected individually for each disease.

---

## 💻 Installation & Setup

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
```

### Move into Project Folder

```bash
cd diabetes-prediction-master
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run streamlit_app.py
```

---

## 🧪 Example Predictions

Users can:

- Select disease type
- Enter medical parameters
- Get instant prediction result

Example:

- Diabetes → Diabetic / Non-Diabetic
- Liver → Disease / No Disease
- Heart → Disease / No Disease

---

## 📈 Future Improvements

- Kidney Disease Prediction
- Better UI/UX
- Doctor Recommendation Module
- PDF Health Report Generation
- Authentication System
- Health History Tracking

---

## 🎯 Use Cases

- Healthcare awareness
- Educational ML project
- Disease risk prediction
- Internship/portfolio showcase
- Machine Learning deployment demo

---

## 👨‍💻 Author

**Prakhar Agrawal**

- 🎓 BCA Student | Aspiring Data Scientist
- 💻 Passionate about Machine Learning & Web Development

---

## ⭐ If you like this project

Please consider giving it a **star ⭐ on GitHub**

---

## 📜 License

This project is for educational and learning purposes.
