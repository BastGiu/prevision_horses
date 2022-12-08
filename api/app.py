# -*- coding: utf-8 -*-
import pandas as pd
import streamlit as st
from PIL import Image
import streamlit as st

st.set_page_config(page_title="PonAI", page_icon=":horse_racing:", \
                    menu_items={"About": "A project made by Lucas, Edouard, Arnaud & Bastien"})

url = 'https://raw.githubusercontent.com/BastGiu/prevision_horses/master/data/2022-12-06_df_streamlit.csv'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

st.markdown("<h1 style='text-align: center;'>PonAI 🏇🏼</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>L'AI qui donne des tuyaux </h3>", unsafe_allow_html=True)

# Horses image
image = Image.open('data/images/chevaux.jpg')
st.image(image, caption='Chevaux qui galopent', width=650)

link = '[PredictionsJour](https://ponai-ebal.streamlit.app/Pr%C3%A9dictions_du_jour)'
st.markdown(link, unsafe_allow_html=True)

link = '[Performances](https://ponai-ebal.streamlit.app/Performances)'
st.markdown(link, unsafe_allow_html=True)

link = '[Informations](https://ponai-ebal.streamlit.app/A_propos)'
st.markdown(link, unsafe_allow_html=True)
