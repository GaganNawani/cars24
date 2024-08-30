import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.header('Car Price Prediction')

#inputs from user
col1, col2 = st.columns(2)

with col1:
    seat_inp = st.selectbox(
    'Enter the number of Seats: ',
    (4, 5, 7, 9, 11))

with col2:
    fuel_type_inp = st.selectbox(
    'Enter the Fuel type: ',
    ('Diesel', 'Petrol', 'CNG', 'LTG', 'Electric'))

#year = st.number_input('Insert a number')

col1, col2 = st.columns(2)

with col1:
    transmission_inp = st.selectbox(
        'Enter the Transmission type: ',
        ('Manual', 'Automatic'))

with col2:
    engine_inp = st.slider('Engine CC',500, 5000, 100)


encoding_dictionary = {
    'fuel_type': {'Diesel':1, 'Petrol': 2, 'CNG': 3, 'LPT': 4, 'Electric': 5},
    'transmission_type' : {'Manual': 1, 'Automatic': 2}
}


#loading the model
def model_pred(fuel_type_encoded, transmission_encoded, engine_inp, seat_inp):
    with open('model_file','rb') as file:
        model = pickle.load(file)

        input_features = [[2014,2,130000,fuel_type_encoded,transmission_encoded,19.7,engine_inp,46.3,seat_inp]]

        return model.predict(input_features)
    

if st.button('Predict'):
    fuel_type_encoded = encoding_dictionary['fuel_type'][fuel_type_inp]
    transmission_encoded = encoding_dictionary['transmission_type'][transmission_inp]

    second_hand_price = model_pred(fuel_type_encoded, transmission_encoded, engine_inp, seat_inp)
    st.write('Predicted Price is: ',str(second_hand_price))
