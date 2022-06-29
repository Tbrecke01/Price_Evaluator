# dependencies
import pandas as pd
import joblib
import json
import requests
import streamlit as st
from main_page import show_predict_page
from graph_page import show_table_page
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie

st.set_page_config(layout ="wide")

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


selected = option_menu(menu_title = "Options",
 options = ["Predictions", "Visualizations"], 
 menu_icon = "menu-button-fill",
 icons = ["activity", "bar-chart-fill"], 
 default_index = 0, 
 orientation = "horizontal")


if selected == "Predictions":
    show_predict_page()
else:
    show_table_page()