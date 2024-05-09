from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

Account_Email = "n.alhu10@gmail.com"
Account_Password = "Ee&10O@Aa$nawaf"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.udacity.com/")

# Click Sign in Button
time.sleep(2)
sign_in_button = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/header/div[1]/div[2]/div[3]/div/a[1]")
sign_in_button.click()


# Sign in
time.sleep(5)
Email_Entry = driver.find_element(By.ID, value="email")
Email_Entry.send_keys(Account_Email)

Password_Entry = driver.find_element(By.ID, value="revealable-password")
Password_Entry.send_keys(Account_Password)
Password_Entry.send_keys(Keys.ENTER)
