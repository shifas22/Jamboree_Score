import streamlit as st
import pandas as pd
import joblib 

model= joblib.load('model.pkl') 

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

