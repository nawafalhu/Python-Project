import tweepy 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import sleep

PDown = 150
PUP = 10
Account_Email = "nawafalhu@gmail.com"
Account_Password = "Ee123123"
User_Account = "test1149197"

class InternetSpeedTwitterBot :
    def __init__(self) :
        self.chrome_option = webdriver.ChromeOptions()
        self.chrome_option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_option)
        self.setup = 0
        self.setdown = 0

    def get_internet_speed(self) :
        self.driver.get("https://www.speedtest.net/")

        self.GO_button = self.driver.find_element(By.XPATH, value="/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a")
        self.GO_button.click()

        sleep(40)
        self.setdown = self.driver.find_element(By.XPATH, value="/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span").text
        self.setup = self.driver.find_element(By.XPATH, value="/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text
        return f"the download is {self.setdown}, and upload is {self.setup}"

    def tweet_at_provider(self) :
        self.driver.get("https://twitter.com/login")

        sleep(10)
        email_input = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        email_input.send_keys(Account_Email)
        sleep(1)
        email_input.send_keys(Keys.ENTER)
        sleep(5)
        try:
            pass_input = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
            pass_input.send_keys(Account_Password)
            pass_input.send_keys(Keys.ENTER)
        except NoSuchElementException:
            username = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
            username.send_keys(User_Account)  #Your Username here in case Twitter asks for username before asking password
            username.send_keys(Keys.ENTER)
            sleep(5)
            pass_input = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
            pass_input.send_keys(Account_Password)
            pass_input.send_keys(Keys.ENTER)
        sleep(5)
        input = self.driver.find_element(By.CSS_SELECTOR, 'br[data-text="true"]')
        input.send_keys(f"My Current Internet Speed is {self.setdown} Download and {self.setup} Upload")
        sleep(3)
        tweet = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div/div/div")
        tweet.click()
        sleep(5)
        print("Tweet Done")
        self.driver.quit()

bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
