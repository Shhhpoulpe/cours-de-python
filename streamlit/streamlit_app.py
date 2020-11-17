import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk

video_games_URL = (
    "streamlit/csv/Video_Games_Sales.csv"
)

netflix_URL = (
    "streamlit/csv/netflix_titles.csv"
)

@st.cache(persist=True)
def load_video_games(nrows):
    data = pd.read_csv(video_games_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    return data

@st.cache(persist=True)
def load_netflix(nrows):
    data = pd.read_csv(netflix_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    return data

st.title("Découverte de streamlib")
st.title("Affichage des tableaux")

nb_video_games = st.number_input('Nombre de ligne a afficher pour les jeux',value=5,step=1)
data_video_games = load_video_games(nb_video_games)
nb_video_games

'video games', data_video_games

nb_netflix = st.number_input('Nombre de ligne a afficher pour netflix',value=5,step=1)
data_netflix = load_netflix(nb_netflix)
nb_netflix

'netflix', data_netflix

st.title("Affichage des colonnes")

data_video_games.columns

st.title("Affichage des types des colonnes et des selections")

list_result = st.selectbox(
    'test list',
    (data_video_games.columns))

st.write('Vous avez choisi:', list_result, ' qui est de type', data_video_games[list_result].dtype)

st.title("Affichage de la shape du dataset")

data_video_games.shape