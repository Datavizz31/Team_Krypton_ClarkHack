import streamlit as st
import pickle
import pandas as pd

# Load the trained model
with open("logistic_regression.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Job Role Predictor")
st.write("Enter your details to predict the best job role for you.")

# User Inputs
gpa = st.number_input("Enter your GPA (0.0 - 4.0)", min_value=0.0, max_value=4.0, step=0.01)
major = st.selectbox("Select your Major", ["Computer Science", "Data Science", "Business", "Engineering", "Other"])
skills = st.text_area("Enter your Skills (comma-separated)")
courses = st.text_area("Enter Relevant Courses Taken (comma-separated)")
certifications = st.text_area("Enter Certifications (comma-separated)")
preferred_industry = st.selectbox("Preferred Industry", ['Technology', 'Finance', 'Healthcare', 'Education', 'Other'])
extracurriculars = st.text_area("Enter Extracurricular Activities (comma-separated)")

if st.button("Predict Job Role"):
    # Convert input into DataFrame format for prediction
    input_data = pd.DataFrame([[gpa, major, skills, courses]], columns=['GPA', 'Major', 'Skills', 'Courses'])
    prediction = model.predict(input_data)  # Ensure your model can handle categorical and text data

    st.success(f"Predicted Job Role: {prediction[0]}")

