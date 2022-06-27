# dependencies
import pandas as pd
from sklearn import *
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from collections import Counter
from sqlalchemy import create_engine
import joblib
import streamlit as st
import pickle 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import datapane as dp
from sqlalchemy import create_engine
import psycopg2
import plotly.graph_objects as go
import sys
from config import password

def show_predict_page():

    st.title("Price Evaluator")

    merchandise = ("Amazon", "Best Buy", "Walmart", "bhphotovideo","Others")

    #item_id = st.text_input("enter your item ID")
    
    box1, box2, box3= st.columns((3,3,3))   
    with box1:
        item_name = st.text_input("Enter Product Name")
    with box2:
        item_price = st.number_input("Enter your price")  
    with box3:
        retailer = st.selectbox("Retailer", merchandise)


    searchButton = st.button("Search")
    if searchButton:
            # Connect to RDS Database to query price_data table and store as a pandas DataFrame
        url = f"postgresql://postgres:{password}@final-project.crnuve3iih8x.us-east-1.rds.amazonaws.com:5432/postgres"

        engine = create_engine(url)

        connect = engine.connect()

        query = "SELECT name, manufacturer, prices_merchant, prices_amountmin FROM price_data"

        df = pd.read_sql(query, con=connect)

      
        for n in df["name"]:
            if n == item_name:
                st.write(n)

        

        # for p in df["prices_amountmin"]:
        #     if p == item_price:
        #         st.write(p)

        # searched_data = pd.DataFrame(n,p)
        # st.write(searched_data)


    st.title("Data Visualization")
        
    df = pd.read_csv("cleaned3.csv")
        
    g1, g2 = st.columns((5,5))

    with g1:
        st.write("### Bar Chart ")
        chart_data = pd.DataFrame(
        df["prices_amountMax"],
        df["prices_amountMin"])
        st.bar_chart(chart_data)

    with g2:
        st.write("### linear Chart ")
        chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
        st.line_chart(chart_data)





    