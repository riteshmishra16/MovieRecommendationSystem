import numpy as np
import pandas as pd
import ast
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle
from nltk.stem.porter import PorterStemmer

# Load the datasets
movies = pd.read_csv('tmdb_5000_movies.csv')
credits = pd.read_csv('tmdb_5000_credits.csv')

print(movies.head())
print(credits.head())

print(movies.shape)
print(credits.shape)

movies = movies.merge(credits, on = 'title')
print(movies.shape)
print(movies.columns)

movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords' , 'cast' , 'crew']]
print(movies.head())
print(movies.isnull().sum())
movies.dropna(inplace=True)
print(movies.isnull().sum())
print(movies.duplicated().sum())

def convert(obj):
    L = []
    for i in ast.literal_eval(obj):
        L.append(i['name'])
    return L

movies['genres'] = movies['genres'].apply(convert)
print(movies['genres'].head())

movies['keywords'] = movies['keywords'].apply(convert)

def convert3(text):
    L = []
    counter = 0

    for i in ast.literal_eval(text):
        if counter != 3:
            L.append(i['name'])
            counter += 1
        else:
            break

    return L

movies['cast'] = movies['cast'].apply(convert3)
print(movies['cast'].head())

def fetch_director(text):
    L = []

    for i in ast.literal_eval(text):
        if i['job'] == 'Director':
            L.append(i['name'])
            break

    return L
movies['crew'] = movies['crew'].apply(fetch_director)
print(movies['crew'].head())

movies['overview'] = movies['overview'].apply(lambda x: x.split())
print(movies['overview'].head())

def collapse(L):
    L1 = []

    for i in L:
        L1.append(i.replace(" ", ""))

    return L1
movies['genres'] = movies['genres'].apply(collapse)
movies['keywords'] = movies['keywords'].apply(collapse)
movies['cast'] = movies['cast'].apply(collapse)
movies['crew'] = movies['crew'].apply(collapse)
print(movies['cast'].head())

movies['tags'] = movies['overview'] + \
                 movies['genres'] + \
                 movies['keywords'] + \
                 movies['cast'] + \
                 movies['crew']
print(movies['tags'].head())

new_df = movies[['movie_id', 'title', 'tags']]
print(new_df.head())

new_df['tags'] = new_df['tags'].apply(lambda x: " ".join(x))
print(new_df['tags'].head())
new_df['tags'] = new_df['tags'].apply(lambda x: x.lower())
print(new_df.head())

ps = PorterStemmer()

def stem(text):
    y = []

    for i in text.split():
        y.append(ps.stem(i))

    return " ".join(y)

new_df['tags'] = new_df['tags'].apply(stem)

cv = CountVectorizer(max_features=5000, stop_words='english')
vectors = cv.fit_transform(new_df['tags']).toarray()
print(vectors.shape)
similarity = cosine_similarity(vectors)
print(similarity.shape)

def recommend(movie):

    movie_index = new_df[
    new_df['title'].str.lower() == movie.lower()
        ].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    for i in movies_list:
        print(new_df.iloc[i[0]].title)

recommend("Batman Begins")

pickle.dump(new_df, open("movies.pkl", "wb"))
pickle.dump(similarity, open("similarity.pkl", "wb"))

 