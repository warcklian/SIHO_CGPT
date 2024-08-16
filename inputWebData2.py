# cspell: disable
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the Chrome options to connect to the existing Chrome instance
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

# Path to the ChromeDriver executable
service = Service(executable_path="./chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL of the webpage where the data will be entered
url = "file:///D:/Code/Ejemplo_selenium_CGPT/test_form.html"
driver.get(url)

# Read the Excel file
df = pd.read_excel('data.xlsx', engine='openpyxl')

# Create a WebDriverWait instance
wait = WebDriverWait(driver, 10)

# Iterate over each row of the DataFrame and fill out the form
for index, row in df.iterrows():
    # Wait for the form fields to be present
    wait.until(EC.presence_of_element_located((By.NAME, "first_name")))

    # Fill out the form fields with data from the Excel file
    driver.find_element(By.NAME, "first_name").clear()
    driver.find_element(By.NAME, "first_name").send_keys(row['First Name'])
    
    driver.find_element(By.NAME, "last_name_paternal").clear()
    driver.find_element(By.NAME, "last_name_paternal").send_keys(row['Last Name (Paternal)'])
    
    driver.find_element(By.NAME, "last_name_maternal").clear()
    driver.find_element(By.NAME, "last_name_maternal").send_keys(row['Last Name (Maternal)'])
    
    driver.find_element(By.NAME, "rfc").clear()
    driver.find_element(By.NAME, "rfc").send_keys(row['RFC'])
    
    driver.find_element(By.NAME, "address").clear()
    driver.find_element(By.NAME, "address").send_keys(row['Address'])
    
    driver.find_element(By.NAME, "postal_code").clear()
    driver.find_element(By.NAME, "postal_code").send_keys(row['Postal Code'])
    
    driver.find_element(By.NAME, "phone").clear()
    driver.find_element(By.NAME, "phone").send_keys(row['Phone'])
    
    driver.find_element(By.NAME, "email").clear()
    driver.find_element(By.NAME, "email").send_keys(row['Email'])
    
    # Wait a bit to avoid sending data too quickly
    time.sleep(2)
    
    # Submit the form
    driver.find_element(By.NAME, "submit_button").click()
    
    # Wait a bit to avoid sending data too quickly
    # time.sleep(1)

# Do not close the browser
# driver.quit()
