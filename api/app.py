# -*- coding: utf-8 -*-
import pandas as pd
from PIL import Image
import streamlit as st

st.set_page_config(
    page_title='ponAI',
    page_icon='🏇🏼')

def performances():
    st.markdown("# Bonnes prédictions de la semaine")
    st.markdown("### Performances du modèle sur les cinq derniers jours")
    st.sidebar.markdown("#  Performances du modèle")

def main_page():
    st.sidebar.markdown("# Main page")

page_names_to_funcs = {
    "Main Page": main_page,
    "Performances du modèle": performances,
}

selected_page = st.sidebar.selectbox("Navigate", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()
