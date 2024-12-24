import streamlit as st
#import joblib

# Load the pre-trained model
model = joblib.load('/home/kimath/Desktop/PROJECTS/Projects/INSURENCE/insurence/insur/static/random_forest_regressor')

# Streamlit app
st.title("Insurance Premium Prediction")

st.write("Enter the following details to predict insurance premium:")

# Input fields
age = st.number_input("Age", min_value=1, max_value=100, step=1)
sex = st.selectbox("Sex", options=["Male", "Female"])
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, step=0.1)
children = st.number_input("Number of Children", min_value=0, max_value=10, step=1)
smoker = st.selectbox("Smoker", options=["Yes", "No"])
region = st.selectbox("Region", options=["Northeast", "Northwest", "Southeast", "Southwest"])

# Convert categorical inputs to numeric
sex = 1 if sex == "Male" else 0
smoker = 1 if smoker == "Yes" else 0
region_mapping = {"Northeast": 0, "Northwest": 1, "Southeast": 2, "Southwest": 3}
region = region_mapping[region]

# Predict button
if st.button("Predict"):
    prediction = model.predict([[age, sex, bmi, children, smoker, region]])
    st.success(f"Predicted Insurance Premium: ${round(prediction[0], 2)}")
