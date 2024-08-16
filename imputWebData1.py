# cspell: disable
import os
import requests
import zipfile
import subprocess
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import sys
import shutil

# Function to install packages if they are not already installed
def install_package(package):
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Check and install the necessary libraries
required_packages = ['requests', 'pandas', 'selenium', 'openpyxl', 'shutil']
for package in required_packages:
    install_package(package)

# Download and extract ChromeDriver
def download_chromedriver():
    chromedriver_zip = 'chromedriver.zip'
    extracted_folder = 'chromedriver-win64'
    chromedriver_path = f'./chromedriver.exe'
    
    # Check if the ChromeDriver file already exists
    if os.path.exists(chromedriver_path):
        print("ChromeDriver is already installed.")
        return
    
    url = "https://storage.googleapis.com/chrome-for-testing-public/127.0.6533.99/win64/chromedriver-win64.zip"
    
    # Download the ChromeDriver zip file
    with requests.get(url) as r:
        with open(chromedriver_zip, 'wb') as f:
            f.write(r.content)
    
    # Extract the ChromeDriver in the root folder from where the script is executed
    with zipfile.ZipFile(chromedriver_zip, 'r') as zip_ref:
        zip_ref.extractall('.')
    
    # Move the `chromedriver.exe` file from the extracted folder to the root
    if os.path.exists(extracted_folder):
        for item in os.listdir(extracted_folder):
            s = os.path.join(extracted_folder, item)
            d = os.path.join('.', item)
            if os.path.isdir(s):
                # Move directories
                shutil.move(s, d)
            else:
                # Move files
                shutil.move(s, d)
    
    # Clean up the extracted folder and the zip file
    os.rmdir(extracted_folder)
    os.remove(chromedriver_zip)
    print("ChromeDriver downloaded and extracted.")

# Download the corresponding ChromeDriver
download_chromedriver()

# Set up the browser using the downloaded ChromeDriver
service = Service(executable_path="./chromedriver.exe")
driver = webdriver.Chrome(service=service)

# URL of the webpage where the data will be entered
url = "file:///D:/Code/Ejemplo_selenium_CGPT/test_form.html"
driver.get(url)

# Read the Excel file
df = pd.read_excel('data.xlsx', engine='openpyxl')

# Iterate over each row of the DataFrame and fill out the form
for index, row in df.iterrows():
    # Fill out the form fields with data from the Excel file
    driver.find_element(By.NAME, "first_name").send_keys(row['First Name'])
    driver.find_element(By.NAME, "last_name_paternal").send_keys(row['Last Name (Paternal)'])
    driver.find_element(By.NAME, "last_name_maternal").send_keys(row['Last Name (Maternal)'])
    driver.find_element(By.NAME, "rfc").send_keys(row['RFC'])
    driver.find_element(By.NAME, "address").send_keys(row['Address'])
    driver.find_element(By.NAME, "postal_code").send_keys(row['Postal Code'])
    driver.find_element(By.NAME, "phone").send_keys(row['Phone'])
    driver.find_element(By.NAME, "email").send_keys(row['Email'])
    
    # Submit the form (this depends on how it is implemented on the page)
    driver.find_element(By.NAME, "submit_button").click()
    
    # Wait a bit to avoid sending data too quickly
    time.sleep(2)
    
    # Return to the page to fill out the next form (this depends on how it is implemented on the page)
    driver.get(url)

# Close the browser when done
driver.quit()
