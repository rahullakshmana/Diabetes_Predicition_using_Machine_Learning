# 🩺 Diabetes Prediction using Machine Learning  
**Vel Tech University | Minor Project 1 | 2024**

An AI-powered diagnostic tool built using machine learning models to predict the likelihood of diabetes based on health parameters. This system compares various classification algorithms and deploys the best model for practical use.

---

## 📚 Table of Contents

- [Overview](#overview)
- [Technologies Used](#technologies-used)
- [Dataset Information](#dataset-information)
- [Models Implemented](#models-implemented)
- [Project Workflow](#project-workflow)
- [Model Accuracy Comparison](#model-accuracy-comparison)
- [Prediction Output](#prediction-output)
- [Installation & Execution](#installation--execution)
- [Future Scope](#future-scope)

---

## 📌 Overview

This machine learning project helps to determine whether a person is diabetic based on medical attributes like glucose, blood pressure, BMI, insulin, and more. It evaluates multiple ML algorithms and identifies the best-performing one, offering predictions and accuracy visualizations.

---

## ⚙️ Technologies Used

- **Python 3.x**
- **NumPy**
- **Pandas**
- **Matplotlib**
- **Scikit-learn**
- **Pickle (Model Serialization)**

---

## 📊 Dataset Information

- **Source**: `diabetes_new (1).csv`
- **Features Used**:
  - Glucose
  - BloodPressure
  - SkinThickness
  - Insulin
  - BMI
  - DiabetesPedigreeFunction
  - Age
- **Target**:
  - Outcome (`0`: No Diabetes, `1`: Has Diabetes)

---

## 🧠 Models Implemented

| Algorithm                | Description                                   |
|-------------------------|-----------------------------------------------|
| Logistic Regression      | Linear classifier for binary outcomes         |
| AdaBoost Classifier      | Boosting ensemble method                      |
| Random Forest Classifier | Ensemble of decision trees                    |
| Decision Tree Classifier | Tree-based learning algorithm                 |
| Gaussian Naive Bayes     | Probabilistic classifier using Bayes' Theorem |

---

## 🔁 Project Workflow

1. Data Preprocessing & Splitting
2. Model Training (5 classifiers)
3. Model Evaluation on test data
4. Accuracy Comparison using Bar Chart
5. Predictive Model Deployment with User Input
6. Save final model (`.pkl`) using Pickle

---

## 📈 Model Accuracy Comparison

A bar graph visually compares the accuracy of all five algorithms. The best-performing algorithm (Random Forest or Decision Tree) is chosen for final deployment.

```python
a = ["LogisticRegression","AdaBoostClassifier","RandomForestClassifier","DecisionTreeClassifier","GaussianNB"]
b = [p1, p2, p3, p4, p5]
plt.figure(figsize=(15,6))
plt.bar(a, b)
plt.title("Accuracy Graph")
plt.xlabel("Algorithm")
plt.ylabel("Accuracy (%)")
plt.show()
```

---

## 🔍 Prediction Output

The system supports:

✅ Real-time CLI prediction using custom input  
✅ Probability-based result with prediction confidence  

**Example:**

```python
result = RF.predict([[84, 82, 31, 125, 38.2, 0.233, 23]])
result_perc = RF.predict_proba([[84, 82, 31, 125, 38.2, 0.233, 23]])

if result == 1:
    print("85% You are having Diabetes")
else:
    print("92% You are not having Diabetes")
```

---

## 🚀 Installation & Execution

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/diabetes-prediction-ml.git
cd diabetes-prediction-ml
```

2. **Install dependencies:**

```bash
pip install numpy pandas matplotlib scikit-learn
```

3. **Ensure the dataset file is in the project folder:**

```
diabetes_new (1).csv
```

4. **Run the program:**

```bash
python dia.py
```

5. **Enter user input when prompted:**

```text
Enter the Glucose level:
Enter the Blood pressure:
Enter the Skin Thickness:
Enter the Insulin:
Enter the BMI value:
Enter the Diabetes Pedigree Function:
Enter the Age:
```

6. **Sample Output:**

```text
87% You are not having Diabetes
```

7. **Final model is saved using Pickle:**

```python
file = open("dia.pkl", "wb")
pickle.dump(DC, file)
file.close()
```

---

## 🔮 Future Scope

- 🌐 Add web interface using **Streamlit** or **Flask**
- ☁️ Deploy on cloud for **API access**
- ⌚ Integrate with **wearable health devices**
- 🧾 Provide **personalized health recommendations**
- 📊 Track user health metrics **over time**

---

## 👨‍💻 Contributors

- **Rahul L** – [GitHub Profile](https://github.com/rahullakshmana/)

---

## 📄 License

This project is open-sourced under the [MIT License](LICENSE)

---
