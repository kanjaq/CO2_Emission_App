import streamlit as st
import pandas as pd
import numpy as np
#from #sklearn.ensemble import RandomForestRegressor
import joblib
from PIL import Image
#Color
#load trained model
model = joblib.load("best_model3.pkl")

# Define the app title and layout
st.title("Vehicles Carbon Emissions -2023")
st.text('Fuel consumption ratings and estimated carbon dioxide emissions for vehicles')

image = Image.open('dataset-cover.jpg')
st.sidebar.image(image, caption='Vehicles Carbon Emissions')
#Vehicle_make = st.sidebar.selectbox ('Make',('Ford','Ram','Land Rover' ,'Nissan','Chevrolet','BMW','Aston Martin','Infiniti','Bentley','Dodge','Maserati','Bugatti','Mercedes-Benz','Cadillac','GMC','Audi','Rolls-Royce','Lamborghini','Jeep'))
st.sidebar.markdown('Different vehicles emit different amounts of carbon dioxide (CO2) in relation to the energy they produce when burned. To analyze emissions across different vehicles, compare the amount of CO2 emitted per unit of energy output or heat content', help=None)

# Define input fields for features

Engine_size = st.number_input("Engine Size", min_value=0, max_value=10, value=5, step=1)
Cylinders = st.number_input("Cylinders", min_value=0.0, max_value=30.0, value=10.0, step=1.0)
Fuel = st.selectbox("Fuel, 1 -Regular Gasoline, 2-Premium Gasoline, 3-Ethanol Gas, 4-Diesel, 5-Natural Gas", [1, 2,3,4,5])
Fuel_Consumption = st.number_input("City Fuel Consumption Litres per 100KM ",min_value =5, max_value=30, step=2)
Highway_Fuel_Consumption = st.number_input("Highway Fuel Consumption Litres per 100KM ",min_value =5, max_value=30, step=2)
Comb_Fuel_Consumption = st.number_input("City/ Highway Fuel Consumption Litres per 100KM ",min_value =5, max_value=30, step=2)
CO2_Emmissions = st.selectbox("Estimated CO2 Emmissions", range(50,300,20))
CO2_Rating = st.selectbox("CO2 Ratings", range(0,10,1))
COMB_Rating = st.selectbox("COMB Ratings", range(0,10,1))



#prediction
if st.button('predict'):
    Make_Prediction = model.predict([[Engine_size,CO2_Emmissions,Cylinders,Fuel_Consumption,Highway_Fuel_Consumption,Comb_Fuel_Consumption,CO2_Rating,COMB_Rating,Fuel]])
    output = round(Make_Prediction[0],2)
    st.success('Your Vehicle Carbon Emmission is {}'.format(output))