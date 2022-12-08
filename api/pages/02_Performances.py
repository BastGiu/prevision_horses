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

link = 'https://ponai-ebal.streamlit.app/Pr%C3%A9dictions_du_jour'
link2 = 'https://ponai-ebal.streamlit.app/A_propos'
link3 = 'https://ponai-ebal.streamlit.app/app'
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown(f'''<a href={link3} target="_self"><button style="background-color:Ivory;">Page principale</button></a>''', unsafe_allow_html=True)
with col2:
    pass
with col3 :
    st.markdown(f'''<a href={link} target="_self"><button style="background-color:Ivory;">Prédictions du jour</button></a>''', unsafe_allow_html=True)
with col4:
    pass
with col5:
    st.markdown(f'''<a href={link2} target="_self"><button style="background-color:Ivory;">A propos</button></a>''', unsafe_allow_html=True)
