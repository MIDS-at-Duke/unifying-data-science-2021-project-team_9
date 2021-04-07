import pandas as pd 
from pandas import DataFrame
import requests 
from bs4 import BeautifulSoup as bs 
import matplotlib.pyplot as plt 
import datetime 

def scrape_imdb(url):
    
    page = requests.get(url)
    soup = bs(page.content, 'html.parser')
    movie_containers = soup.find_all('div', class_ = 'lister-item mode-advanced')

    # init lists
    titles = []
    year = []
    imdb_rating = []
    num_votes = []
    genre = []
    film_rating = []
    director = []
    lead_actor = []

    # create "vectors"
    for j in range(0, len(movie_containers)):
        print(j)
        
        if movie_containers[j].find('div', class_ = 'ratings-imdb-rating') is not None:
        
            titles.append(movie_containers[j].h3.a.text)
            year.append(movie_containers[j].h3.find('span', 'lister-item-year text-muted unbold').text.replace('(','').replace(')',''))
            imdb_rating.append(float(movie_containers[j].strong.text))
            #metascore_rating.append(int(movie_containers[i].find('span', class_ = 'metascore favorable').text))
            num_votes.append(int(movie_containers[j].find('span', attrs = {'name' : 'nv'}).text.replace(",", "")))
            genre.append(movie_containers[j].find('span', 'genre').contents[0].split(',', 1)[0].replace('\n', '').strip())
            film_rating.append(movie_containers[j].find('p').contents[1].text)
            director.append(movie_containers[j].find_all('p')[2].find('a').text)
            lead_actor.append(movie_containers[j].find_all('p')[2].find_all('a')[1].text)
        

    # convert into dataframe
    movies = pd.DataFrame({
        'titles' : titles,
        'year' : year,
        'imdb_rating' : imdb_rating,
        'num_votes' : num_votes,
        'genre' : genre,
        'film_rating' : film_rating,
        'director' : director,
        'lead_actor' : lead_actor
    })

    #Frame = Frame.append(pd.DataFrame(data = movies), ignore_index=True)
    return movies


url1 = 'https://www.imdb.com/search/title/?release_date=2017-01-01,2017-12-31&sort=boxoffice_gross_us,desc' # pg 1 for 2017 
url2 = 'https://www.imdb.com/search/title/?release_date=2017-01-01,2017-12-31&sort=boxoffice_gross_us,desc&start=51&ref_=adv_nxt' # pg 2 for 2017  
url3 = 'https://www.imdb.com/search/title/?release_date=2017-01-01,2017-12-31&sort=boxoffice_gross_us,desc&start=101&ref_=adv_nxt' 
url4 = 'https://www.imdb.com/search/title/?release_date=2017-01-01,2017-12-31&sort=boxoffice_gross_us,desc&start=151&ref_=adv_nxt' 
url5 = 'https://www.imdb.com/search/title/?release_date=2017-01-01,2017-12-31&sort=boxoffice_gross_us,desc&start=201&ref_=adv_nxt' 
url6 = 'https://www.imdb.com/search/title/?release_date=2017-01-01,2017-12-31&sort=boxoffice_gross_us,desc&start=251&ref_=adv_nxt' 

m1 = scrape_imdb(url1)
m2 = scrape_imdb(url2)
m3 = scrape_imdb(url3)
m4 = scrape_imdb(url4)
m5 = scrape_imdb(url5)
m6 = scrape_imdb(url6)

m_2017 = pd.concat([m1, m2, m3, m4, m5, m6], ignore_index=True)







url1 = 'https://www.imdb.com/search/title/?release_date=2018-01-01,2018-12-31&sort=boxoffice_gross_us,desc' # pg 1 for 2018 
url2 = 'https://www.imdb.com/search/title/?release_date=2018-01-01,2018-12-31&sort=boxoffice_gross_us,desc&start=51&ref_=adv_nxt' # pg 2 for 2018  
url3 = 'https://www.imdb.com/search/title/?release_date=2018-01-01,2018-12-31&sort=boxoffice_gross_us,desc&start=101&ref_=adv_nxt' 
url4 = 'https://www.imdb.com/search/title/?release_date=2018-01-01,2018-12-31&sort=boxoffice_gross_us,desc&start=151&ref_=adv_nxt' 
url5 = 'https://www.imdb.com/search/title/?release_date=2018-01-01,2018-12-31&sort=boxoffice_gross_us,desc&start=201&ref_=adv_nxt' 
url6 = 'https://www.imdb.com/search/title/?release_date=2018-01-01,2018-12-31&sort=boxoffice_gross_us,desc&start=251&ref_=adv_nxt' 

m1 = scrape_imdb(url1)
m2 = scrape_imdb(url2)
m3 = scrape_imdb(url3)
m4 = scrape_imdb(url4)
m5 = scrape_imdb(url5)
m6 = scrape_imdb(url6)

m_2018 = pd.concat([m1, m2, m3, m4, m5, m6], ignore_index=True)



url1 = 'https://www.imdb.com/search/title/?release_date=2019-01-01,2019-12-31&sort=boxoffice_gross_us,desc' # pg 1 for 2019 
url2 = 'https://www.imdb.com/search/title/?release_date=2019-01-01,2019-12-31&sort=boxoffice_gross_us,desc&start=51&ref_=adv_nxt' # pg 2 for 2019  
url3 = 'https://www.imdb.com/search/title/?release_date=2019-01-01,2019-12-31&sort=boxoffice_gross_us,desc&start=101&ref_=adv_nxt' 
url4 = 'https://www.imdb.com/search/title/?release_date=2019-01-01,2019-12-31&sort=boxoffice_gross_us,desc&start=151&ref_=adv_nxt' 
url5 = 'https://www.imdb.com/search/title/?release_date=2019-01-01,2019-12-31&sort=boxoffice_gross_us,desc&start=201&ref_=adv_nxt' 
url6 = 'https://www.imdb.com/search/title/?release_date=2019-01-01,2019-12-31&sort=boxoffice_gross_us,desc&start=251&ref_=adv_nxt' 

