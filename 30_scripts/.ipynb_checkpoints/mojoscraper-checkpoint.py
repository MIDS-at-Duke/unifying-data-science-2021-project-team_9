# loading libraries
import pandas as pd 
from pandas import DataFrame
import requests 
from bs4 import BeautifulSoup as bs 
import matplotlib.pyplot as plt 
import datetime 

# dictonary of months 
months = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', 
          'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}

# cleans date related columns
def date_clean(x, year):
    year = str(year)
    month = x.str[0:3].map(months).astype('str')
    day = '01'
    date = year + '-' + month + '-' + day
    date = pd.to_datetime(date, format='%Y/%m/%d', errors='coerce')
    return date
    pass

# scrapes mojo website top yearly domestic movies 
def scrape_mojo(start_year, end_year):
    
    # init final frame
    Frame = pd.DataFrame()
    
    for i in range(start_year, end_year + 1):
        # url of the domestic box office for a given year
        url = "https://www.boxofficemojo.com/year/%s/?grossesOption=totalGrosses&sort=rank&sortDir=asc" % i
        page = requests.get(url)
        soup = bs(page.content, 'html.parser')
        
        # scraping relevant columns
        titles = soup.find_all('td', class_= 'a-text-left mojo-field-type-release mojo-cell-wide')
        gross = soup.find_all('td', class_= 'a-text-right mojo-field-type-money mojo-estimatable')
        max_theaters = soup.find_all('td', class_= 'a-text-right mojo-field-type-positive_integer')
        opening_gross = soup.find_all('td', class_= 'a-text-right mojo-field-type-money')
        opening_weekend_perc = soup.find_all('td', class_= 'a-text-right mojo-field-type-percent')
        opening_theaters = soup.find_all('td', class_= 'a-text-right mojo-field-type-positive_integer')
        open_date = soup.find_all('td', class_= 'a-text-left mojo-field-type-date a-nowrap')
        close_date = soup.find_all('td', class_= 'a-text-left mojo-field-type-date a-nowrap')
        #distributor = soup.find_all('td', class_= 'a-text-left mojo-field-type-studio')
        
        # init lists
        all_titles = []
        all_gross = []
        all_max_theaters = []
        all_oppening_gross = []
        all_opening_weekend_perc = []
        all_opening_theaters = []
        all_open_date = []
        all_close_date = []
        #all_distributors = []
        
        # create "vectors"
        for j in range(0,len(titles)):
            all_titles.append(titles[j].select('a')[0].string)
            all_gross.append(gross[j].string)
            all_max_theaters.append(max_theaters[j].string)
            all_oppening_gross.append(opening_gross[j].string)
            all_opening_weekend_perc.append(opening_weekend_perc[j].string)
            all_opening_theaters.append(opening_theaters[j].string)
            all_open_date.append(open_date[j].string)
            all_close_date.append(close_date[j].string)
            #distributor[i].select()
            pass
        
        # combine in to df 
        movies = pd.DataFrame({
            'titles': all_titles,
            'gross' : all_gross,
            'max_theaters' : all_max_theaters,
            'opening_gross' : all_oppening_gross,
            'opening_weekend_perc' : all_opening_weekend_perc,
            'opening_theaters' : all_opening_theaters,
            'open_date' : all_open_date,
            'close_date' : all_close_date,
            # add dist later
            })
        
        # cleaning df
        movies['gross'] = movies['gross'].replace({'\$':'', ',':''}, regex = True).astype(int)
        movies['max_theaters'] = movies['max_theaters'].replace({',':'', '-':'0'}, regex = True).astype(int)
        movies['opening_gross'] = movies['opening_gross'].replace({'\$':'', ',':'', '-':'0'}, regex = True).astype(int) 
        movies['opening_weekend_perc'] = movies['opening_weekend_perc'].replace({'-':'0'}).str.strip('%')
        movies['opening_theaters'] = movies['opening_theaters'].replace({',' : '', '-' : '0'}, regex = True).astype(int)
        movies['open_date'] = date_clean(movies['open_date'], i)
        movies['close_date'] = date_clean(movies['close_date'], i)
        
        Frame = Frame.append(pd.DataFrame(data = movies), ignore_index=True)
        
    return Frame


