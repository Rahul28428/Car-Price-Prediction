from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import pandas as pd
import logging

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

with open('car_price_prediction_model.pkl', 'rb') as f:
    model = pickle.load(f)

class CarPredictionInput(BaseModel):
    year: int
    km_driven: int
    fuel: int
    seller_type: int
    transmission: int
    owner: int
    mileage: float
    engine: float
    max_power: float
    seats: int

@app.get("/")
def read_root():
    return {"message": "Welcome to the Car Price Prediction API"}

@app.post("/predict")
def predict(input: CarPredictionInput):
    try:
        input_data = pd.DataFrame([input.dict().values()], 
                                  columns=['year', 'km_driven', 'fuel', 'seller_type', 'transmission', 'owner', 'mileage(km/ltr/kg)', 'engine', 'max_power', 'seats'])
        logger.info(f"Input Data: {input_data}")
        prediction = model.predict(input_data)
        logger.info(f"Prediction: {prediction}")
        return {"prediction": prediction[0]}
    except Exception as e:
        logger.error(f"Error during prediction: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
