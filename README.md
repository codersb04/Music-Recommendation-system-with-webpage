# Music-Recommendation-system-with-webpage

This repository contains files to create a Music recommendation system along with a webpage view. I create it in 2 ways using Flask and Streamlit(Both Included in this repo)

Language/ Tools - Python, Jupyter notebook, Visual Studio code, HTML

Dataset: Spotify Million Song Dataset, https://www.kaggle.com/datasets/notshrirang/spotify-million-song-dataset

## Recommendation System
### Types of Recomendation system
1. Popularity(Formula Based)
2. Content Based (Tags like comedy , thriller, love, etc,.)
3. Collaborative filtering (Based on users similarity)
4. Hybrid (Collection of all the above 3)</br>

We are going to develop using Content Based
### Steps involved
1. Data collection and preparation: Load the data, Take a sample of 5000 data out of 57650, remove the link column.
2. Text Processing: Convert all the alphabets to lower case in the 'Text' column,Replace all the non alphabetic, non digits and new line(\n) to empty space.
3. Tokenization:
   - import nltk library and PorterStemmer from nltk(Natural Language Tool kit)
   - Divide the text into small tokens using word_tokenize from nltk. Example, "This is a great movie" will become ["This","is","a","great","movie"]
   -  Convert all the words to it's root word. Example, the words Recomend, Recommendation, Recomending will be reduced to recommend
4. Vectorization:
   - Load the library TfidfVectorizer and cosine_similarity from sklearn
   - Get the tfidf value
     - tf: term frequency = word count in the document/ total words in sentence 
     - idf: Inverse Document frequency =  Total document/ Word count in doucumnet
     - tfidf = Tf* Idf
   - Create the cosine similarity Matrix, Consine similarity get the Angle between the two vetors. The matrix would result in 5000 by 5000 matrix each containing the value of angle between the two song vectors.
5. Recommendation system:
   - Get the index of the song based on song name
   - Get the whole row of similar matrix corresponse to the index and Sort it in reverse order based on vector value and also get the index value using enumerate function
   - Make use of Index value to get the song names of top 10 songs, 0th index is sikped as that is the song itself
6. Store the created model and dataframe using pickle

## Webpage using Flask
### Pre-steps:
- Create an folder in the desired location, open that in VS Code
- Created an conda environment using command "conda create -p venv python==3.11 -y"
- Activate the environment with command conda activate "C:\Users<user-name>\<Folder-Name>\venv"
- install flask library to the environment
- Load the dataframe and create model using pickle library
- Paste the same recommender function of the model created
- Create 2 more functions one for getting the list of songs and one for getting the recommeded songs and return the index templates with name of the songs as parameter
- Putting debug = True will automatically reload the page after every update
- Create the index.html page:
  - Got the pre coded format from Bootstrap, [Include Bootstrap’s CSS and JS](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
  - Use 'jinja' feature in flask to access varibles or any type of data in html page using double curly brackets({{}}) and for printing many songs it can be used as<br> {% for i in name %}<br>
            {{i}}</br>
            {% endfor %}
   - Recommended music is printed in the form of card, and code is used from same Bootstrap website's, [Example Code](https://getbootstrap.com/docs/5.3/components/card/) and songs passed through the 'jinja' feature.
- File can be execute by typing the command "python app.py" on the terminal, it will give us an URL for the webpage.
 
## Webpage using Streamlit
- the first 3 steps are similar to above one
- install spotipy and streamlit
- Get the Client ID and Client secret key by creating an account on [Spotify for developer](https://developer.spotify.com/) and create an random app.
- Intialise the spotify client
- Load the created model and dataframe
- Create a function to get the URL of album cover
  - Search query to narrow down the search to song and artist and search the track
  - All the data in spotify is stored in JSON formal
  - Run and if Else code else would print a spotify logo if image not found, for if Check whether result is not empty and there atleast on item corresponsding to the track. 1st item is access and 1st image is accessed in that as it would of high quality. Print the poster
- Recommeder function would be almost same, except we will be accessing our artist name(Which is used to extract the album cover URL) along with song and returning both song and artist name
- Create a selectbox using streamlit and search button
- extract the song and poster
- Created 5 column each containing recommended songs name with poster
- File can be excuted using the command "Streamlit run app.py" on the terminal
## Troubleshooting 
- The major proportion faced at the beginning would be package installation and there compatability with each other.The best way to resolve is to create an environment with suitable python version and corresponding desired package.
- Chrome, Edge or whichever browser is being used should be updated to avoid any unexpected errors.
- Naming convention shoulf be proper, when passing the values from one page to another in case of Flask. double check the Jinja feature names.
- One more issue which I faced was while working on Streamlit, both Streamlit and Spotipy was giving Pylance error. Streamlit error was gone when I restarted my VS code but Spotipy error persit and try to Unistall and install Spotipy, it installed but keep on giving the error of 'not found', then when I installed Spotipy through Anaconda prompt it worked for me.

## Future work
- Work on bigger dataset and training the model with more features.
- Develop a better webpage</br></br></br>

References:
1. Music Recommendation System | AI-Driven Songs Recommendations | Machine Learning Project| Urdu Hindi, Artificial Intelligence, https://www.youtube.com/watch?v=gb7EzyuNSxI
2. Complete Python Flask Tutorial For Data Science Projects In Hindi, Krish Naik Hindi, https://www.youtube.com/watch?v=KF-rDqQfqz0
3. Music Recommender System Using Python, KNOWLEDGE DOCTOR, https://www.youtube.com/watch?v=jm9JamrbSv8&t=2252s
4. Spotipy, https://spotipy.readthedocs.io/en/2.24.0/