# run this line of code, put in range of years
movies = scrape_mojo(2017, 2020)    



# write out to folder
movies.to_csv(r'..\00_data\mojo_movies.csv', index = False)







### prototype code
#########################################################################################################################


# # url of the domestic box office for a given year
# url = "https://www.boxofficemojo.com/year/2018/?grossesOption=totalGrosses&sort=rank&sortDir=asc"
# page = requests.get(url)
# soup = bs(page.content, 'html.parser')

# # scraping relevant columns
# titles = soup.find_all('td', class_= 'a-text-left mojo-field-type-release mojo-cell-wide')
# gross = soup.find_all('td', class_= 'a-text-right mojo-field-type-money mojo-estimatable')
# max_theaters = soup.find_all('td', class_= 'a-text-right mojo-field-type-positive_integer')
# opening_gross = soup.find_all('td', class_= 'a-text-right mojo-field-type-money')
# opening_weekend_perc = soup.find_all('td', class_= 'a-text-right mojo-field-type-percent')
# opening_theaters = soup.find_all('td', class_= 'a-text-right mojo-field-type-positive_integer')
# open_date = soup.find_all('td', class_= 'a-text-left mojo-field-type-date a-nowrap')
# close_date = soup.find_all('td', class_= 'a-text-left mojo-field-type-date a-nowrap')
# #distributor = soup.find_all('td', class_= 'a-text-left mojo-field-type-studio')

# # init lists
# all_titles = []
# all_gross = []
# all_max_theaters = []
# all_oppening_gross = []
# all_opening_weekend_perc = []
# all_opening_theaters = []
# all_open_date = []
# all_close_date = []
# all_distributors = []

# # create "vectors"
# for i in range(0,len(titles)):
#     all_titles.append(titles[i].select('a')[0].string)
#     all_gross.append(gross[i].string)
#     all_max_theaters.append(max_theaters[i].string)
#     all_oppening_gross.append(opening_gross[i].string)
#     all_opening_weekend_perc.append(opening_weekend_perc[i].string)
#     all_opening_theaters.append(opening_theaters[i].string)
#     all_open_date.append(open_date[i].string)
#     all_close_date.append(close_date[i].string)
#     #distributor[i].select()
#     pass

# # combine in to df 
# movies = pd.DataFrame({
#     'titles': all_titles,
#     'gross' : all_gross,
#     'max_theaters' : all_max_theaters,
#     'opening_gross' : all_oppening_gross,
#     'opening_weekend_perc' : all_opening_weekend_perc,
#     'opening_theaters' : all_opening_theaters,
#     'open_date' : all_open_date,
#     'close_date' : all_close_date,
#     # add dist later
# })

# months = {'Jan':'01', 'Feb':'02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', 
#           'Jul':'07', 'Aug':'08', 'Sep':'09', 'Oct':'10', 'Nov':'11', 'Dec':'12'}

# def date_clean(x, year):
#     year = str(year)
#     month = x.str[0:3].map(months).astype('str')
#     day = '01'
#     date = year + '-' + month + '-' + day
#     date = pd.to_datetime(date, format='%Y/%m/%d', errors='coerce')
#     return date
#     pass
    
# # cleaning df
# movies['gross'] = movies['gross'].replace({'\$':'', ',':''}, regex = True).astype(int)
# movies['max_theaters'] = movies['max_theaters'].replace({',':'', '-':'0'}, regex = True).astype(int)
# movies['opening_gross'] = movies['opening_gross'].replace({'\$':'', ',':'', '-':'0'}, regex = True).astype(int) 
# movies['opening_weekend_perc'] = movies['opening_weekend_perc'].replace({'-':'0'}).str.strip('%').astype(float)
# movies['opening_theaters'] = movies['opening_theaters'].replace({',' : '', '-' : '0'}, regex = True).astype(int)
# movies['open_date'] = date_clean(movies['open_date'])
# movies['close_date'] = date_clean(movies['close_date'])


