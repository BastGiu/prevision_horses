import pandas as pd
import streamlit as st
from fast import predict_winner
import streamlit as st
import requests

url = 'https://pmu_breaking.ai/'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')
'''
# Pon.A.I (aka See Horses Races)
'''
# id,comp,jour,hippo,numcourse,cl,dist,partant,typec,cheque,numero,cheval,sexe,age,cotedirect,coteprob,recence,ecurie,distpoids,ecar,redkm,redkmInt,corde,defoeil,defoeilPrec,recul,gains,musiquept,musiqueche,m1,m2,m3,m4,m5,m6,jockey,musiquejoc,montesdujockeyjour,couruejockeyjour,victoirejockeyjour,entraineur,musiqueent,monteentraineurjour,courueentraineurjour,victoireentraineurjour,coursescheval,victoirescheval,placescheval,coursesentraineur,victoiresentraineur,placeentraineur,coursesjockey,victoiresjockey,placejockey,dernierhippo,dernierealloc,derniernbpartants,dernieredist,derniereplace,dernierecote,dernierJoc,dernierEnt,dernierProp,dernierRedKm,proprietaire,nbcoursepropjour,poidmont,pourcVictJock,pourcPlaceJock,pourcVictCheval,pourcPlaceCheval,pourcVictEnt,pourcPlaceEnt,pourcVictEntHippo,pourcVictJockHippo,pourcPlaceEntHippo,pourcPlaceJockHippo,pourcVictChevalHippo,pourcPlaceChevalHippo,nbrCourseJockHippo,nbrCourseEntHippo,nbrCourseChevalHippo,nbCourseCouple,nbVictCouple,nbPlaceCouple,TxVictCouple,TxPlaceCouple,nbCourseCoupleHippo,nbVictCoupleHippo,nbPlaceCoupleHippo,TxVictCoupleHippo,TxPlaceCoupleHippo,pere,mere,peremere,commen,gainsCarriere,gainsVictoires,gainsPlace,gainsAnneeEnCours,gainsAnneePrecedente,jumentPleine,engagement,handicapDistance,handicapPoids,indicateurInedit,tempstot,vha,recordG,recordGint,txreclam,dernierTxreclam,createdat,updatedat,rangTxVictJock,rangTxVictCheval,rangTxVictEnt,rangTxPlaceJock,rangTxPlaceCheval,rangTxPlaceEnt,rangRecordG,appetTerrain,idChe,idJockey,idEntraineur,defFirstTime,oeilFirstTime,estSupplemente,oeil,devise,dernierOeil,coat,country,id.1,jour.1,heure,hippo.1,reun,prix,prixnom,meteo,typec.1,partant.1,handi,reclam,dist.1,groupe,sex,corde.1,age.1,autos,cheque.1,europ,quinte,natpis,amat,courseabc,pistegp,arriv,lice,temperature,forceVent,directionVent,nebulositeLibelleCourt,condi,url,tempscourse,updatedAt,createdAt,devise.1,ref

data_url = 'https://raw.githubusercontent.com/BastGiu/prevision_horses/master/data/2022-12-04_df_pred.csv'
def display_dataframe(data_url):
    df = pd.read_csv(data_url)
    return df

df = display_dataframe(data_url=data_url)
st.dataframe(df)
