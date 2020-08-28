import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
movies=pd.read_csv('Data/movies.csv')
ratings=pd.read_csv('Data/ratings.csv')

genres=[]
for genre in movies.genres:
    x=genre.split('|')
    for i in x:
         if i not in genres:
            genres.append(str(i))

movie_titles=[]

for title in movies.title:
    movie_titles.append(str(title).lower())


genres=str(genres)   
mtitles=str(movie_titles)
cv=TfidfVectorizer()
tfidf_matrix=cv.fit_transform(movies['genres'])
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
indices=pd.Series(movies.index,index=movies['title'])
titles=movies['title']
def recommendations(title):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]
    movie_indices = [i[0] for i in sim_scores]
    ser = titles.iloc[movie_indices]
    mov = ser.values.tolist()
    return mov 