from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_driver_path = r"C:\Users\nawaf"

# chrome_options = webdriver.ChromeOptions(chrome_driver_path)
# chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

driver.find_elemen