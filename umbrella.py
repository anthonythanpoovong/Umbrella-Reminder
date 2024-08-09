import schedule 
import smtplib    
import requests 
from bs4 import BeautifulSoup 


city = "Hyderabad"
url = "https://www.google.com/search?q=" + "weather" + city 
html = requests.get(url).content 

soup = BeautifulSoup(html, 
                     'html.parser') 
temperature = soup.find( 
  'div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text 
time_sky = soup.find( 
  'div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text 
  
# formatting data 
sky = time_sky.split('\n')[1] 

if sky == "Rainy" or sky == "Rain And Snow" or sky == "Showers" or sky == "Haze" or sky == "Cloudy": 
    smtp_object = smtplib.SMTP('smtp.gmail.com', 587)