m1 = scrape_imdb(url1)
m2 = scrape_imdb(url2)
m3 = scrape_imdb(url3)
m4 = scrape_imdb(url4)
m5 = scrape_imdb(url5)
m6 = scrape_imdb(url6)

m_2019 = pd.concat([m1, m2, m3, m4, m5, m6], ignore_index=True)



url1 = 'https://www.imdb.com/search/title/?release_date=2020-01-01,2020-12-31&sort=boxoffice_gross_us,desc' # pg 1 for 2020 
url2 = 'https://www.imdb.com/search/title/?release_date=2020-01-01,2020-12-31&sort=boxoffice_gross_us,desc&start=51&ref_=adv_nxt' # pg 2 for 2020  
url3 = 'https://www.imdb.com/search/title/?release_date=2020-01-01,2020-12-31&sort=boxoffice_gross_us,desc&start=101&ref_=adv_nxt' 
url4 = 'https://www.imdb.com/search/title/?release_date=2020-01-01,2020-12-31&sort=boxoffice_gross_us,desc&start=151&ref_=adv_nxt' 
url5 = 'https://www.imdb.com/search/title/?release_date=2020-01-01,2020-12-31&sort=boxoffice_gross_us,desc&start=201&ref_=adv_nxt' 
url6 = 'https://www.imdb.com/search/title/?release_date=2020-01-01,2020-12-31&sort=boxoffice_gross_us,desc&start=251&ref_=adv_nxt' 

m1 = scrape_imdb(url1)
m2 = scrape_imdb(url2)
m3 = scrape_imdb(url3)
m4 = scrape_imdb(url4)
m5 = scrape_imdb(url5)
m6 = scrape_imdb(url6)

m_2020 = pd.concat([m1, m2, m3, m4, m5, m6], ignore_index=True)

movies2 = pd.concat([m_2017, m_2018, m_2019, m_2020], ignore_index=True)

# cleaning data
movies2['genre'] = movies2['genre'].str.split(',').str[0]


# write out to folder
movies2.to_csv('C:\\Users\\abhis\\Documents\\Duke University\\IDS 793 Unifying Data Science\\unifying-data-science-2021-project-team_9\\00_data\\imdb_movies.csv', index = False)




######################################################################################################################################################################################################

# soup
url = 'https://www.imdb.com/search/title/?release_date=2019-01-01,2019-12-31&sort=boxoffice_gross_us,desc&start=101&ref_=adv_nxt'
page = requests.get(url)
soup = bs(page.content, 'html.parser')
movie_containers = soup.find_all('div', class_ = 'lister-item mode-advanced')


j = 23

# scraping relevant columns
title = movie_containers[j].h3.a.text
year = movie_containers[j].h3.find('span', 'lister-item-year text-muted unbold').text.replace('(','').replace(')','')
imdb_rating = float(movie_containers[j].strong.text)
num_votes = int(movie_containers[j].find('span', attrs = {'name' : 'nv'}).text.replace(",", ""))
genre = movie_containers[j].find('span', 'genre').contents[0].split(',', 1)[0].replace('\n', '').strip()
#genre = movie_containers[0].find('p').contents[9].text.split(',', 1)[0].replace('\n', '') # issue for some cases

film_rating = movie_containers[j].find('span', 'certificate').contents[1].text
film_rating = movie_containers[j].find('p').contents[1].text
director = movie_containers[j].find_all('p')[2].find('a').text
lead_actor = movie_containers[j].find_all('p')[2].find_all('a')[1].text

# init lists
titles = []
year = []
imdb_rating = []
num_votes = []
genre = []
film_rating = []
director = []
lead_actor = []

# create "vectors"
for i in range(0, len(movie_containers)):
    titles.append(movie_containers[i].h3.a.text)
    year.append(movie_containers[i].h3.find('span', 'lister-item-year text-muted unbold').text.replace('(','').replace(')',''))
    imdb_rating.append(float(movie_containers[i].strong.text))
    #metascore_rating.append(int(movie_containers[i].find('span', class_ = 'metascore favorable').text))
    num_votes.append(int(movie_containers[i].find('span', attrs = {'name' : 'nv'}).text.replace(",", "")))
    genre.append(movie_containers[i].find('p').contents[9].text.split(',', 1)[0].replace('\n', ''))
    film_rating.append(movie_containers[i].find('p').contents[1].text)
    director.append(movie_containers[i].find_all('p')[2].find('a').text)
    lead_actor.append(movie_containers[i].find_all('p')[2].find_all('a')[1].text)
    pass

# convert into dataframe
movies = pd.DataFrame({
    'titles' : titles,
    'year' : year,
    'imdb_rating' : imdb_rating,
    'num_votes' : num_votes,
    'genre' : genre,
    'film_rating' : film_rating,
    'director' : director,
    'lead_actor' : lead_actor
})



    
def ss(year, i):
    url = 'https://www.imdb.com/search/title/?release_date=%s-01-01,%s-12-31&sort=boxoffice_gross_us,desc&start=%s&ref_=adv_prv' % (year, year, 51 + (50 * (i - 2)))
    return url

ss(2017,2)
51 + (50 * (i - 2))    
