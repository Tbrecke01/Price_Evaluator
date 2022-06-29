# dependencies
import pandas as pd
from sklearn import *
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from collections import Counter
from soupsieve import escape
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

def show_predict_page(df):

    st.title("Price Evaluator")
    product_names = list(df['name'].unique())
    merchants = ("Amazon.com", "Bestbuy.com", "Walmart.com", "bhphotovideo.com","Others")
    product_conditions = ("New", "Used")
    #item_id = st.text_input("enter your item ID")
    
    box1, box2, box3, box4 = st.columns((3,2,2,2))   
    with box1:
        item_name = st.selectbox("Enter Product Name", product_names)
    with box2:
        item_price = st.number_input("Enter your price")  
    with box3:
        retailer = st.selectbox("Retailer", merchants)
    with box4:
        p_condition = st.selectbox("Product Condition", product_conditions)
    
    df.rename(columns = {"name": "Product Name", 
            "prices_amountmin": "Price", 
            "prices_merchant": "Merchant",
            "prices_condition": "Product Condition"},
            inplace = True)

    searchButton = st.button("Search")

    if searchButton:     

        with st.spinner("Searching for your product"):
            time.sleep(1)

        st.balloons()
        # st.write(df[['Product Name', 'Price', 'Merchant', 'Product Condition']])
        # df = pd.read_csv("cleaned.csv")
        
        user_df = df.loc[df["Product Name"] == item_name]
        st.write(user_df[['Product Name', 'Price', 'Merchant', 'Product Condition', '']])
        
        # Filter df for item_name in order to find product_id
        product_id = df['id'].loc[df['Product Name'] == item_name].iloc[0]    
        eval = evaluate_price(product_id, item_price, p_condition, retailer)
        if eval == True:
            st.success("Seems like Good Deal!")
        if eval == False:
            st.warning("May Not be Discounted.")
    

        # searched_data = pd.DataFrame(n,p)
        # st.write(searched_data)


    st.title("Data Visualization")
        
        
    g1, g2 = st.columns((5,5))

    with g1:
        st.write("### Bar Chart ")
        chart_data = pd.DataFrame(df["Price"])
        st.bar_chart(chart_data)

    with g2:
        st.write("### linear Chart ")
        chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
        st.line_chart(chart_data)





    