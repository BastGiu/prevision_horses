from datetime import datetime
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()
app.state.model = load_model()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.get("/")
def root():
    return {'greeting': 'Hello, are you looking for the best three horses in upcoming PMU race ?'}

@app.get("/predict")
def predict_winner():
    df = pd.read_csv('/Users/bastiengiudicelli/code/BastGiu/prevision_horses/2022-12-04_df_pred.csv')
    return df

# app.state.model.predict(...)
