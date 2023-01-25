from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import pytest
import time

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

  
def test_one():
    driver.get("https://fime.com")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR,"a[href='/contact']").click()
    time.sleep(5)


