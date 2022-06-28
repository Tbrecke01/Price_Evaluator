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

def show_predict_page():

    st.title("Price Evaluator")

    merchandise = ("Amazon.com", "Bestbuy.com", "Walmart.com", "bhphotovideo.com","Others")
    products_condition = ("New", "Used")
    #item_id = st.text_input("enter your item ID")
    
    box1, box2, box3, box4 = st.columns((3,2,2,2))   
    with box1:
        item_name = st.text_input("Enter Product Name")
    with box2:
        item_price = st.number_input("Enter your price")  
    with box3:
        retailer = st.selectbox("Retailer", merchandise)
    with box4:
        p_condition = st.selectbox("Product Condition", products_condition)

    searchButton = st.button("Search")

    if searchButton:     
        # Connect to RDS Database to query price_data table and store as a pandas DataFrame
        url = f"postgresql://postgres:{password}@final-project.crnuve3iih8x.us-east-1.rds.amazonaws.com:5432/postgres"

        engine = create_engine(url)

        connect = engine.connect()

        query = "SELECT name, prices_amountmin, prices_merchant, prices_condition FROM price_data"
        # query = "SELECT * FROM price_data"

        df = pd.read_sql(query, con=connect)

        with st.spinner("Searching for your product"):
            time.sleep(1)   

        df.rename(columns = {"name": "Product Name", 
        "prices_amountmin": "Price", 
        "prices_merchant": "Merchant",
         "prices_condition": "Product Condition"},
          inplace = True)

        st.balloons()
        st.write(df)
        # df = pd.read_csv("cleaned3.csv")
        
        n, p, r, c = st.columns(4)
        with n:     
            # for n, p, r, c in (df["Product Name"], df["Price"], df["Merchant"], df["Product Condition"]):
            #     if n == item_name & p == item_price & r == retailer & c == p_condition:
            #         st.write(n)
            #         st.write(p)
            #         st.write(r)
            #         st.write(c)
            #         break
            #     elif n!= item_name:
            #         st.write("product not found")
            #         break
             for n in df["Product Name"]:
                if n == item_name:
                    st.write(n)
                    break
                elif n!= item_name:
                    st.write("Not found")
                    break



       
        # with p: 
        #     for p in df["Price"]:
        #         if p == item_price:
        #             st.write(p)
        #             break
        #         elif n!= item_price:
        #             st.write("price not found")
        #             break
                    
        # with r: 
        #     for r in df["Merchant"]:
        #         if r == retailer:
        #             st.write(r)
        #             break

        # with c: 
        #     for c in df["Product Condition"]:
        #         if c == p_condition:
        #             st.write(c)
        #             break
        


        st.success("Good Deal!")

        st.warning("Not a Good Deal!")
    

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





    