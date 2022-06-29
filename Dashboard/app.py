# Dependencies
import pandas as pd
import json
import requests
import streamlit as st
from main_page import show_predict_page, charts
from graph_page import show_table_page
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from config import password
from sqlalchemy import create_engine

st.set_page_config(layout ="wide")

# Connect to RDS Database to query price_data table and store as pandas dataframe
url = f"postgresql://postgres:{password}@final-project.crnuve3iih8x.us-east-1.rds.amazonaws.com:5432/postgres"
engine = create_engine(url)
connect = engine.connect()
query = "SELECT id, name, prices_amountmax, prices_amountmin, prices_issale, prices_merchant, prices_condition FROM price_data"
df = pd.read_sql(query, con=connect)
# df.to_csv('cleaned.csv')

#Renaming the columns that we want to present on the website
df.rename(columns = {"name": "Product Name", 
            "prices_amountmin": "Price", 
            "prices_merchant": "Merchant",
            "prices_condition": "Product Condition",
            "prices_issale": "On Sale"},
            inplace = True)

# Adding animated graphic
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_hello = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_w5hernhv.json")
st_lottie(
    lottie_hello, 
    # key = "hello",
    speed = 1,
    reverse = False,
    height = 150,
    width = 200
)

# Option menu (Predictions and Visualizations tabs)
selected = option_menu(menu_title = "Options",
 options = ["Predictions", "Visualizations"], 
 menu_icon = "menu-button-fill",
 icons = ["activity", "bar-chart-fill"], 
 default_index = 0, 
 orientation = "horizontal")

# Show selected tab from option menu
if selected == "Predictions":
    show_predict_page(df), charts(df)
else:
    show_table_page()