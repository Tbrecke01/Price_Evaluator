# Dependencies
import pandas as pd
import streamlit as st
import numpy as np
from sqlalchemy import create_engine
import psycopg2
from config import password
import time
from ML_Evaluator import evaluate_price

# Function to generate predictions page
def show_predict_page(df):
    st.title("Price Evaluator")

    # Dropdown menu options
    product_names = list(df['Product Name'].unique())
    merchants = ("Amazon.com", "Bestbuy.com", "Walmart.com", "bhphotovideo.com","Others")
    product_conditions = ("New", "Used")

    # Generate input form
    with st.form('user_form'):
        # Splits the page width for four input columns
        box1, box2, box3, box4 = st.columns((3,2,2,2))

        # Create Input Boxes & retain user input as variables
        with box1:
            item_name = st.selectbox("Enter Product Name", product_names)
        with box2:
            item_price = st.number_input("Enter your price")
        with box3:
            retailer = st.selectbox("Retailer", merchants)
        with box4:
            p_condition = st.selectbox("Product Condition", product_conditions)

        # Submit button for Input Form
        submitted = st.form_submit_button('Submit')
    
    # Runs Machine Learning Model each time input form is 'submitted' by user
    if submitted:     
        # Adds spinner after clicking the button
        with st.spinner("Searching for your product"):
            time.sleep(1)

        # Filter df for item_name in order to find corresponding product_id
        product_id = df['id'].loc[df['Product Name'] == item_name].iloc[0]
        
        # Use ML_Evaluator to make a prediction based on user input
        eval = evaluate_price(product_id, item_price, p_condition, retailer)
        if eval == True:
            st.success("Seems like a Good Deal!")
            st.balloons()
        if eval == False:
            st.warning("May Not be Discounted.")

        # Print output df showing all product details matching selected product name
        output_df = df.loc[df["Product Name"] == item_name]
        st.write(output_df[['Product Name', 'Price', 'Merchant', 'Product Condition', 'On Sale']])
        

# Add high level visualizations to the page
def charts(df):       
        
    g1, g2 = st.columns((5,5))

    with g1:
        st.write("### Bar Chart ")
        chart_data = pd.DataFrame(
        df["prices_amountmax"],
        df["Price"])
        st.bar_chart(chart_data)

    with g2:
        st.write("### linear Chart ")
        chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['a', 'b', 'c'])
        st.line_chart(chart_data)




    