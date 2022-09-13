from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import os

if 20 > datetime.now().hour < 9:
    print("Еще не время")
    exit()

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-devshm-usage")
chrome_options.add_argument("--no-sandbox")

try:
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
    driver.get("https://lk.sut.ru/cabinet/")
    driver.find_element(By.ID, "users").send_keys("gnataly2106@mail.ru")
    driver.find_element(By.ID, "parole").send_keys("Andrey2002")
    driver.find_element(By.ID, "logButton").click()
    sleep(3)
    driver.find_element(By.ID, "heading1").click()
    driver.find_element(By.ID, "menu_li_6118").click()
    sleep(3)
    driver.find_element(By.LINK_TEXT, "Начать занятие").click()
    print("Кнопка найдена и нажата")
except:
    print("Нет кнопки или произошла ошибка")