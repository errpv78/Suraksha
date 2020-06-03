from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
from sys import platform
from opencage.geocoder import OpenCageGeocode




def get_current_Location():
    cwd = os.getcwd()
    if platform == "linux" or platform == "linux2":
        driver_path = cwd + "/chromedriver"
    else:
        driver_path = cwd + "\chromedriver"
    options = Options()
    options.add_argument("--use-fake-ui-for-media-stream")
    timeout = 20
    driver = webdriver.Chrome(executable_path = driver_path, options=options)
    driver.get("https://mycurrentlocation.net/")
    wait = WebDriverWait(driver, timeout)
    time.sleep(3)
    longitude = driver.find_elements_by_xpath('//*[@id="longitude"]')
    longitude = [x.text for x in longitude]
    longitude = str(longitude[0])
    latitude = driver.find_elements_by_xpath('//*[@id="latitude"]')
    latitude = [x.text for x in latitude]
    latitude = str(latitude[0])
    driver.quit()
    key = 'd25ac72e7a1e43b8a2d3c939895889d1'
    geocoder = OpenCageGeocode(key)

    results = geocoder.reverse_geocode(float(lat), float(long))
    # print(type(results))

    location = results[0]["formatted"]
    coordinates = results[0]["geometry"]
    return str(location)+ str(coordinates)