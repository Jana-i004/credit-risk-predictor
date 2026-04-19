# 💳 Consumer Credit Risk Predictor (Saudi BNPL Market)

A data-driven project that analyzes customer financial behavior and predicts the likelihood of delayed payments using machine learning.

---

## 🚀 Project Overview

This project combines **data analysis** and **machine learning** to understand customer behavior and predict credit risk in Buy Now, Pay Later (BNPL) services.

It follows a complete workflow:

1. 📊 Customer behavior analysis  
2. 🧠 Feature engineering  
3. 🤖 Machine learning modeling  
4. 🖥️ Interactive prediction application  

---

## 🇸🇦 Market Relevance

This project is based on **Saudi Arabia BNPL consumer behavior data** (sourced from Kaggle).

It reflects real financial patterns in the Saudi market and is relevant to:

- Fintech companies in Saudi Arabia  
- BNPL platforms  
- Credit risk assessment systems  
- Financial decision-making tools  

---

## 🎯 Objective

To predict whether a customer is likely to **delay a payment** based on:

- Monthly income  
- Purchase amount  
- Installment structure  
- Existing monthly debt  

---

## 📊 Customer Behavior Analysis

An exploratory data analysis (EDA) was conducted to understand how customers behave financially.

The analysis focused on:
- Spending patterns  
- Payment behavior  
- Customer segmentation  
- Debt distribution  

### 📌 Customer Behavior Dashboard

<img width="1789" height="985" alt="Customer_Behavior_Dashboard" src="https://github.com/user-attachments/assets/599be18b-1acd-4fa9-88aa-11837d454826" />


---

## 🧠 Machine Learning Model

- Algorithm: **Random Forest Classifier**
- Accuracy: **~92%**
- Output: Probability of delayed payment

---

## ⚙️ Feature Engineering

Key engineered features:

- **Installment Ratio**  
  → Monthly installment relative to income  

- **DTI (Debt-to-Income Ratio)**  
  → Total monthly obligations relative to income  

- **Stress Index**  
  → Combined financial pressure  

- **Income Safety**  
  → Measures how comfortably income covers payments  

These features were derived from the insights gained during data analysis.

---

## 📈 Risk Analysis Insights

The analysis revealed strong relationships:

- Higher DTI → higher risk of delayed payments  
- Higher installment pressure → increased financial stress  

### 📌 Feature Importance

<img width="626" height="388" alt="feature_importance" src="https://github.com/user-attachments/assets/8679fa10-0d13-4b07-89b9-8fc7fe112aa5" />

---

## 🖥️ Application

🔗 **Try the app here:**  
https://credit-risk-predictor-dpl4mznx2reqemju8fyj3v.streamlit.app/

An interactive Streamlit app allows users to:

- Input financial data  
- Simulate purchase scenarios  
- Get instant risk predictions  

### 📌 App Preview


<img width="2028" height="2659" alt="low_risk" src="https://github.com/user-attachments/assets/af59853c-cc26-48dc-84fc-b544a92308d8" />


<img width="2073" height="2667" alt="medium_risk" src="https://github.com/user-attachments/assets/4c781c50-409c-4ddd-906b-9bee05d78398" />



<img width="2110" height="2740" alt="high_risk" src="https://github.com/user-attachments/assets/6292337c-044a-4a22-8420-f79245c46267" />


---

## ⚠️ Important Design Decision

To ensure reliable predictions:

> Input values (such as number of installments) were restricted to match the training data.

This avoids unrealistic scenarios and improves model consistency.

---

## 🛠️ Tech Stack

- Python  
- Pandas  
- Scikit-learn  
- Streamlit  
- Matplotlib & Seaborn  

