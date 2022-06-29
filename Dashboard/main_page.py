# dependencies
import pandas as pd
from sklearn import *
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from collections import Counter
from soupsieve import escape
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
import time
from ML_Evaluator import evaluate_price

# Connect to RDS Database to query price_data table and store as csv (locally)
url = f"postgresql://postgres:{password}@final-project.crnuve3iih8x.us-east-1.rds.amazonaws.com:5432/postgres"
engine = create_engine(url)
connect = engine.connect()
query = "SELECT id, name, prices_amountmax, prices_amountmin, prices_issale, prices_merchant, prices_condition FROM price_data"
df = pd.read_sql(query, con=connect)
df.to_csv('cleaned.csv')

def show_predict_page():

    st.title("Price Evaluator")

    merchant = ("Amazon.com", "Bestbuy.com", "Walmart.com", "bhphotovideo.com","Others")
    products_condition = ("New", "Used")
    #item_id = st.text_input("enter your item ID")
    
    box1, box2, box3, box4 = st.columns((3,2,2,2))   
    with box1:
        item_name = st.text_input("Enter Product Name")
    with box2:
        item_price = st.number_input("Enter your price")  
    with box3:
        retailer = st.selectbox("Retailer", merchant)
    with box4:
        p_condition = st.selectbox("Product Condition", products_condition)
    
    product_id = 'AVpgMuGwLJeJML43KY_c'

    searchButton = st.button("Search")

    if searchButton:     
        df = pd.read_csv('cleaned.csv')

        with st.spinner("Searching for your product"):
            time.sleep(1)

        df.rename(columns = {"name": "Product Name", 
            "prices_amountmin": "Price", 
            "prices_merchant": "Merchant",
            "prices_condition": "Product Condition"},
            inplace = True)

        st.balloons()
        st.write(df)
        # df = pd.read_csv("cleaned.csv")
        
        user_df = df.loc[df["Product Name"] == item_name]
        st.write(user_df)
        
    eval = evaluate_price(product_id, item_price, p_condition, retailer)
    if eval == True:
        st.success("Seems like Good Deal!")
    if eval == False:
        st.warning("May Not be the Best Deal!")
    

        # searched_data = pd.DataFrame(n,p)
        # st.write(searched_data)


    st.title("Data Visualization")
        
    df = pd.read_csv("cleaned.csv")
        
    g1, g2 = st.columns((5,5))

    with g1:
        st.write("### Bar Chart ")
        chart_data = pd.DataFrame(
        df["prices_amountmax"],
        df["prices_amountmin"])
        st.bar_chart(chart_data)

    with g2:
        st.write("### linear Chart ")
        chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
        st.line_chart(chart_data)





    