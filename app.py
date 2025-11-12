import streamlit as st
import pandas as pd
import pickle

# -------------------------------
# ✅ Load the trained model
# -------------------------------
with open("gbr_model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Possum Age Predictor", layout="centered")

st.title("🦝 Possum Age Prediction App")

st.write("""
This app predicts **Possum Age** using biological measurements.
Enter the values below and click **Predict Age**.
""")

# -----------------------------------------
# ✅ Input fields for the 6 required features
# -----------------------------------------
hdlngth = st.number_input("Head Length", value=90.0)
skullw = st.number_input("Skull Width", value=60.0)
totlngth = st.number_input("Total Body Length", value=90.0)
eye = st.number_input("Eye Size", value=15.0)
chest = st.number_input("Chest Size", value=28.0)
belly = st.number_input("Belly Size", value=33.0)

# -----------------------------------------
# ✅ Prepare input for prediction
# -----------------------------------------
input_data = pd.DataFrame([[
    hdlngth, skullw, totlngth, eye, chest, belly
]], columns=["hdlngth", "skullw", "totlngth", "eye", "chest", "belly"])

# -----------------------------------------
# ✅ Predict Button
# -----------------------------------------
if st.button("Predict Age"):
    prediction = model.predict(input_data)[0]
    st.success(f"✅ Predicted Possum Age: **{prediction:.2f} years**")
