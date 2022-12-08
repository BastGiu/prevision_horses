# Contents of ~/my_app/streamlit_app.py
import streamlit as st

def main_page():
    st.markdown("# PonAI 🏇🏼")
    st.sidebar.markdown("# Main page")

def page2():
    st.markdown("# Prevision of tomorrow")
    st.sidebar.markdown("# Prevision of tomorrow ")

page_names_to_funcs = {
    "Main Page": main_page,
    "Page 2": page2,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
