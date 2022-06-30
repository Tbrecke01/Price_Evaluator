import streamlit as st
import streamlit.components.v1 as components

# Show Tableau Dashboard
def show_table_page():
    st.title("Data Visualization") 
    HtmlFile=open('Dashboard/static/tableau_dashboard.html')
    components.html(HtmlFile.read(), height=1000)
