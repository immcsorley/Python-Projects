Weimport bs4
from bs4 import BeautifulSoup
import requests
import time


#gets time, temperature, and sky of city input from google search
def weather (city):
    url = "https://www.google.com/search?q="+"weather"+city
    response = requests.get(url)
    html_doc = response.text
    soup = BeautifulSoup(html_doc, "lxml")
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    info = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    data = info.split('\n')
    time = data[0]
    sky = data[1]
    
    print("\nTime:", time, )
    print("Temperature is currently ", temp,)
    print("Sky Description: ", sky, '\n')

#gets air quality data of city input  from wunderground
def airquality(city): 
   url='https://www.wunderground.com/health/us/ia/'+city 
   request_result = requests.get( url )
   soup = bs4.BeautifulSoup( request_result.text
						, "html.parser" )
   AQI = soup.find( "div" , class_='aqi-value' ).text
   status = soup.find( "div" , class_='aqi-type' ).text
   time.sleep(1)
   print('Air Quality:', AQI)
   print('Live AQI Index: ', status, 'Air Quality\n')

# Gets population of city input from google
def city_population (city):
    url = 'https://www.google.com/search?q='+'population'+city
    response = requests.get(url)
    html_doc = response.text
    soup = BeautifulSoup(html_doc, "html.parser")
    population = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    print('Population of', city, ':', population)

    
# gets average age of city input from google search
def average_age (city):
    url = "https://www.google.com/search?q="+"average age in "+city
    response = requests.get(url)
    html_doc = response.text
    soup = BeautifulSoup(html_doc, "lxml")
    avg_age = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    time.sleep(1)
    print('\nAverage age in', city, ':' , avg_age)
    


