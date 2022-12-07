# -*- coding: utf-8 -*-

import pandas as pd
import streamlit as st
from PIL import Image
import streamlit as st

url = 'https://raw.githubusercontent.com/BastGiu/prevision_horses/master/data/2022-12-06_df_streamlit.csv'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

st.markdown("<h1 style='text-align: center;'>ponAI 🏇🏼</h1>", unsafe_allow_html=True)

image = Image.open('data/images/chevaux.jpg')
st.image(image, caption='Chevaux', width=800)

data_url = 'https://raw.githubusercontent.com/BastGiu/prevision_horses/master/data/df_pred_2022-12-07.csv '
def display_dataframe(data_url):
    df = pd.read_csv(data_url, index_col=0)
    df.drop(columns=["jour", "proba pl"], inplace=True)
    df.rename(columns={'hippo': 'Hippodrome', 'prixnom': 'Prix', 'cheval': 'Cheval','numero' : 'Numéro','heure':'Heure départ'}, inplace=True)
    return df

if st.button("Magic"):
    st.write(' ## Prédictions du jour de ponAI 🦄')
else:
    st.write(' ## Prédictions du jour de ponAI 🏇🏼')
df = display_dataframe(data_url=data_url)
st.dataframe(df)


image2 = Image.open('data/images/people.png')
st.image(image2, caption='Youpi !', width=800)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
