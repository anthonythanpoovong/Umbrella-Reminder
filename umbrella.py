import schedule
import smtplib
import requests
from bs4 import BeautifulSoup


def umbrellaReminder():
    city = "Toronto"
    
    # Creating the URL and making a request
    url = f"https://www.google.com/search?q=weather+{city}"
    html = requests.get(url).content
    
    # Parsing the raw data using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    temperature = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    time_sky = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    
    # Extracting sky condition from the parsed data
    sky = time_sky.split('\n')[1]

    # Checking weather conditions
    if sky in ["Rainy", "Rain And Snow", "Showers", "Haze", "Cloudy"]:
        # Setting up the SMTP server
        smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
        
        # Start TLS for security
        smtp_object.starttls()
        
        # Authentication (replace with your actual email and password)
        smtp_object.login("athanpoovongtesting@gmail.com", "athanpoovong123")
        
        # Email subject and body
        subject = "GeeksforGeeks Umbrella Reminder"
        body = f"""Take an umbrella before leaving the house.
Weather condition for today is {sky} and temperature is {temperature} in {city}."""
        
        # Formatting the message
        msg = f"Subject:{subject}\n\n{body}\n\nRegards,\nGeeksforGeeks".encode('utf-8')
        
        # Sending the email (replace with actual from and to emails)
        smtp_object.sendmail("athanpoovongtesting@gmail.com", "thanpoovong84@gmail.com", msg)
        
        # Terminating the SMTP session
        smtp_object.quit()
        
        print("Email Sent!")


# Schedule the umbrella reminder function to run every day at 06:00 AM
schedule.every().day.at("06:00").do(umbrellaReminder)

# Keep the script running
while True:
    schedule.run_pending()
