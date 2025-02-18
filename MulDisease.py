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

def required_check(iterable):
    for var in iterable:
        if var=='':
            return False
    return True

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


    diab_var = [Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]

    # Code for the Prediction
    diab_diagnosis = ''

    # Create a button for the Prediction
    if st.button('Diabetes Test Result'):
        if (required_check(diab_var)==True):
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness,
                                                    Insulin, BMI, DiabetesPedigreeFunction, Age]])
            if diab_prediction[0] == 1:
                diab_diagnosis = 'The Person is Diabetic'
            else:
                diab_diagnosis = 'The Person is Not Diabetic'

            st.success(diab_diagnosis)
        else:
            st.warning("Please fill all the details")

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
