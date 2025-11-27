import streamlit as st
import pandas as pd
import numpy as np 
import pickle

with open("Heart_Diseases.pkl",'rb') as f:
    artifacts=pickle.load(f)

preprocess=artifacts['preprocess']
model=artifacts['model']

def get_result(age,sex,ChestPain,restingBP,Cholesterol,FastingBS,RestingECG,MaxHR,exerciseAnginea,oldPeak,stSlope):
  input=pd.DataFrame([{
      'Age':age,
      'Sex':sex,
      'ChestPainType':ChestPain,
      'RestingBP':restingBP,
      'Cholesterol':Cholesterol,
      'FastingBS':FastingBS,
      'RestingECG':RestingECG,
      'MaxHR':MaxHR,
      'ExerciseAngina':exerciseAnginea,
      'OldPeak':oldPeak,
      'ST_Slope':stSlope
  }])
  
  input_encoded=preprocess.transform(input)
  prdiction=model.predict(input_encoded)[0]
  return int(prdiction)

