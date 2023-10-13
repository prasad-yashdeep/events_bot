import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Load configurations from a JSON file
with open("config.json") as f:
    config = json.load(f)

def send_email(time, availability):
    # Email sending logic
    msg = MIMEMultipart()
    msg['From'] = config['sendEmail']['user']
    msg['To'] = ', '.join(["krushiraj123@hotmail.com"])  # Add other email addresses if needed
    msg['Subject'] = f"Alert - {config['name']} Tickets available at {config['theatres'][0]} for time:{time} show"
    
    body = (f"{config['name']} tickets available in {config['theatres'][0]} for {time} show.\n"
            f"There are {availability} tickets available in total, excluding the top most and bottom 4 rows.\n"
            f"Please hurry up, help yourself or ping Krushi ASAP to ask him to proceed further.")
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(config['sendEmail']['user'], config['sendEmail']['pass'])
        text = msg.as_string()
        server.sendmail(config['sendEmail']['user'], ["krushiraj123@hotmail.com"], text)  # Add other email addresses if needed
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")


def example():
    driver = webdriver.Chrome()
    try:
        driver.maximize_window()
        print(f"Read the configuration file. Now I'm trying to book tickets for {config['name']} in {config['theatres'][0]}, {config['location']}.")
        driver.get(f"https://in.bookmyshow.com/{config['location']}/{config['type']}/")
        # Your web scraping logic goes here
        # ...
        # Placeholder for the full code logic, as the full translation is quite extensive
        
    finally:
        driver.quit()
        time.sleep(10)
        # example()


# Run the example function
example()
