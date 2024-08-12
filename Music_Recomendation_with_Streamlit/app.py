import pickle
import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = #<Client-ID key got from spotify develper website>
CLIENT_SECRET = #<Client-Secret key got from spotify develper website>

# Intialising the spotify client
client_credential_manager = SpotifyClientCredentials(
    client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credential_manager)


# Loading the created Music Recommendation Model
st.header('Music Recommendation System')
df = pickle.load(open('recommendation_df.pkl', 'rb'))
similarity = pickle.load(open('recommendation.pkl', 'rb'))

# function to fetch poster or cover of songs


def get_song_poster_url(song_name, singer):

    # Search query to narrow down the search to song and artist
    search_query = f"track:{song_name} artist:{singer}"

    # Search the track
    results = sp.search(q=search_query, type="track")

    # print the photo
    # The data is in JSON file formal
    # CHeck whether result is not empty and there atleast on item corresponsding to the track
    if results and results['tracks']['items']:
        track = results['tracks']['items'][0]  # 1st item accesses
        # 1st URL accessed as it will be of high quality and resolution
        song_poster_url = track['album']['images'][0]['url']
        print(song_poster_url)
        return song_poster_url
    else:
        # returned if song cover not found
        return "https://i.postimg.cc/0QNxYz4V/social.png"


# recommender function
def recommender(song_name):
    idx = df[df['song'] == song_name].index[0]
    # Get the whole row of similar matrix corresponse to the index and Sort it in reverse order based on vector value
    # Also get the index value using enumerate function
    vector_idx = sorted(
        list(enumerate(similarity[idx])), reverse=True, key=lambda x: x[1])
    songs = []
    songs_poster = []

    # Make use of Index value to get the song names of top 10 songs, 0th index is sikped as that is the song itself
    for s_id in vector_idx[:5]:

        # get song poster
        singer = df.iloc[s_id[0]].artist
        print(singer)
        print(df.iloc[s_id[0]].song)  # Get the song name

        # Append song poster
        songs_poster.append(get_song_poster_url(df.iloc[s_id[0]].song, singer))

        # Append song name
        songs.append(df.iloc[s_id[0]].song)

    return songs, songs_poster


# Creating a drobdown select box in streamlit
song_list = df['song'].values
selected_song = st.selectbox("Select a song", song_list)

# Create button and list of songs
if st.button('Search'):
    songs, songs_poster = recommender(selected_song)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(songs[0])
        st.image(songs_poster[0])
    with col2:
        st.text(songs[1])
        st.image(songs_poster[1])
    with col3:
        st.text(songs[2])
        st.image(songs_poster[2])
    with col4:
        st.text(songs[3])
        st.image(songs_poster[3])
    with col5:
        st.text(songs[4])
        st.image(songs_poster[4])
