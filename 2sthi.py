import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

op = webdriver.ChromeOptions()
op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
op.add_argument("--headless")
op.add_argument("--no-sandbox")
op.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),  options=op)
driver.get("https://glauniversity.in:8070/LeadManagement/ShowResult")

s,e = 9080060,9080070
for i in range(s,e):
    a = 'GLA2022-1'+str(i).zfill(7)
    driver.find_element(By.XPATH,"//input[contains(@id,'reg')]").send_keys(a)
    driver.find_element(By.XPATH,"//input[contains(@class,'btn')]").click()
    driver.implicitly_wait(0.025)
    try :
        s = driver.find_element(By.XPATH,"//div[normalize-space()='Sorry! Registration Number Not Found']")
        print (s.txt )
    except :
        try :
            rgnames = driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/h4[1]")
            rehm = rgnames.text
            print(rehm)
        except :
            pass
    driver.find_element(By.XPATH,"//input[contains(@id,'reg')]").clear()
