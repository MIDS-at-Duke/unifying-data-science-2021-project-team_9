import pandas as pd 

imdb = pd.read_csv('C:/Users/abhis/Documents/Duke University/IDS 793 Unifying Data Science/unifying-data-science-2021-project-team_9/00_data/imdb_movies.csv')
mojo = pd.read_csv('C:/Users/abhis/Documents/Duke University/IDS 793 Unifying Data Science/unifying-data-science-2021-project-team_9/00_data/mojo_movies.csv')
actor = pd.read_csv('C:/Users/abhis/Documents/Duke University/IDS 793 Unifying Data Science/unifying-data-science-2021-project-team_9/00_data/all_poc_actors_actresses.csv')


movie_data = imdb.merge(mojo )