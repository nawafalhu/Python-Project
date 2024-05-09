from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

Email = "n.alhu10@gmail.com"
Password = "NnAaFf10"

class InstaFollower :
    def __init__(self) :
        self.chrome_option = webdriver.ChromeOptions()
        self.chrome_option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_option)
    
    def login(self) :
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(5)
        
        Email_Entry = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[1]/div/label/input')
        Password_Entry = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[2]/div/label/input')
        
        sleep(2)
        Email_Entry.send_keys(Email)
        Password_Entry.send_keys(Password)
        sleep(2)
        Password_Entry.send_keys(Keys.ENTER)
        try :
            sleep(2)
            dm = self.driver.find_element(By.XPATH, value='//*[@id="mount_0_0_8P"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div/div[5]/div/div/div/span/div/a/div/div/div/div')
            dm.click()

            sleep(2)
            chat = self.driver.find_element(By.XPATH, value='//*[@id="mount_0_0_NX"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div[2]/div')
            chat.click()

            sleep(2)
            text = self.driver.find_element(By.XPATH, value='//*[@id="mount_0_0_NX"]/div/div/div[2]/div/div/div/div[1]/div[1]/div[2]/section/div/div/div/div[1]/div/div[2]/div/div/div/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/div[1]')
            text.send_keys("السلام عليكم ورحمة الله وبركاته")
            text.send_keys(Keys.ENTER)
        except NoSuchElementException :
            pass

    def find_followers(self):
        pass

    def follow(self):
        pass

bot = InstaFollower()
bot.login()
