            # music-recomendation-system
This project builds a song recommender system using song lyrics. The primary steps involve data cleaning, preprocessing, and generating recommendations based on the cosine similarity of TF-IDF vectors of the song lyrics.

              # Table of Contents

1.Introduction
2.Data
3.Preprocessing
4.Model
5.Recommender Function
6.Usage
7.Files
8.Dependencies

              # Introduction

The goal of this project is to recommend songs based on their lyrics. We use Natural Language Processing (NLP) techniques to preprocess the lyrics and calculate the similarity between songs.

            # Data
The dataset used in this project is spotify_millsongdata.csv, which contains the following columns:

artist: Name of the artist.
song: Name of the song.
link: Link to the song lyrics (not used in the final model).
text: Lyrics of the song.

        # Preprocessing

1.Sampling and Resetting Index:
#We sample 5000 entries from the dataset and drop the link column.
df = df.sample(5000).drop('link', axis=1).reset_index(drop=True) 

2.Text Cleaning:
#Convert lyrics to lowercase.
#Remove unwanted characters and new lines.
df['text'] = df['text'].str.lower().replace(r'^/w/s', ' ').replace(r'/n', ' ', regex=True)

3.Tokenization and Stemming:
#Tokenize the lyrics and apply stemming to reduce words to their root form.
import nltk
from nltk.stem import PorterStemmer
nltk.download('punkt')
stemmer = PorterStemmer()

def token(txt):
    token = nltk.word_tokenize(txt)
    a = [stemmer.stem(w) for w in token]
    return " ".join(a)

              # Model
#We use TF-IDF Vectorizer to convert lyrics into numerical vectors and calculate cosine similarity between these vectors.
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

tfidf = TfidfVectorizer(analyzer='word', stop_words='english')
matrix = tfidf.fit_transform(df['text'])
similer = cosine_similarity(matrix)

             # Recommender Function
The recommender function takes a song name as input and returns a list of top 20 recommended songs based on cosine similarity.

def recommender(song_name):
    idx = df[df['song'] == song_name].index[0]
    distance = sorted(list(enumerate(similer[idx])), reverse=True, key=lambda x: x[1])
    song = [df.iloc[s_id[0]].song for s_id in distance[1:21]]
    return song

       # Usage
To get song recommendations, use the recommender function with the desired song name.
recommender("song name")

      # Files
spotify_millsongdata.csv: Original dataset.
similarity: Pickle file containing the cosine similarity matrix.
df: Pickle file containing the processed DataFrame.

     # Dependencies
pandas
numpy
nltk
scikit-learn
pickle 

     # Saving and Loading Model
#The similarity matrix and DataFrame are saved using pickle.
import pickle
pickle.dump(similer, open("similarity", "wb"))
pickle.dump(df, open("df", "wb"))

#To load these files later in app.py:
similarity = pickle.load(open("similarity", "rb"))
df = pickle.load(open("df", "rb"))













