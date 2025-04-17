import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
#loading the saved models
heart_disease_model = pickle.load(open("heart_disease.sav",'rb'))
diabetes_model = pickle.load(open("diabetes.sav", 'rb'))
scaler = pickle.load(open("scaler.pkl", 'rb'))
parkinsons_model = pickle.load(open("parkinson.sav", 'rb'))

#sidebar to navigate
with st.sidebar:
    selected = option_menu("Smart Health Predictor",
                           ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinson Prediction'],
                           icons=['heart', 'activity', 'person'],
                           default_index=0
                           )
    
if (selected == 'Heart Disease Prediction'):
    st.title("Heart Disease Prediction using ML") #page title

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    #Code for prediction
    heart_diagnosis = ''

    #Creating a button for prediction
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having a heart disease'
        else:
            heart_diagnosis = "The person doesn't have a heart disease"
        
    st.success(heart_diagnosis)


elif (selected == 'Diabetes Prediction'):
    st.title("Diabetes Prediction using ML") #page title

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        # Age (Integer input)
        age = st.number_input("Age", min_value=0, step=1, format="%d")

    with col2:
        # BMI (Float input)
        bmi = st.number_input("BMI value", min_value=0.0, format="%.2f")

    with col3:
        # HbA1c Level (Float input)
        HbA1c_level = st.number_input("HbA1c Level", min_value=0.0, format="%.1f")

    with col1:
        # Blood Glucose Level (Float input)
        blood_glucose_level = st.number_input("Blood Glucose Level", min_value=0, step=1, format="%d")

    with col2:
        # Heart Disease (Radio button)
        heart_disease = st.radio("Heart Disease", options=["Yes", "No"], index=1)

    with col3:
        # Hypertension (Radio button)
        hypertension = st.radio("Hypertension", options=["Yes", "No"], index=1)

    with col1:
        # Gender (Radio button)
        gender = st.radio("Gender", options=["Male", "Female", "Others"], index=0)

    with col2:
        # Smoking History (Radio button)
        smoking_history = st.radio("Smoking History", options=["Never smoked", "Had smoked", "Currently smoking"], index=0)

    # Convert categorical inputs to numeric for prediction
    age_encoded = float(age)
    gender_encoded = {"Male": 0, "Female": 1, "Others": 2}[gender]
    hypertension_encoded = 1 if hypertension == "Yes" else 0
    heart_disease_encoded = 1 if heart_disease == "Yes" else 0
    smoking_history_encoded = {"Never smoked": 0, "Had smoked": 1, "Currently smoking": 2}[smoking_history]

    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction
    if st.button('Diabetes Test Result'):

        user_input_dict = {'gender': gender_encoded, 
                'age': [age_encoded],
                 'hypertension': [hypertension_encoded], 
                 'heart_disease': [heart_disease_encoded],
                 'smoking_history': [smoking_history_encoded],
                  'bmi': [bmi],
                  'HbA1c_level': [HbA1c_level],
                   'blood_glucose_level': [blood_glucose_level]}

        user_input = [[
            gender_encoded,
            age_encoded,
            hypertension_encoded,
            heart_disease_encoded,
            smoking_history_encoded,
            bmi,
            HbA1c_level,
            blood_glucose_level,
        ]]

        user_input_df = pd.DataFrame(user_input_dict)

        user_input_scaled = scaler.transform(user_input_df)
        diab_prediction = diabetes_model.predict(user_input_scaled)

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

elif (selected == 'Parkinson Prediction'):
    st.title("Parkinson Prediction using ML") #page title

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)