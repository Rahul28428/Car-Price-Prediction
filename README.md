# Car Price Prediction Model

This project aims to predict car prices using machine learning. The model leverages a dataset to train a RandomForestRegressor and deploys the prediction system using FastAPI and Streamlit.

## Project Components

1. **Colab Notebook (`Colab_Notebook.ipynb`)**:
   - Preprocesses the dataset (`cardekho.csv`) by handling missing values, encoding categorical features, and saving the cleaned data.
   - Performs Exploratory Data Analysis (EDA) using visualizations to understand the relationships between variables.
   - Trains a RandomForestRegressor model and evaluates its performance using metrics such as Mean Absolute Error, Mean Squared Error, and R2 Score.
   - Utilizes GridSearchCV for hyperparameter tuning to improve model accuracy.
   - Saves the trained model with the best parameters.

2. **FastAPI Application (`main.py`)**:
   - Implements a RESTful API for car price predictions.
   - Serves the trained model to provide price estimates based on input features.

3. **Testing Script (`test_predict.py`)**:
   - Tests the FastAPI application to ensure that the prediction endpoint is working correctly and returning accurate results.

4. **Streamlit Application (`streamlit_app.py`)**:
   - Creates an interactive web interface using Streamlit.
   - Allows users to input car features and view the predicted price.

5. **Deployment**:
   - Deployed the project on Google Cloud Platform (GCP) using the command-line SDK.
   - Ensures that the application is accessible and operational in a cloud environment.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Rahul28428/Car-Price-Prediction
   cd Car-Price-Prediction
   ```
2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Run the FastAPI application:
```bash
uvicorn main:app --reload
```

4. Launch the Streamlit application:
```bash
streamlit run streamlit_app.py
```
5. Deplying on GCP
Follow the steps in this youtube tutorial Video : <a href="https://www.youtube.com/watch?v=xcODUk0o6tU"> Link </a>

## Model Performance
Best R2 Score: Approximately 91.81%

## Acknowledgements
Dataset: <a href="https://www.kaggle.com/datasets/sukhmandeepsinghbrar/car-price-prediction-dataset?select=cardekho.csv">cardekho.csv</a>
Tools: Google Colab, FastAPI, Streamlit, Google Cloud Platform
