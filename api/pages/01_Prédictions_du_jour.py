
# -*- coding: utf-8 -*-
import pandas as pd
import streamlit as st
from PIL import Image


st.set_page_config(page_title="PonAI", page_icon=":horse_racing:", \
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

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
link = '[Informations](https://ponai-ebal.streamlit.app/A_propos)'
link2 = '[Performances](https://ponai-ebal.streamlit.app/Performances)'
link3 = '[Main](https://ponai-ebal.streamlit.app/app)'

if st.button("Informations"):
    st.markdown(f'''<a href={link}''', unsafe_allow_html=True)
if st.button("Performances"):
    st.markdown(f'''<a href={link2}''', unsafe_allow_html=True)
if st.button("Main"):
    st.markdown(f'''<a href={link3}''', unsafe_allow_html=True)
