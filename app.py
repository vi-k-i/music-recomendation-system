import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify API credentials
CLIENT_ID = "6025496231b84546a58cd6a5e7779038"
CLIENT_SECRET = "826daeba815a4eb3ad06526cbdd99760"

# Initialize the Spotify client
client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Function to get album cover URL from Spotify
def get_song_album_cover_url(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")

    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        return album_cover_url
    else:
        return "https://i.postimg.cc/0QNxYz4V/social.png"

# Function to recommend similar songs
def recommend(song):
    index = music[music['song'] == song].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_music_names = []
    recommended_music_posters = []
    for i in distances[1:6]:
        artist = music.iloc[i[0]].artist
        recommended_music_posters.append(get_song_album_cover_url(music.iloc[i[0]].song, artist))
        recommended_music_names.append(music.iloc[i[0]].song)

    return recommended_music_names, recommended_music_posters

# Streamlit app
st.header('Music Recommender System')

# Load data from pickle files
music = pickle.load(open('df', 'rb'))
similarity = pickle.load(open('similarity', 'rb'))

# Dropdown to select a song
selected_song = st.selectbox("Select a song", music['song'].values)

# Button to trigger recommendations
if st.button('Show Recommendations'):
    recommended_music_names, recommended_music_posters = recommend(selected_song)

    # Display recommendations in columns
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_music_names[0])
        st.image(recommended_music_posters[0], caption=recommended_music_names[0])
    with col2:
        st.text(recommended_music_names[1])
        st.image(recommended_music_posters[1], caption=recommended_music_names[1])
    with col3:
        st.text(recommended_music_names[2])
        st.image(recommended_music_posters[2], caption=recommended_music_names[2])
    with col4:
        st.text(recommended_music_names[3])
        st.image(recommended_music_posters[3], caption=recommended_music_names[3])
    with col5:
        st.text(recommended_music_names[4])
        st.image(recommended_music_posters[4], caption=recommended_music_names[4])

