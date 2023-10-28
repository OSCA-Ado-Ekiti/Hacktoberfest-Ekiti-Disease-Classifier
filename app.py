import joblib
import streamlit as st
import sklearn
from joblib import load

model = load("model.joblib")

def main():
    st.title("Disease Classifier")
    st.text("This model classfies common disease among Nigeria students")

    
    options = {'': 'Select an option(1 stands for Yes and 0 stands for No)','Yes': 1, 'No': 0,}

    headache = st.selectbox('Headache', list(options.values()))

    fatigue = st.selectbox('Fatigue', list(options.values()))

    ys = st.selectbox('Yelowish Skin', list(options.values()))

    ab = st.selectbox('Abdominal Pain', list(options.values()))

    chills = st.selectbox('Chills', list(options.values()))

    vomiting = st.selectbox('Vomiting', list(options.values()))

    cs = st.selectbox('Continuous Sneezing', list(options.values()))

    cough = st.selectbox('Cough', list(options.values()))

    malaise = st.selectbox('Malaise', list(options.values()))

    hf = st.selectbox('High Fever', list(options.values()))

    itc = st.selectbox('Itching', list(options.values()))

    mp = st.selectbox('Muscle Pull', list(options.values()))

    mf = st.selectbox('Mild Fever', list(options.values()))

    alf = st.selectbox('Acute Liver Failure', list(options.values()))

    dz = st.selectbox('Dizziness', list(options.values()))

    fhr = st.selectbox('Fast Heart Rate', list(options.values()))



    prognosis = {'Allergy': 0, 'Peptic ulcer diseae': 1, 'Diabetes ': 2, 'Gastroenteritis': 3,
       'Bronchial Asthma': 4, 'Hypertension ': 5, 'Migraine': 6, 'Malaria': 7,
       'Chicken pox': 8, 'Typhoid': 9, 'hepatitis A': 10, 'Hepatitis B': 11,
       'Hepatitis C': 12, 'Hepatitis D': 13, 'Hepatitis E': 14, 'Tuberculosis': 15,
       'Common Cold': 16, 'Pneumonia': 17, 'Acne': 18, 'Urinary tract infection': 19}

    def get_result_key(prog_dict, result_value):
        for key, value in prog_dict.items():
            if value == result_value:
                return key

    if st.button('Predict'):
        mkpred = model.predict([[headache, fatigue, ys, ab, chills, vomiting, cs, cough, malaise, hf, itc, mp, mf, alf, dz, fhr]])
        print([headache, fatigue, ys, ab, chills, vomiting, cs, cough, malaise, hf, itc, mp, mf, alf, dz, fhr])
        result = mkpred[0]

        result_key = get_result_key(prognosis, result)

        st.success(f'The result of your diagnosis is {result_key}')

if __name__ == '__main__':
    main()