# Import required packages
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

# Define the chromedriver service
s = Service('chromedriver.exe')
# Instantiate the webdriver
driver = webdriver.Chrome(service=s)
# check heading_class is present or not first by document.querySelector("");, leetcode page's heading and body class changes day by day

heading_class = ".mr-2.text-label-1"
body_class = ".px-5.pt-4"
index = 1
QDATA_FOLDER = "Qdata"


def get_array_of_links():
    arr = []  # Array to store the lines of the file
# Open the file
    with open("lc_problems.txt", "r") as file:
        # Read each line one by one
        for line in file:
            arr.append(line)
    return arr


def add_text_to_index_file(text):
    index_file_path = os.path.join(QDATA_FOLDER, "index.txt")
    with open(index_file_path, "a") as index_file:
        index_file.write(text + "\n")


def add_link_to_Qindex_file(text):
    index_file_path = os.path.join(QDATA_FOLDER, "Qindex.txt")
    with open(index_file_path, "w", encoding="utf-8", errors="ignore") as Qindex_file:
        Qindex_file.write(text)


def create_and_add_text_to_file(file_name, text):
    folder_path = os.path.join(QDATA_FOLDER, file_name)
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, file_name + ".txt")
    with open(file_path, "w", encoding="utf-8", errors="ignore") as new_file:
        new_file.write(text)


def getPagaData(url, index):
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, body_class)))
        time.sleep(1)
        heading = driver.find_element(By.CSS_SELECTOR, heading_class)
        body = driver.find_element(By.CSS_SELECTOR, body_class)
        print(heading.text)
        if (heading.text):
            add_text_to_index_file(heading.text)
            add_link_to_Qindex_file(url)
            create_and_add_text_to_file(str(index), body.text)
        time.sleep(1)
        return True
    except Exception as e:
        print(e)
        return False


arr = get_array_of_links()
for link in arr:
    success = getPagaData(link, index)
    if (success):
        index = index+1


driver.quit()
