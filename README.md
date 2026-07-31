# 🧠 Human Behaviour Analysis Using EEG Signal Analysis

> A Machine Learning and AI-powered web application that predicts human mental behaviour from EEG (Electroencephalography) signals using multiple classification algorithms and generates an AI-based interpretation report.

---

## 📖 Overview

Human Behaviour Analysis Using EEG Signal Analysis is a Flask-based web application developed to analyze EEG datasets and predict the user's mental state.

The system uses trained Machine Learning models to classify EEG signals into one of the following mental states:

- 🟢 Relaxed
- 🟡 Neutral
- 🔴 Concentrating

After prediction, the application automatically generates an AI interpretation report using **Ollama (Llama 3.2)**, providing behavioural observations, recommendations, and a professional summary.

---

## ✨ Features

- 📂 Upload EEG CSV Dataset
- 🤖 Multiple Machine Learning Models
- 📊 Prediction Confidence Analysis
- 📈 Interactive Charts
- 🧠 AI Generated Behaviour Interpretation
- 📥 Export Prediction Report
- 🌙 Modern Responsive UI
- ⚡ Fast Prediction using Flask Backend
- 💾 Automatic CSV Report Generation

---

## 🧠 Mental States Predicted

| Label | Behaviour |
|--------|-----------|
| Relaxed | Calm and relaxed mental activity |
| Neutral | Balanced cognitive state |
| Concentrating | High attention and focus |

---

## 🤖 Machine Learning Models

The application supports multiple trained models.

| Model | Accuracy |
|---------|-----------|
| Random Forest | **97.04%** |
| SVM | 94.71% |
| Logistic Regression | 93.66% |
| K-Nearest Neighbors | 89.64% |
| Decision Tree | 87.53% |

Random Forest is the default and best-performing model.

---

## 🧠 AI Report Generation

After prediction, the application sends the dominant mental state to **Ollama (Llama 3.2:3B)**.

The AI generates:

- Behaviour Interpretation
- Possible Observations
- Recommendations
- Disclaimer

The generated report is displayed in HTML format inside the application.

---

## 📊 Prediction Workflow

```
Upload EEG CSV
        │
        ▼
Read Dataset
        │
        ▼
Preprocessing
(Label Removal + Scaling)
        │
        ▼
Machine Learning Prediction
        │
        ▼
Dominant Behaviour Detection
        │
        ▼
Confidence Calculation
        │
        ▼
AI Interpretation (Ollama)
        │
        ▼
Display Results
        │
        ▼
Export Report
```

---

## 🏗 Project Structure

```
Human Behaviour Analysis/
│
├── app.py
├── scaler.pkl
├── random_forest_model.pkl
├── svm.pkl
├── logistic_regression.pkl
├── knn.pkl
├── decision_tree.pkl
│
├── templates/
│     └── index.html
│
├── static/
│     └── style.css
│
├── uploads/
│
├── Dataset/
│
└── README.md
```

---

## 💻 Technologies Used

### Backend

- Python
- Flask
- Pandas
- Joblib
- Scikit-Learn
- Ollama API

### Frontend

- HTML5
- CSS3
- JavaScript
- Chart.js
- Lucide Icons

### AI Model

- Llama 3.2 (3B)
- Ollama

---

## ⚙ Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Human-Behaviour-Analysis-Final-Version.git

cd Human-Behaviour-Analysis-Final-Version
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Install Ollama

Download:

https://ollama.com/

Run

```bash
ollama pull llama3.2:3b
```

---

### Run Application

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

## 📂 Dataset

The application accepts EEG datasets in **CSV format**.

Requirements:

- Numeric EEG Features
- Optional Label Column
- Same feature format used during model training

If a **Label** column exists, it is automatically removed before prediction.

---

## 📈 Output

The application displays

- Selected Model
- Model Accuracy
- Uploaded File Name
- Dominant Mental State
- Prediction Confidence
- Behaviour Distribution Chart
- AI Generated Interpretation Report

---

## 📥 Export

The generated prediction report can be exported as

- CSV

---

## 🔮 Future Enhancements

- PDF Export
- User Authentication
- Prediction History
- EEG Signal Visualization
- Deep Learning Models
- Cloud Deployment
- Real-Time EEG Device Support
- Database Integration

---

## 👨‍💻 Developed By

**Jatin Kumar**

Bachelor of Technology (Computer Science & Engineering)

GitHub:
https://github.com/jatin-cse

---

## 📜 License

This project is developed for educational and research purposes.

---

## ⭐ Acknowledgements

- Flask
- Scikit-Learn
- Pandas
- Ollama
- Chart.js
- Lucide Icons

---

## 📷 Screenshots

<img width="1907" height="1093" alt="image" src="https://github.com/user-attachments/assets/9a827a40-dcce-455b-b56c-77202baf7c7c" />
<img width="1906" height="1093" alt="image" src="https://github.com/user-attachments/assets/a83ae8e1-bba6-44ee-8458-0e9c2564d279" />
<img width="1908" height="1005" alt="image" src="https://github.com/user-attachments/assets/ac163124-6bb6-4186-a051-b217230c7b5a" />
<img width="1906" height="1076" alt="image" src="https://github.com/user-attachments/assets/8e91e11b-9c69-4601-83a6-e0566fa0bb89" />



Example

- Home Page
- Upload Dataset
- Prediction Result
- AI Report
- Export Report

---

## ❤️ Thank You

If you found this project useful, consider giving it a ⭐ on GitHub.
