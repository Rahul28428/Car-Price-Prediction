# test_predict.py

import requests

url = "http://127.0.0.1:8000/predict"
data = {
    'year': 2014,
    'km_driven': 145500,
    'fuel': 1,
    'seller_type': 1,
    'transmission': 1,
    'owner': 1,
    'mileage': 23.40,
    'engine': 1248.0,
    'max_power': 74.0,
    'seats': 5
}

response = requests.post(url, json=data)

# Print status code and response text for debugging
print("Status Code:", response.status_code)
print("Response Text:", response.text)

try:
    json_response = response.json()
    print("JSON Response:", json_response)
except requests.exceptions.JSONDecodeError:
    print("Response is not in JSON format")
