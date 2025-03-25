import pandas as pd
import pickle
import streamlit as st

# Load trained model and encoder
model = pickle.load(open("logistic_regression.pkl", "rb"))
encoder = pickle.load(open("encoder.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

st.title("Job Role Predictor")
st.write("Enter your details to predict the best job role for you.")

# User Inputs
gpa = st.number_input("Enter your GPA (0.0 - 4.0)", min_value=0.0, max_value=4.0, step=0.01)
major = st.selectbox("Select your Major", ["Computer Science", "Data Science", "Business", "Engineering", "Other"])
skills = st.text_area("Enter your Skills (comma-separated)")
courses = st.text_area("Enter Relevant Courses Taken (comma-separated)")

if st.button("Predict Job Role"):
    # Convert input into DataFrame format for prediction
    input_data = pd.DataFrame([[gpa, major, skills, courses]], columns=['GPA', 'Major', 'Skills', 'Courses'])
    
    # Apply the same transformations as during training
    encoded_input = encoder.transform(input_data)
    encoded_input = pd.DataFrame(encoded_input, columns=encoder.get_feature_names_out(['GPA', 'Major', 'Skills', 'Courses']))

    # Ensure all expected columns exist
    for col in columns:
        if col not in encoded_input.columns:
            encoded_input[col] = 0

    # Align with training column order
    encoded_input = encoded_input[columns]

    # Predict job role
    prediction = model.predict(encoded_input)
    st.success(f"Predicted Job Role: {prediction[0]}")
