"""
 @author: Mbaka JohnPaul

 """

import uvicorn
from fastapi import FastAPI
from parkinson import Parkinson
import numpy as np
import pickle 
import pandas as pd

app = FastAPI()
pickle_in = open("pk_knn_model.pkl","rb")
classifier = pickle.load(pickle_in)

@app.get('/')
def index():
    return {'message': 'Hello, welcome to Parkinson-ML'}

@app.post('/predict')
def predict_parkinsons(data:Parkinson):
    data = data.dict()
    mdvpFo = data["MDVPFo"]
    mdvpFhi = data['MDVPFhi']
    mdvpFlo = data['MDVPFlo']
    mdvpJitter = data['MDVPJitter']
    mdvpJitterAbs = data['MDVPJitterAbs']
    mdvpRAP = data['MDVPRAP']
    mdvpPPQ = data['MDVPPPQ']
    jitterDDP = data['JitterDDP']
    mdvpShimmer = data['MDVPShimmer']
    mdvpShimmerdB = data['MDVPShimmerdB']
    shimmerAPQ3 = data['ShimmerAPQ3']
    shimmerAPQ5 = data['ShimmerAPQ5']
    mdvpAPQ = data['MDVPAPQ']
    shimmerDDA = data['ShimmerDDA']
    nHR = data['NHR']
    hNR = data['HNR']
    rPDE = data['RPDE']
    dFA = data['DFA']
    spread1 = data['spread1']
    spread2 = data['spread2']
    d2 = data['D2']
    pPE = data['PPE'] 

    prediction = classifier.predict([[mdvpFo, mdvpFhi, mdvpFlo,mdvpJitter, mdvpJitterAbs, mdvpRAP, mdvpPPQ,jitterDDP,mdvpShimmer,mdvpShimmerdB,shimmerAPQ3,shimmerAPQ5,mdvpAPQ,shimmerDDA,nHR,hNR,rPDE,dFA,spread1,spread2,d2,pPE]])
    return{
        'prediction': str(prediction)
    }


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port= 8008)
