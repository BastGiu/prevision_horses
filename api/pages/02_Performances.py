import streamlit as st
import pandas as pd

st.set_page_config(page_title="PonAI", page_icon=":horse_racing:", \
                    menu_items={"About": "A project made by Lucas, Edouard, Arnaud & Bastien"})

st.markdown("# Performances ")
st.markdown("### Bonnes prédictions récentes ")
st.sidebar.markdown("# Performances du modèle")

data_url = 'https://raw.githubusercontent.com/BastGiu/prevision_horses/master/data/df_perf_modele_2022-12-03__2022-12-07.csv'
def display_dataframe(data_url):
    df = pd.read_csv(data_url)
    df.drop(columns=["pl", "id", "coteprob","cotedirect","predi_placé", "bonne_pred", "numcourse", "proba pl"], inplace=True)
    df["cl"] = df["cl"].astype(int)
    df.rename(columns={'cl':'Classement', 'jour' : 'Date','hippo': 'Hippodrome', 'prixnom': 'Prix', 'cheval': 'Cheval','numero' : 'Numéro','heure':'Heure course'}, inplace=True)
    return df
df = display_dataframe(data_url=data_url)
st.dataframe(df)

link = '[PredictionsJour](https://ponai-ebal.streamlit.app/Pr%C3%A9dictions_du_jour)'
st.markdown(link, unsafe_allow_html=True)

link = '[Informations](https://ponai-ebal.streamlit.app/A_propos)'
st.markdown(link, unsafe_allow_html=True)

link = '[Main](https://ponai-ebal.streamlit.app/app)'
st.markdown(link, unsafe_allow_html=True)
