library(tidyverse)
library(tidyr)

# load data
imdb = read.csv('C:/Users/abhis/Documents/Duke University/IDS 793 Unifying Data Science/unifying-data-science-2021-project-team_9/00_data/imdb_movies.csv')
mojo = read.csv('C:/Users/abhis/Documents/Duke University/IDS 793 Unifying Data Science/unifying-data-science-2021-project-team_9/00_data/mojo_movies.csv')
actor = read.csv('C:/Users/abhis/Documents/Duke University/IDS 793 Unifying Data Science/unifying-data-science-2021-project-team_9/00_data/all_poc_actor_actress.csv',
                    encoding='latin-1')
more_imdb = read.csv('C:/Users/abhis/Documents/Duke University/IDS 793 Unifying Data Science/unifying-data-science-2021-project-team_9/00_data/imdb_movies.csv')

# clean more_imdb
more_imdb$year = extract_numeric(more_imdb$year)
more_imdb$year = substr(more_imdb$year, start = 1, stop = 4)

# clean imdb
imdb$year = extract_numeric(imdb$year)
imdb$year = substr(imdb$year, start = 1, stop = 4)
imdb = imdb %>% filter(year >= 2017)

# rbind imdb files
imdb_full = rbind(imdb, more_imdb)

# remove duplicates
imdb_full = imdb_full %>% distinct(titles, .keep_all = T)

# left join tables
movies = left_join(imdb_full, mojo, by = "titles")
movies = left_join(movies, actor, by = c("lead_actor" = "Name"))

# assign race
movies$Race = ifelse(is.na(movies$Race) == T, "Not POC", movies$Race)
movies$Race_Specific = ifelse(is.na(movies$Race_Specific) == T, "White", movies$Race_Specific)

# remove duplicates
movies = movies %>% distinct(titles, .keep_all = T)

# write out
write.csv(movies, file = "C:/Users/abhis/Documents/Duke University/IDS 793 Unifying Data Science/unifying-data-science-2021-project-team_9/00_data/full_data.csv", row.names = F)



