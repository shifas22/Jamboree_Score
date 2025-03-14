import streamlit as st
import pandas as pd
import joblib 

model= joblib.load('model.pkl') 
page=st.sidebar.selectbox('Pages',('Admission Prediction','About Data'))

if page=='Admission Prediction':
    GRE_Score =st.number_input('GRE Score')
    TOEFL_Score=st.number_input('TOEFL Score')
    University_Rating=st.number_input('University Rating')
    SOP=st.number_input('SOP')
    LOR=st.number_input('LOR')
    CGPA=st.number_input('CGPA')
    Research =st.selectbox('Research',('YES','NO'))
    Research= 1 if Research=='YES' else 0
    
    
    data=pd.DataFrame({'GRE Score':[GRE_Score], 'TOEFL Score':[TOEFL_Score], 'University Rating':[University_Rating], 'SOP':[SOP],'LOR ':[LOR], 'CGPA':[CGPA], 'Research':[Research]})
    # st.write(data)
    
    pred=model.predict(data)[0]
    pred=pred*100
    pred=round(pred,2)
    if st.button('Check'):
        st.write(f'You Have {pred} Chance to Get thi Admission')

else : 
    st.write('''The Jamboree Linear Regression dataset is designed to estimate the chances of graduate admission from an Indian perspective. It contains several features that can be used to predict the likelihood of a student's acceptance into a graduate program. Here's a breakdown of each feature:

Serial No.: A unique identifier for each record in the dataset.

GRE Score: Graduate Record Examination score, ranging up to 340.

TOEFL Score: Test of English as a Foreign Language score, ranging up to 120.

University Rating: An ordinal rating of the university, typically on a scale from 1 to 5.

SOP: Strength of Statement of Purpose, rated on a scale from 1 to 5.

LOR: Strength of Letter of Recommendation, rated on a scale from 1 to 5.

CGPA: Undergraduate Cumulative Grade Point Average, on a scale of 10.

Research: Indicates research experience; 1 if the applicant has research experience, 0 otherwise.

Chance of Admit: The probability of admission, ranging from 0 to 1.

These features collectively provide a comprehensive profile of an applicant, which can be utilized to predict their chances of being admitted to a graduate program.''')

