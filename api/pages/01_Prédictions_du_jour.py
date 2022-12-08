
# -*- coding: utf-8 -*-
import pandas as pd
import streamlit as st
from PIL import Image
import streamlit as st

st.set_page_config(page_title="PonAI", page_icon="🏇🏼", \
                    menu_items={"About": "A project made by Lucas, Edouard, Arnaud & Bastien"})

st.sidebar.markdown("# Prédictions du jour")
data_url = 'https://raw.githubusercontent.com/BastGiu/prevision_horses/master/data/df_pred_2022-12-08_pr_bastos.csv'
def display_dataframe(data_url):
    df = pd.read_csv(data_url)
    df.drop(columns=["proba pl", "country"], inplace=True)
    df.heure = df.heure.map(lambda x: str(x)[0:-3])
    df.rename(columns={'hippo': 'Hippodrome', 'prixnom': 'Prix', 'cheval': 'Cheval','numero' : 'Numéro','heure':'Heure course'}, inplace=True)
    return df[["Hippodrome", "Heure course", "Prix", "Cheval", "Numéro"]]

st.markdown("<h2 style='text-align: center;'>👇    Prédictions du jour    👇</h2>", unsafe_allow_html=True)
st.write("\n \n \n \n \n")
df = display_dataframe(data_url=data_url)
st.markdown("Jeudi 8 décembre 2022")
st.dataframe(df)

st.write("\n \n \n \n \n")
st.markdown("<h2 style='text-align: center;'>Qu'est-ce que PonAI ? 🏇🏼</h2>", unsafe_allow_html=True)
st.write("PonAI est une intelligence artificielle (AI) qui fournit des tuyaux pour les courses hippiques du jour. Il s'agit d'un algorithme de machine learning qui est entrainé pour prédire les chevaux <i>placés</i>.\n", unsafe_allow_html=True)
st.write("\n \n ")
st.write("\n \n ")

# People image
image2 = Image.open('data/images/people.png')
st.image(image2, caption='  Youpi !', width=650)

st.write("\n \n \n")
st.write("\n \n \n")

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
    st.session_state.emoji = ":point_up_2:"

emojis = [":racehorse:", ":horse_racing:", ":carousel_horse:", ":unicorn_face:", ":money_with_wings:"]

#if st.button("Magic Button"):
#    st.write(' ## Prédictions du jour de ponAI 🦄')
#else:
#    st.write(' ## Prédictions du jour de ponAI 🏇🏼')

# Display dataframe

# st.write("ponAI est une intelligence artificielle qui a pour but de donner des prédictions sur le podium final")
col1, col2, col3 , col4, col5 = st.columns(5)

with col1:
    pass
with col2:
    pass
with col4:
    pass
with col5:
    pass
with col3 :
    center_button = st.button(f"Magic button {st.session_state.emoji} \n", on_click=random_emoji)
