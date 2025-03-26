import streamlit as st
import pandas as pd

def calculate_bmi(weight, height_ft):
    height_m = height_ft * 0.3048  # Convert feet to meters
    bmi = weight / (height_m ** 2)
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"
    return bmi, category

# Streamlit App
st.set_page_config(page_title="BMI Calculator", page_icon="⚖️")
st.title("BMI Calculator")

st.write("Enter your weight and height to calculate your BMI.")

# User input with slider
weight = st.slider("Weight (kg)", min_value=1.0, max_value=200.0, value=70.0, step=0.1)
height_ft = st.slider("Height (feet)", min_value=1.5, max_value=8.0, value=5.7, step=0.1)

if st.button("Calculate BMI"):
    if weight > 0 and height_ft > 0:
        bmi, category = calculate_bmi(weight, height_ft)
        st.success(f"Your BMI is {bmi:.2f} ({category})")
    else:
        st.error("Please enter valid weight and height.")

# Creating a DataFrame to show BMI ranges
bmi_data = pd.DataFrame({
    "Category": ["Underweight", "Normal weight", "Overweight", "Obese"],
    "BMI Range": ["< 18.5", "18.5 - 24.9", "25 - 29.9", ">= 30"]
})
st.write("### BMI Categories")
st.dataframe(bmi_data, hide_index=True)
