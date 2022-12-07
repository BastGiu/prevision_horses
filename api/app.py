# -*- coding: utf-8 -*-

import pandas as pd
import streamlit as st
from PIL import Image
import streamlit as st

st.set_page_config(
    page_title='ponAI',
    page_icon='🏇🏼')
url = 'https://raw.githubusercontent.com/BastGiu/prevision_horses/master/data/2022-12-06_df_streamlit.csv'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

st.markdown("<h1 style='text-align: center;'>ponAI 🏇🏼</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>L'AI qui donne des tuyaux </h3>", unsafe_allow_html=True)

# Horses image
image = Image.open('data/images/chevaux.jpg')
st.image(image, caption='Chevaux qui galopent', width=650)

data_url = 'https://raw.githubusercontent.com/BastGiu/prevision_horses/master/data/df_pred_2022-12-07.csv '
def display_dataframe(data_url):
    df = pd.read_csv(data_url)
    df.drop(columns=["jour", "proba pl", "country"], inplace=True)
    df.rename(columns={'hippo': 'Hippodrome', 'prixnom': 'Prix', 'cheval': 'Cheval','numero' : 'Numéro','heure':'Heure course'}, inplace=True)
    return df[["Hippodrome", "Heure course", "Prix", "Cheval", "Numéro"]]

st.markdown("<h2 style='text-align: center;'>👇    Prédictions du jour    👇</h2>", unsafe_allow_html=True)
st.write("\n \n \n \n \n")
df = display_dataframe(data_url=data_url)
st.dataframe(df)
st.write("\n \n \n \n \n")
st.markdown("<h2 style='text-align: center;'>Qu'est-ce que ponAI ? 🏇🏼</h2>", unsafe_allow_html=True)
st.write("<h4> style='text-align: center;'> ponAI est une intelligence artificielle (AI) qui fournit des tuyaux pour les courses hippiques du jour. Il s'agit d'un algorithme de machine learning qui est entrainé pour prédire les chevaux <i>placés</i>.\n </h4>", unsafe_allow_html=True)
st.write("\n")
# People images
image2 = Image.open('data/images/people.png')
st.image(image2, caption='Youpi !', width=650)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# callback to update emojis in Session State
# in response to the on_click event
import random

# callback to update emojis in Session State
# in response to the on_click event
def random_emoji():
    st.session_state.emoji = random.choice(emojis)

# initialize emoji as a Session State variable
if "emoji" not in st.session_state:
    st.session_state.emoji = "👈"

emojis = [":racehorse:", ":horse_racing:", ":carousel_horse:", ":unicorn_face:", ":money_with_wings:"]

st.button(f"Magic button {st.session_state.emoji}", on_click=random_emoji)
#if st.button("Magic Button"):
#    st.write(' ## Prédictions du jour de ponAI 🦄')
#else:
#    st.write(' ## Prédictions du jour de ponAI 🏇🏼')

# Display dataframe

# st.write("ponAI est une intelligence artificielle qui a pour but de donner des prédictions sur le podium final")
