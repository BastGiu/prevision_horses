import streamlit as st
from fast import predict_winner

url = 'https://pmu_breaking.ai/'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')
import streamlit as st
'''
# Pon.A.I (aka See Horses Races)
'''
import requests

# id,comp,jour,hippo,numcourse,cl,dist,partant,typec,cheque,numero,cheval,sexe,age,cotedirect,coteprob,recence,ecurie,distpoids,ecar,redkm,redkmInt,corde,defoeil,defoeilPrec,recul,gains,musiquept,musiqueche,m1,m2,m3,m4,m5,m6,jockey,musiquejoc,montesdujockeyjour,couruejockeyjour,victoirejockeyjour,entraineur,musiqueent,monteentraineurjour,courueentraineurjour,victoireentraineurjour,coursescheval,victoirescheval,placescheval,coursesentraineur,victoiresentraineur,placeentraineur,coursesjockey,victoiresjockey,placejockey,dernierhippo,dernierealloc,derniernbpartants,dernieredist,derniereplace,dernierecote,dernierJoc,dernierEnt,dernierProp,dernierRedKm,proprietaire,nbcoursepropjour,poidmont,pourcVictJock,pourcPlaceJock,pourcVictCheval,pourcPlaceCheval,pourcVictEnt,pourcPlaceEnt,pourcVictEntHippo,pourcVictJockHippo,pourcPlaceEntHippo,pourcPlaceJockHippo,pourcVictChevalHippo,pourcPlaceChevalHippo,nbrCourseJockHippo,nbrCourseEntHippo,nbrCourseChevalHippo,nbCourseCouple,nbVictCouple,nbPlaceCouple,TxVictCouple,TxPlaceCouple,nbCourseCoupleHippo,nbVictCoupleHippo,nbPlaceCoupleHippo,TxVictCoupleHippo,TxPlaceCoupleHippo,pere,mere,peremere,commen,gainsCarriere,gainsVictoires,gainsPlace,gainsAnneeEnCours,gainsAnneePrecedente,jumentPleine,engagement,handicapDistance,handicapPoids,indicateurInedit,tempstot,vha,recordG,recordGint,txreclam,dernierTxreclam,createdat,updatedat,rangTxVictJock,rangTxVictCheval,rangTxVictEnt,rangTxPlaceJock,rangTxPlaceCheval,rangTxPlaceEnt,rangRecordG,appetTerrain,idChe,idJockey,idEntraineur,defFirstTime,oeilFirstTime,estSupplemente,oeil,devise,dernierOeil,coat,country,id.1,jour.1,heure,hippo.1,reun,prix,prixnom,meteo,typec.1,partant.1,handi,reclam,dist.1,groupe,sex,corde.1,age.1,autos,cheque.1,europ,quinte,natpis,amat,courseabc,pistegp,arriv,lice,temperature,forceVent,directionVent,nebulositeLibelleCourt,condi,url,tempscourse,updatedAt,createdAt,devise.1,ref
st.markdown('''Take your better bets ''')
hippo = st.text_input('Hippodrome')
exhibit = st.text_input('Prix')
horse_name = st.text_input('Nom du cheval / Horse name')
horse_number = st.number_input('Numero du cheval / Horse number')
date = st.date_input('Date')
time = st.time_input('Time')
proba_pl = st.number_input('Proba')
df = predict_winner()
st.dataframe(df)

params = {
    'hippo' : str(hippo),
    'prix': str(exhibit),
    'Horse Name': str(horse_name),
    'numero': int(horse_number),
    'jour': str(date),
    'heure': str(time),
    'proba pl': int(proba_pl),
}


BASE_URI = "https://pmu_breaking.ai/predict"
response = requests.get(BASE_URI, params=params).json()
taxiFareApiUrl = 'https://pmu_breaking.streamlit.app/predict'

st.text('Fixed width text')
st.markdown(f'The first 3 winners of this race are :\n {response["fare"]}') # see *
#st.caption('Balloons. Hundreds of them...')
st.write('Dataframe pmu breaking') # df, err, func, keras!
#st.write(['st', 'is <', 3]) # see *
st.title('See Horses Races') # Seahorse Races dha ha
#st.header('My header')
#st.subheader('My sub')
