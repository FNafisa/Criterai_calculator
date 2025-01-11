import streamlit as st
import pandas as pd

about_page= st.Page(
    page= "Criteria.py",
    title= "Criteria Calculator",
    icon=":material/account_circle:",
    default=True
)

st.title('Criteria Calculator')
st.divider()


col_input, col_output= st.columns(2,gap='large')

with col_input:
    height= st.slider('First Criteria:', 100, 250, 175)
    weight= st.slider('Second Cirteria:', 40, 200, 70)
    bmi= weight / ((height/100)**2)

with col_output:
    st.write(f'# Your Score Is:')
    st.write(f'# {bmi:.2f}')

st.write('### Score Categories')
st.write('- Poor: score is less than 18.5')
st.write('- Normal: score is between 18.5 and 24.9')
st.write('- Extreme: score is between 25 and 29.9')
st.write('- Dangerous: score is 30 or greater')
