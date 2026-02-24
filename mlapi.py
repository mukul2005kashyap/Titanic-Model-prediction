from fastapi import FastAPI , Path , HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel ,Field
import json
import pickle
import numpy as np
import joblib

with open("titanicmodel.pkl" , "rb") as f:
    model = joblib.load(f)


class User_input(BaseModel):
    pclass : int = Field(..., description="p class of user ", gt=0 , le=3)
    sex  : str
    age : int
    sibsp : int
    parch :int
    fare :float =Field(description="enter ticket fare in float ", gt=0 , le=99)

app = FastAPI()
@app.post("/predict")
def predict_chance(data : User_input):
    
    sex_value = 0 if data.sex.lower() == "male" else 1
    # global input_array
    input_array = np.array([[data.pclass, sex_value ,data.age ,data.sibsp ,data.parch , data.fare]])
    prediction = model.predict(input_array)[0]

    if prediction==0:
        return JSONResponse(status_code=200 , content=f"pessanger not survived{prediction}" )
    else:
        return JSONResponse(status_code=200 , content=f"pessanger survived" )


    




























# @app.get("/show")
# def show():
#     return input.tolist()