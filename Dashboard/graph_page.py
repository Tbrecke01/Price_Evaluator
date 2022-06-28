from re import A
import streamlit as st
import pickle 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import datapane as dp
import eel

def load_model():
    df = pd.read_csv("cleaned3.csv")
    return df

df = load_model()


def show_table_page():
    
    st.title("Data Visualization") 

    eel.init("static")
 
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

    eel.start("index.html")

    # st.markdown(f"""<a href = "http://127.0.0.1:5500/static/index.html"> click here </a>""")
    # st.write("http://127.0.0.1:5500/static/index.html")

    

