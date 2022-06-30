# Dependencies
import pandas as pd
import streamlit as st
import numpy as np
from sqlalchemy import create_engine
import psycopg2
from config import password
import time
from ML_Evaluator import evaluate_price
import altair as alt

# Function to generate predictions page
def show_predict_page(df):
    st.title("Price Evaluator")

    # Dropdown menu options
<<<<<<< HEAD
    product_names = list(df['Product Name'].unique())
    merchants = list(df['Merchant'].unique())
    product_conditions = list(df['Product Condition'].unique())
=======
    product_names = list(df['name'].unique())
    merchants = list(df['prices_merchant'].unique())
    product_conditions = list(df['prices_condition'].unique())
>>>>>>> 1286773897db677b4f59626007dc81ffcc81c1a2

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
            retailer = st.selectbox("Select a Retailer", merchants)
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
        product_id = df['id'].loc[df['name'] == item_name].iloc[0]
        
        # Use ML_Evaluator to make a prediction based on user input
        eval = evaluate_price(product_id, item_price, p_condition, retailer)
        if eval == True:
            st.success("Seems like a Good Deal!")
            st.balloons()
        if eval == False:
            st.warning("May Not be Discounted.")

        # Print output df showing all product details matching selected product name
        output_df = df.loc[df["name"] == item_name]
        display_df = pd.DataFrame({'Product Name': output_df['name'], 
                                    'Price': output_df['prices_amountmin'], 
                                    'Merchant': output_df['prices_merchant'], 
                                    'Product Condition': output_df['prices_condition'],
                                    'On Sale': output_df['prices_issale']})
        st.write(display_df.style.format({"Price": "{:.2f}"}))
    
    # Generate columns of equal width for interactive visualizations
    g1, g2 = st.columns((5,5))

    # Graph 1 - Price History
    with g1:
        output_df = df.loc[df["name"] == item_name]
        chart_data = pd.DataFrame({'Date': output_df['prices_dateseen'], 
                                    'Price': output_df['prices_amountmin'],
                                    'Merchant': output_df['prices_merchant']})
        st.write("### Price History")
        st.altair_chart(alt.Chart(chart_data).mark_line().encode(x='Date',
                                                        y='Price',
                                                        color='Merchant'))

    # Graph 2 - Bar Chart
    with g2:
        st.write("### Bar Chart ")
        chart_data = pd.DataFrame(
        df["prices_amountmax"],
        df["prices_amountmin"])
        st.bar_chart(chart_data)




    