# Team_Krypton_ClarkHack
📌 Problem Statement
Students face challenges to find the right internships, and universities need a data-driven approach to career guidance. Our project aims to solve this by predicting the best internship role for a student based on academic, skill, and experience data.

📌 Steps Taken in The Project

1️⃣ Data Preprocessing

Loaded the dataset and handled missing values.

Performed One-Hot Encoding for categorical features and Standard Scaling for numerical features.

Ensured dataset consistency by keeping feature names and structures aligned.

2️⃣ Exploratory Data Analysis (EDA)

Identified correlations between GPA, major, experience, and internship success.

Checked for data imbalances and distribution across different internship roles.

3️⃣ Model Selection & Training

Implemented Logistic Regression, Random Forest, and initially XGBoost (later removed).

Trained models on the preprocessed dataset and tested performance using accuracy, precision, recall, and F1-score.

Logistic Regression performed the best with an accuracy of 87%, while Random Forest underperformed.

4️⃣ Saving the Model & Preprocessing Pipelines

Stored the trained model using Pickle (.pkl) for later use.

Saved the encoder, scaler, and label encoder to ensure consistency during inference.

5️⃣ Making Predictions on New Data

Loaded new student data (new_data.csv) and applied the same preprocessing pipeline.

Used the saved logistic regression model to predict the best internship role.

Decoded predictions back to internship role names using the label encoder.

📌 Final Outcomes
✅ Developed an AI-powered system to recommend internships based on student profiles.
✅ Achieved 87% accuracy in internship role predictions using Logistic Regression.
✅ Built a scalable and reusable pipeline to process new student data for real-time predictions.
