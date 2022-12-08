# -*- coding: utf-8 -*-

import pandas as pd
import streamlit as st
from PIL import Image
import streamlit as st

st.set_page_config(
    page_title='ponAI',
    page_icon='🏇🏼')


def main_page():
    st.sidebar.markdown("# Main page")

def performances():
    st.markdown("# Bonnes prédictions de la semaine")
    st.sidebar.markdown("# Bonnes prédictions")

page_names_to_funcs = {
    "Main Page": main_page,
    "Performances du modèle": performances,
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
