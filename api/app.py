# -*- coding: utf-8 -*-

import pandas as pd
import streamlit as st
from fast import predict_winner
import streamlit as st
import requests

url = 'https://raw.githubusercontent.com/BastGiu/prevision_horses/master/data/2022-12-06_df_streamlit.csv'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')
if st.button('Magic button'):
    st.write('''
            # Pon.A.I 🦄
            ''')
else:
    st.write('''
            # Pon.A.I 🏇🏼
            ''')


data_url = 'https://raw.githubusercontent.com/BastGiu/prevision_horses/master/data/2022-12-06_df_streamlit.csv'
def display_dataframe(data_url):
    df = pd.read_csv(data_url)
    df.drop(columns="jour", inplace=True)
    df.rename(columns={'hippo': 'Hippodrome', 'prixnom': 'Prix', 'cheval': 'Nom', 'numero': 'Numéro','heure':'Départ de la course', 'proba pl':"Probabilité d'être classé"}, inplace=True)
    return df

st.write('Here you can consult our predictions')
df = display_dataframe(data_url=data_url)
st.dataframe(df)



# Afficher sur streamlit
