from flask import Flask, request, render_template
import numpy as np
import pandas as pd
import pickle

# Loading models and dataset
df = pickle.load(open('./venv/recommendation_df.pkl', 'rb'))
model = pickle.load(open('./venv/recommendation.pkl', 'rb'))

# Function for the song recomendation


def recommender(song_name):
    idx = df[df['song'] == song_name].index[0]

    # Get the whole row of similar matrix corresponse to the index and Sort it in reverse order based on vector value
    # Also get the index value using enumerate function
    vector_idx = sorted(
        list(enumerate(model[idx])), reverse=True, key=lambda x: x[1])
    songs = []

    # Make use of Index value to get the song names of top 10 songs, 0th index is sikped as that is the song itself
    for s_id in vector_idx[:21]:
        songs.append(df.iloc[s_id[0]].song)
    return songs


# flask app
app = Flask(__name__)
# Paths


@app.route('/')
# Get the list of songs
def index():
    names = list(df['song'].values)
    return render_template('index.html', name=names)


@app.route('/recom', methods=['POST'])
# Function for recommendation system
def recommended_music():
    user_song = request.form['names']
    rec_songs = recommender(user_song)

    return render_template('index.html', songs=rec_songs)
# Main function


if __name__ == "__main__":
    app.run(debug=True)
