import streamlit as st
import pandas as pd
import numpy as np


# import findspark
# findspark.init()
# import pyspark
# from pyspark.sql import SparkSession
# spark = SparkSession.builder.master("local[1]").appName("SparkByExamples.com").getOrCreate()
# from pyspark.ml.classification import RandomForestClassificationModel
# importing 

st.title('My first app')
st.header('Car Price prediction')
st.subheader('House Prediction')
account_length = int(st.slider('Select total active month', 1, 250))
st.text('Like this video and subsribe it')

st.title("Salary Pridiction")
nav = st.sidebar.radio("Navigation",["Home","Prediction", "contribution"])
if nav == "Home":
    st.write('Home')
    # st.image('data//premium_photo-1664637952648-8f0b876bad49.avif')
elif nav=="Prediction":
    st.write('Pred')
else:
    st.write('contri')
