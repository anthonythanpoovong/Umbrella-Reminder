import schedule 
import smtplib    
import requests 
from bs4 import BeautifulSoup 


city = "Hyderabad"
url = "https://www.google.com/search?q=" + "weather" + city 
html = requests.get(url).content 