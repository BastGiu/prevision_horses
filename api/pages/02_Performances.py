import streamlit as st
import pandas as pd

st.markdown("# Performances ")
st.markdown("### Bonnes prédictions récentes ")
st.sidebar.markdown("# Performances du modèle")

data_url = 'https://raw.githubusercontent.com/BastGiu/prevision_horses/master/data/df_perf_modele_2022-12-03__2022-12-07.csv'
def display_dataframe(data_url):
    df = pd.read_csv(data_url)
    df.drop(columns=["pl", "id", "coteprob","cotedirect","predi_placé", "bonne_pred", "numcourse", "proba pl"], inplace=True)
    df["cl"].astype(int)
    df.rename(columns={'cl':'Classement', 'jour' : 'Date','hippo': 'Hippodrome', 'prixnom': 'Prix', 'cheval': 'Cheval','numero' : 'Numéro','heure':'Heure course'}, inplace=True)
    return df
df = display_dataframe(data_url=data_url)
st.dataframe(df)
