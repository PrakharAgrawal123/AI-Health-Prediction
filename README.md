# 🧠 AI Multi Disease Prediction System

A Machine Learning powered healthcare web application that predicts the probability of multiple diseases using trained ML models and an interactive Streamlit interface.

## 🚀 Live Demo
🔗 **Live App:** [https://ai-health-predictor.streamlit.app]  
🔗 **GitHub Repository:** [https://github.com/PrakharAgrawal123/AI-Health-Prediction]

---

## 📌 Project Overview

The **AI Multi Disease Prediction System** is an intelligent healthcare prediction platform that helps users predict disease risk based on medical input parameters.

This project integrates:

- Machine Learning
- Data Analysis
- Feature Engineering
- Model Deployment
- Interactive Streamlit Web Interface

### Currently Supported Diseases

✅ Diabetes Prediction  
✅ Liver Disease Prediction  
✅ Heart Disease Prediction  
🚧 Kidney Disease Prediction (Dataset Added, Model Pending)

---

## ✨ Features

- 🔍 Multi-disease prediction in one platform
- 🧠 Machine Learning based prediction
- 📊 Trained on real healthcare datasets
- ⚡ Real-time prediction
- 🎨 Interactive Streamlit UI
- 📈 Data preprocessing and feature scaling
- 💾 Model saving using Pickle
- 🌐 Public cloud deployment

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

### Language
- Python

### Libraries Used
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Pickle

### Machine Learning Algorithms Used
- Logistic Regression
- K-Nearest Neighbors (KNN)
- Naive Bayes
- Support Vector Machine (SVM)
- Decision Tree
- Random Forest

---

## 📂 Project Structure

```plaintext
AI-HEALTH-PREDICTION/
│
├── diabetes-prediction-master/
│   │
│   ├── data/
│   │   ├── clean_liver.csv
│   │   ├── diabetes.csv
│   │   ├── heart_disease_uci.csv
│   │   ├── kidney_disease.csv
│   │
│   ├── models/
│   │   ├── diabities_model.pkl
│   │   ├── heart_model.pkl
│   │   ├── liver_model.pkl
│   │
│   ├── scalers/
│   │   ├── diabities_scaler.pkl
│   │   ├── heart_scaler.pkl
│   │   ├── liver_scaler.pkl
│   │
│   ├── training/
│   │   ├── diabetes_prediction.ipynb
│   │   ├── heart_disease_prediction.ipynb
│   │   ├── liver_prediction.ipynb
│   │
│   ├── requirements.txt
│   └── streamlit_app.py
```

---

## ⚙️ Machine Learning Workflow

### 1️⃣ Data Collection
Collected healthcare datasets for multiple diseases.

### 2️⃣ Data Cleaning
- Null value handling
- Missing value treatment
- Duplicate removal

### 3️⃣ Data Visualization
- Count plots
- Histograms
- Correlation heatmaps
- Distribution analysis

### 4️⃣ Feature Engineering
- Label Encoding
- Feature Scaling
- Data Standardization using `StandardScaler`

### 5️⃣ Model Training
Multiple ML algorithms trained and compared.

### 6️⃣ Model Evaluation
Best model selected based on performance metrics.

### 7️⃣ Deployment
Models saved using Pickle and deployed using Streamlit.

---

## 📊 Model Performance

The following ML models were tested:

- Logistic Regression
- KNN
- Naive Bayes
- SVM
- Decision Tree
- Random Forest

Best-performing models were selected for deployment.

---

## 💻 Installation & Setup

### Clone Repository

```bash
git clone https://github.com/PrakharAgrawal123/AI-Health-Prediction.git
```

### Move into Project Folder

```bash
cd diabetes-prediction-master
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run App

```bash
streamlit run streamlit_app.py
```

---

## 🧪 Example Predictions

Users can:

- Select disease type
- Enter medical parameters
- Get instant prediction results

Example outputs:

- Diabetes → Diabetic / Non-Diabetic
- Liver → Disease / No Disease
- Heart → Disease / No Disease

---

## 📈 Future Improvements

- Kidney Disease Prediction
- Better UI/UX
- Doctor Recommendation System
- PDF Health Report Generation
- User Authentication

---

## 🎯 Use Cases

- Disease risk prediction
- Healthcare awareness
- Machine Learning project showcase
- Internship portfolio project
- ML deployment demonstration

---

## 👨‍💻 Author

**Prakhar Agrawal**

- 🎓 BCA Student | Aspiring Data Scientist
- 💻 Passionate about Machine Learning & Web Development

---

## ⭐ Support

If you like this project, consider giving it a **star ⭐ on GitHub**

---

## 📜 License

This project is for educational and learning purposes.
