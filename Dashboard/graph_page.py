import streamlit as st
import numpy as np
import pandas as pd
import eel


def show_table_page():
    
    st.title("Data Visualization") 

    eel.init("Dashboard/static")
    eel.start("index.html")
