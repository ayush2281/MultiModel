# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:58:09 2025

@author: lenovo
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the saved models
def load_models():
    diabetes_model = pickle.load(open('diabetes_model.pkl', 'rb'))
    heart_model = pickle.load(open('heart_disease_model (1).sav', 'rb'))
    return diabetes_model, heart_model

diabetes_model, heart_model = load_models()

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Disease Prediction',
                            'Heart Disease Prediction'],
                           icons=['activity', 'heart-pulse-fill'],
                           default_index=0)

# Diabetes prediction page
def diabetes_prediction_page(diabetes_model):
    st.title("Diabetes Prediction Using ML")
    
    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
        
    with col2:
        Glucose = st.text_input('Number of Glucose')
        
    with col3:
        BloodPressure = st.text_input('Number of Blood Pressure')
        
    with col1:
        SkinThickness = st.text_input('Enter Skin Thickness')
        
    with col2:
        Insulin = st.text_input('Number of Insulin')
        
    with col3:
        BMI = st.text_input('Number of BMI')
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('Number of Diabetes Pedigree Function')
        
    with col2:
        Age = st.text_input('Number of Age')
        
    with col3:
        Outcome = st.text_input('Number of Outcome')
    
    # Code for the Prediction
    diab_diagnosis = ''
    
    # Create a button for the Prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness,
                                                   Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if diab_prediction[0] == 1:
            diab_diagnosis = 'The Person is Diabetic'
        else:
            diab_diagnosis = 'The Person is Not Diabetic'
            
    st.success(diab_diagnosis)

# Heart disease prediction page
def heart_disease_prediction_page(heart_model):
    st.title("Heart Disease Prediction Using ML")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age of the Person')
    
    with col2:
        sex = st.text_input('Enter Gender of the Person')
    
    with col3:
        cp = st.text_input('Chest Pain Types')
    
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    
    with col1:
        restecg = st.text_input('Resting Electrocardiographic Result')
    
    with col2:
        thalach = st.text_input('Thalach Value')
    
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    
    with col1:
        oldpeak = st.text_input('ST Depression Induced by Exercise')
    
    with col2:
        slope = st.text_input('Slope of the Peak Exercise ST Segment')
    
    with col3:
        ca = st.text_input('Major Vessels Colored by Fluoroscopy')
    
    with col1:
        thal = st.text_input('Thal: 0 = Normal; 1 = Fixed Defect; 2 = Reversible Defect')
    
    # Code for the Prediction
    heart_diagnosis = ''
    
    # Create a button for the Prediction
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,
                                                 thalach, exang, oldpeak, slope, ca, thal]])
        
        if heart_prediction[0] == 1:
            heart_diagnosis = 'The Person has Heart Disease'
        else:
            heart_diagnosis = 'The Person does not have Heart Disease'
    
    st.success(heart_diagnosis)

# Render the selected page
if selected == 'Diabetes Disease Prediction':
    diabetes_prediction_page(diabetes_model)
elif selected == 'Heart Disease Prediction':
    heart_disease_prediction_page(heart_model)
