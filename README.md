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

![Customer Behavior](images/customer_overview.png)

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

![Feature Importance]([images/feature_importance.png](https://github.com/Jana-i004/credit-risk-predictor/blob/31d5eecc565ae0e95543d07ed9ae4a5bd412e6c0/feature_importance.png))

---

## 🖥️ Application

An interactive Streamlit app allows users to:

- Input financial data  
- Simulate purchase scenarios  
- Get instant risk predictions  

### 📌 App Preview

![Input](images/app_input.png)

![Low Risk](images/low_risk.png)

![High Risk](images/high_risk.png)

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

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
streamlit run app.py
