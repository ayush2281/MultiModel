# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 13:58:09 2025

@author: lenovo
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt

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
                            'Heart Disease Prediction',
                            'User Feedback'],  # Added User Feedback option
                           icons=['activity', 'heart-pulse-fill', 'chat-right-dots'],
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
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0, step=1)  # Changed to number_input
        
    with col2:
        Glucose = st.number_input('Number of Glucose', min_value=0, step=1)
        
    with col3:
        BloodPressure = st.number_input('Number of Blood Pressure', min_value=0, step=1)
        
    with col1:
        SkinThickness = st.number_input('Enter Skin Thickness', min_value=0, step=1)
        
    with col2:
        Insulin = st.number_input('Number of Insulin', min_value=0, step=1)
        
    with col3:
        BMI = st.number_input('Number of BMI', min_value=0.0, step=0.1)  # Changed to float input
        
    with col1:
        DiabetesPedigreeFunction = st.number_input('Number of Diabetes Pedigree Function', min_value=0.0, step=0.01)
        
    with col2:
        Age = st.number_input('Number of Age', min_value=0, step=1)
        
    diab_var = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
    
    # Code for the Prediction
    diab_diagnosis = ''
    
    # Create a button for the Prediction
    if st.button('Diabetes Test Result'):
        if required_check(diab_var):
            diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness,
                                                      Insulin, BMI, DiabetesPedigreeFunction, Age]])
            if diab_prediction[0] == 1:
                diab_diagnosis = 'The Person is Diabetic'
            else:
                diab_diagnosis = 'The Person is Not Diabetic'
                
            st.success(diab_diagnosis)
            
            # Visualize the results
            labels = ['Diabetic', 'Not Diabetic']
            sizes = [diab_prediction[0], 1 - diab_prediction[0]]
            fig1, ax1 = plt.subplots()
            ax1.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
            ax1.axis('equal')
            st.pyplot(fig1)  # Added pie chart visualization
        else:
            st.warning("Please fill all the details")

# Heart disease prediction page
# Heart disease prediction page
def heart_disease_prediction_page(heart_model):
    st.title("Heart Disease Prediction Using ML")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.slider('Age of the Person', min_value=0, max_value=120, step=1)
    
    with col2:
        sex = st.selectbox('Enter Gender of the Person', options=['Male', 'Female'])
    
    with col3:
        cp = st.selectbox('Chest Pain Types', options=['Type 1', 'Type 2', 'Type 3', 'Type 4'])
    
    with col1:
        trestbps = st.slider('Resting Blood Pressure', min_value=0, max_value=200, step=1)
    
    with col2:
        chol = st.slider('Serum Cholestoral in mg/dl', min_value=0, max_value=600, step=1)
    
    with col3:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', options=['True', 'False'])
    
    with col1:
        restecg = st.selectbox('Resting Electrocardiographic Result', options=['Normal', 'Abnormal'])
    
    with col2:
        thalach = st.slider('Thalach Value', min_value=0, max_value=250, step=1)
    
    with col3:
        exang = st.selectbox('Exercise Induced Angina', options=['Yes', 'No'])
    
    with col1:
        oldpeak = st.slider('ST Depression Induced by Exercise', min_value=0.0, max_value=10.0, step=0.1)
    
    with col2:
        slope = st.selectbox('Slope of the Peak Exercise ST Segment', options=['Up', 'Flat', 'Down'])
    
    with col3:
        ca = st.slider('Major Vessels Colored by Fluoroscopy', min_value=0, max_value=4, step=1)
    
    with col1:
        thal = st.selectbox('Thal', options=['Normal', 'Fixed Defect', 'Reversible Defect'])
    
    heart_var = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
    
    # Code for the Prediction
    heart_diagnosis = ''
    
    # Create a button for the Prediction
    if st.button('Heart Disease Test Result'):
        if required_check([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]):
            heart_prediction = heart_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg,
                                                    thalach, exang, oldpeak, slope, ca, thal]])
            
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The Person has Heart Disease'
            else:
                heart_diagnosis = 'The Person does not have Heart Disease'
        
            st.success(heart_diagnosis)
            
            # Enhanced Visualization
            labels = ['Heart Disease', 'No Heart Disease']
            sizes = [heart_prediction[0], 1 - heart_prediction[0]]
            fig = px.pie(values=sizes, names=labels, title='Heart Disease Prediction Results')
            st.plotly_chart(fig)  # Added Plotly chart visualization
        else:
            st.warning("Please fill all the details")
    else:
        st.info("Please fill in the details and click the button to get the result.")  # Added info message


# User feedback page
def user_feedback_page():
    st.title("User Feedback")
    feedback = st.text_area("Please provide your feedback here")
    if st.button("Submit Feedback"):
        st.success("Thank you for your feedback!")

# Render the selected page
if selected == 'Diabetes Disease Prediction':
    diabetes_prediction_page(diabetes_model)
elif selected == 'Heart Disease Prediction':
    heart_disease_prediction_page(heart_model)
elif selected == 'User Feedback':
    user_feedback_page()  # Added user feedback page
