# -*- coding: utf-8 -*-

import pandas as pd
import streamlit as st
from fast import predict_winner
import streamlit as st
import requests
from PIL import Image

url = 'https://raw.githubusercontent.com/BastGiu/prevision_horses/master/data/2022-12-06_df_streamlit.csv'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')
unicorn = st.select_slider("Displayed values:", ["🏇🏼", "🦄"])

if unicorn:
    st.write('''# Pon.A.I 🦄''')
else:
    st.write('''# Pon.A.I 🏇🏼''')


data_url = 'https://raw.githubusercontent.com/BastGiu/prevision_horses/master/data/2022-12-06_df_streamlit.csv'
def display_dataframe(data_url):
    df = pd.read_csv(data_url)
    df.drop(columns=["jour", "proba pl"], inplace=True)
    df.rename(columns={'hippo': 'Hippodrome', 'prixnom': 'Prix', 'cheval': 'Cheval', 'numero': 'Numéro','heure':'Heure départ'}, inplace=True)
    return df

st.write('Vous pouvez consulter les prédictions faites par notre IA')
df = display_dataframe(data_url=data_url)
st.dataframe(df)

image = Image.open('prevision_horses/data/images/chevaux.png')
st.image(image, caption='Chevals', use_column_width=False)

image2 = Image.open('prevision_horses/data/images/people.png')
st.image(image2, caption='Nous 4 dans quelques jours', use_column_width=False)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
# Afficher sur streamlit
