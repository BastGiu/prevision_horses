import streamlit as st
import pandas as pd

st.markdown("# Performances ")
st.markdown("### Bonnes prédictions du modèle sur la semaine écoulée")
st.markdown("### Données d'hier ")

data_url = 'https://raw.githubusercontent.com/BastGiu/prevision_horses/master/data/df_perf_modele_2022-12-03__2022-12-07.csv'
def display_dataframe(data_url):
    df = pd.read_csv(data_url)
    df.drop(columns=["jour", "proba pl"], inplace=True)
    df.heure = df.heure.map(lambda x: str(x)[0:-3])
    df.rename(columns={'hippo': 'Hippodrome', 'prixnom': 'Prix', 'cheval': 'Cheval','numero' : 'Numéro','heure':'Heure course'}, inplace=True)
    return df

display_dataframe(data_url=data_url)
