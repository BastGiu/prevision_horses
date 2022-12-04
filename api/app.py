import streamlit as st

url = 'https://pmu_breaking.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')
import streamlit as st
'''
# My Stremlit App
'''
import requests

params = {
    'hippo' : str(hippo),
    'prix': str(exhibit),
    'Horse Name': str(horse_name),
    'numero': int(numero),
    'jour': str(day),
    'heure': str(hour),
    'proba pl': int(nb_passenger)
}

BASE_URI = "https://pmu_breaking.ai/predict"
response = requests.get(BASE_URI, params=params).json()
taxiFareApiUrl = 'https://pmu_breaking.streamlit.app/predict'

st.markdown('''Bonjour :)''')
date = st.date_input('Date')
time = st.time_input('Time')
pic_lon = st.number_input('Pickup longitude')
pic_lat = st.number_input('Pickup latitude')
drop_lon = st.number_input('Dropoff longitude')
drop_lat = st.number_input('Dropoff latitude')
nb_passenger = st.number_input('How many passengers ?')
url = 'https://pmu_breaking.ai/predict'

st.text('Fixed width text')
st.markdown(f'The first 3 winners of this race are :\n {response["fare"]}') # see *
#st.caption('Balloons. Hundreds of them...')
st.write('Dataframe pmu breaking') # df, err, func, keras!
#st.write(['st', 'is <', 3]) # see *
st.title('See Horses Races') # Seahorse Races dha ha
#st.header('My header')
#st.subheader('My sub')
