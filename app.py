import streamlit as st
import joblib
import pandas as pd

st.set_page_config(
    page_title="Late Payment Predictor",
    page_icon="📊"
)

model = joblib.load("model.pkl")

st.title("Consumer Credit Risk Predictor")
st.caption("Estimate the chance of delayed payments based on financial behavior")
st.write("Enter customer financial information to predict the probability of delayed payment.")

# User inputs
age = st.number_input("Age", min_value=18, max_value=100, value=30)
monthly_income = st.number_input("Monthly Income", min_value=1.0, value=10000.0)
purchase_amount = st.number_input("Purchase Amount", min_value=0.0, value=2000.0)
installments = st.selectbox("Number of Installments", [3, 4])
current_monthly_debt = st.number_input("Current Monthly Debt", min_value=0.0, value=1000.0)

if st.button("Predict Risk"):
    if monthly_income <= 0:
        st.error("Monthly income must be greater than zero.")
    else:
        # Calculated features
        monthly_installment = purchase_amount / installments
        installment_ratio = monthly_installment / monthly_income
        dti_ratio = (current_monthly_debt + monthly_installment) / monthly_income
        stress_index = installment_ratio * dti_ratio
        income_safety = monthly_income / (monthly_installment + 1)

        # Input data
        input_data = pd.DataFrame([{
            "Age": age,
            "Monthly_Income": monthly_income,
            "Purchase_Amount": purchase_amount,
            "Installments": installments,
            "installment_ratio": installment_ratio,
            "DTI_Ratio": dti_ratio,
            "stress_index": stress_index,
            "income_safety": income_safety
        }])

        # Prediction
        probability = model.predict_proba(input_data)[0][1]
        prediction = 1 if probability >= 0.50 else 0

        # Risk level
        if probability < 0.30:
            risk_level = "Low Risk"
            risk_color = "green"
        elif probability < 0.70:
            risk_level = "Medium Risk"
            risk_color = "orange"
        else:
            risk_level = "High Risk"
            risk_color = "red"

        prediction_label = "Likely to Delay Payment" if prediction == 1 else "Likely to Pay On Time"

        # 🔥 
        st.subheader("📊 Risk Assessment Result")

        st.markdown(f"""
        <div style="padding:15px; border-radius:10px;">

        <b>Prediction:</b> {prediction_label}<br><br>

        <b>Probability of Delay:</b> {probability:.2%}<br><br>

        <b>Risk Level:</b> 
        <span style='color:{risk_color}; font-weight:bold'>{risk_level}</span>

        </div>
        """, unsafe_allow_html=True)
        
        st.info(
            "Higher debt-to-income ratio and higher installment burden increase the risk of delayed payments."
        )

        
        st.subheader("📈 Financial Indicators")

        st.write(f"**Estimated Monthly Installment:** {monthly_installment:.2f}")
        st.write(f"**Installment Ratio:** {installment_ratio:.3f}")
        st.write(f"**DTI Ratio (after purchase):** {dti_ratio:.3f}")
        st.write(f"**Stress Index:** {stress_index:.3f}")
        st.write(f"**Income Safety:** {income_safety:.3f}")