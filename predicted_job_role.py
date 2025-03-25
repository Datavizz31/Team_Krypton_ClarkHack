import pickle

# Save Logistic Regression model
with open("logistic_regression.pkl", "wb") as file:
    pickle.dump(log_reg, file)


print("Models saved successfully!")

from google.colab import files

uploaded = files.upload()  # This will prompt you to upload your .pkl file

!pip install streamlit
import streamlit as st
loaded_model = pickle.load(open("logistic_regression.pkl", "rb"))
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
    prediction = model.predict(input_data)  # Ensure your model can handle categorical and text data

    st.success(f"Predicted Job Role: {prediction[0]}")

!echo "streamlit\npandas\nscikit-learn\nnumpy\LogisticRegression\RandomForestClassifier\XGBClassifier\accuracy_score, classification_report\StandardScaler\train_test_split" > requirements.txt

!jupyter nbconvert --to script /content/Predicted_Job_Role.ipynb

import os
print(os.listdir("/content"))
