from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.by import by

service = Service() #] é usada para instanciar o chrome webdriver
options = webdriver.ChromeOptions() # definir preferencias do chrome
driver = webdriver.Chrome(service=service, options=options)

url = ""

driver.get(url)
time.sleep(5)