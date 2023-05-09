from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app=FastAPI()

class model_input(BaseModel):
    N : int
    P : int
    K : int
    temperature : float
    humidity: float
    ph: float

#loading model
#loading saved file
crop_model=pickle.load(open("Crop_recommendation.sav",'rb'))

@app.post('/crop_prediction')
def crop_pred(input_parameters : model_input):
    input_data=input_parameters.json()
    input_dictionary = json.loads(input_data)

    n = input_dictionary['N']
    p = input_dictionary['P']
    k = input_dictionary['K']
    temp = input_dictionary['temperature']
    hm = input_dictionary['humidity']
    ph = input_dictionary['ph']

    input_list=[n,p,k,temp,hm,ph]
    prediction=crop_model.predict([input_list])

    return int(prediction)
  


