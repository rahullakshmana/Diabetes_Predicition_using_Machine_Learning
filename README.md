# 🩺 Diabetes Predictor using Machine Learning

A Machine Learning-based diagnostic tool that predicts the likelihood of a person having diabetes based on medical attributes such as glucose level, BMI, insulin, and more. This project implements multiple ML models and compares their performance to choose the best predictor.

---

## 📌 Features

- Takes medical input features and predicts diabetes presence.
- Supports five ML models:
  - Logistic Regression
  - AdaBoost Classifier
  - Random Forest Classifier
  - Decision Tree Classifier
  - Gaussian Naive Bayes
- Accuracy visualization using bar graph.
- Allows live user input through CLI.
- Model persistence using `pickle` for deployment.

---

## 🧠 Algorithms Used

| Algorithm                | Description                                   |
|-------------------------|-----------------------------------------------|
| Logistic Regression      | Linear classifier for binary prediction       |
| AdaBoost Classifier      | Ensemble method boosting weak learners        |
| Random Forest Classifier | Ensemble of decision trees                    |
| Decision Tree Classifier | Tree-based classification model               |
| Gaussian Naive Bayes     | Probabilistic classifier using Bayes theorem  |

---

## 📝 Dataset

- **File**: `diabetes_new (1).csv`
- **Features Used**:
  - Glucose
  - BloodPressure
  - SkinThickness
  - Insulin
  - BMI
  - DiabetesPedigreeFunction
  - Age
- **Target**: `Outcome` (0: No Diabetes, 1: Has Diabetes)

---

## 🔧 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/diabetes-predictor.git
   cd diabetes-predictor
