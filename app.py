import numpy as np
import pandas as pd
import pickle
import streamlit as st
import json
import math
import base64

result = None
bsk=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]


with open(
        r"/Users/akashsharma/PycharmProjects/pythonProject/bangalore_home_prices_model.pickle",
        'rb') as f:
    __model = pickle.load(f)

with open(r"/Users/akashsharma/PycharmProjects/pythonProject/Columns.json", 'r') as obj:
    __data_columns = json.load(obj)["Columns"]
    __locations = __data_columns[3:]

def get_predicted_price(
location, sqft, bath, bhk):
    try:
        loc_index = __data_columns.index(location.lower())

    except ValueError as e:

        loc_index = -1


    lis = np.zeros(len(__data_columns))
    lis[0] = sqft
    lis[1] = bath
    lis[2] = bhk


    price = round(__model.predict([lis])[0], 2)
    strp = ' lakhs'

    if math.log10(price) >= 2:
        price = price / 100
        price = round(price, 2)
        strp = " crores"

    return str(price) + strp


def main():
    global result
    st.title("Bangalore House Price Predictor")
    html_temp = """
           <div>
           <h3>House Price Prediction ML app</h3>
           </div>
           """
    st.markdown(html_temp, unsafe_allow_html=True)

    total_sqft = st.text_input("Total Sq feet")

    bathroom = st.selectbox("Number of Bathrooms",bsk)

    bhk=st.selectbox("bhk",bsk)

    location = st.selectbox("Location", __locations)

    if st.button("Predict"):
        result = get_predicted_price(location, total_sqft, bathroom, bhk)

    st.success(f"Price = {result}")


if __name__ == "__main__":
    main()