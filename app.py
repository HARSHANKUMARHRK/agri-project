import streamlit as st
import joblib


st.title("SMACRO - Humidity Prediction")
temp = st.number_input("Enter Temperature")
number=int(temp)

if st.button('Predict'):
    # st.write('Why hello there')
    model=joblib.load("model_regression")
    res=model.predict([[number]])
    st.success(res)
else:
    st.write('Please Enter valid input')