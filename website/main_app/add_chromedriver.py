import time
from selenium import webdriver
from sys import platform
import os

def add_to_path():
    cwd = os.getcwd()
    if platform == "linux" or platform == "linux2":
        driver_path = cwd + "/main_app/chromedriver"
    else:
        driver_path = cwd + "\main_app\chromedriver"
    # print(driver_path)

    driver = webdriver.Chrome(driver_path)  # Optional argument, if not specified will search path.
    driver.get('http://www.google.com/');

    search_box = driver.find_element_by_name('q')
    search_box.send_keys('ChromeDriver')
    search_box.submit()

    driver.quit()

# add_to_path()