# streamlit_app.py

import streamlit as st
import requests
from PIL import Image

# Page config
st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Load an image to make the UI more visually appealing
header_image = Image.open("car.jpg")

# Display the header image
st.image(header_image, use_column_width=True)

# Title and subtitle
st.title("Car Price Prediction App")
st.subheader("Predict the price of a car based on its specifications")

# Create columns for input fields to make the UI cleaner
col1, col2 = st.columns(2)

with col1:
    year = st.number_input("Year", min_value=1900, max_value=2024, value=2014)
    km_driven = st.number_input("KM Driven", min_value=0, max_value=1_000_000, value=145500)
    fuel = st.selectbox("Fuel", options=["Diesel", "Petrol", "LPG", "CNG"])
    seller_type = st.selectbox("Seller Type", options=["Individual", "Dealer", "Trustmark Dealer"])

with col2:
    transmission = st.selectbox("Transmission", options=["Manual", "Automatic"])
    owner = st.selectbox("Owner", options=["First Owner", "Second Owner", "Third Owner", "Fourth & Above Owner", "Test Drive Car"])
    mileage = st.number_input("Mileage (km/ltr/kg)", min_value=0.0, max_value=100.0, value=23.4)
    engine = st.number_input("Engine (CC)", min_value=0.0, max_value=10000.0, value=1248.0)
    max_power = st.number_input("Max Power (bhp)", min_value=0.0, max_value=1000.0, value=74.0)
    seats = st.number_input("Seats", min_value=1, max_value=20, value=5)

# Add a predict button with some spacing
st.markdown("##")
if st.button("Predict Price"):
    data = {
        "year": year,
        "km_driven": km_driven,
        "fuel": 1 if fuel == "Diesel" else 2 if fuel == "Petrol" else 3 if fuel == "LPG" else 4,
        "seller_type": 1 if seller_type == "Individual" else 2 if seller_type == "Dealer" else 3,
        "transmission": 1 if transmission == "Manual" else 2,
        "owner": 1 if owner == "First Owner" else 2 if owner == "Second Owner" else 3 if owner == "Third Owner" else 4 if owner == "Fourth & Above Owner" else 5,
        "mileage": mileage,
        "engine": engine,
        "max_power": max_power,
        "seats": seats
    }
    
    response = requests.post("http://127.0.0.1:8000/predict", json=data)
    
    if response.status_code == 200:
        prediction = response.json()["prediction"]
        st.success(f"The predicted price is: Rs { prediction:,.2f}")
    else:
        st.error("An error occurred during prediction.")

# Add some custom CSS to style the UI
st.markdown(
    """
    <style>
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        transition-duration: 0.4s;
    }

    .stButton button:hover {
        background-color: white;
        color: black;
        border: 2px solid #4CAF50;
    }

    .stNumberInput, .stSelectbox {
        padding: 5px;
    }

    .stNumberInput input, .stSelectbox select {
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
