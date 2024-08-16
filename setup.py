# cspell: disable

import os
import requests
import zipfile
import subprocess
import sys
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Function to install packages if they are not already installed
def install_package(package):
    try:
        __import__(package)
    except ImportError:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# Check and install the necessary libraries
required_packages = ['selenium', 'shutil', 'requests']
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

# At this point, the WebDriver is ready to be used for further automation tasks

# Close the browser when done
driver.quit()
