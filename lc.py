# these are just various libraries that I used to make this script work
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time
from bs4 import BeautifulSoup

# this is the path to the chromedriver.exe file
# download it from here: https://chromedriver.chromium.org/downloads
# and put it in the same folder as this script
# i have used chrome that's why chromedriver.exe

s = Service('chromedriver.exe')
driver = webdriver.Chrome(service=s)

# base url of leetcode problems page
# i will iterate from 1 to 55 below
page_URL = "https://leetcode.com/problemset/all/?page="

# function to get all a tags and filter out the ones that have the pattern "/problems/"
# this is because all the questions have this pattern in their url
# so i just filter out the ones that have this pattern
# and then write them to a file called lc.txt
# i have used a for loop to iterate from 1 to 55
# because there are 55 pages in the leetcode problems page
# and i have used time.sleep() to wait for 5 seconds after each page
# because i don't want to get blocked by leetcode
# and i have used try except because some a tags don't have href attribute
# so i just skip them
# and i have used with open() to write to the file
# and i have used 'a' as the second argument to append to the file
# because i don't want to overwrite the file
# and i have used '\n' to write each url on a new line
# because i want to read the file line by line later
# and i have used driver.quit() to quit the browser


def get_a_tags(url):
    driver.get(url)
    time.sleep(1)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    all_ques = soup.find_all('a')
    pattern = "/problems/"
    ans = []
    for i in all_ques:
        try:
            if pattern in i.get('href'):
                ans.append(i.get('href'))
        except:
            pass
    return ans


for i in range(1, 56):
    my_ans = get_a_tags(page_URL+str(i))
    time.sleep(5)
    with open('lc.txt', 'a') as f:
        for j in my_ans:
            f.write(j+'\n')


driver.quit()
