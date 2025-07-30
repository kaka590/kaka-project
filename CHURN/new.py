import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn import datasets
import streamlit as st
import joblib
import numpy as np
import pickle
import numpy as np# 
from sklearn.linear_model import LogisticRegression
log_reg = LogisticRegression()
with open("logistic_model.pkl", "wb") as file:
    pickle.dump(log_reg, file)
model = pickle.load(open("logistic_model.pkl", "rb"))
model
import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load(r'c:\Users\USER\OneDrive\Dokumente\logistic_model_1.pkl', 'rb')

# UI
st.title("Expresso Churn Prediction")

# Replace these inputs with your actual feature names
feature1 = st.number_input("feature 1")
feature2 = st.number_input("feature 2")
feature3 = st.number_input("feature 3")
feature4 = st.number_input("feature 4")
feature5 = st.number_input("feature 5")
feature6 = st.number_input("feature 6")
feature7 = st.number_input("feature 7")
# ...
# Example input list
features = [feature1, feature2, feature3, feature4, feature5, feature6, feature7]  # Add all feature inputs

if st.button("Predict"):
    prediction = model.predict([features])
    st.success(f"Prediction: {'Churn' if prediction[0]==1 else 'No Churn'}")















