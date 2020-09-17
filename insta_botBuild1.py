from selenium import webdriver 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from getpass import getpass
import time

class InstaBot:
    def __init__(self):
        self.PATH = "C:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(self.PATH)
    
    def start(self):
        self.driver.get('https://www.instagram.com/')
        time.sleep(3)

    def login(self,username,pw):
        self.username = username
        self.pw = pw
        user_field = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        pw_field = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        login_button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
        user_field.send_keys(self.username)
        pw_field.send_keys(self.pw)
        login_button.click()
        time.sleep(3)
        not_now1 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now1.click()
        time.sleep(2)
        not_now2 = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        not_now2.click()
        time.sleep(1000)

def main():
    bb8 = InstaBot()
    bb8.start()
    username = input('Enter your username:')
    pw = getpass()
    bb8.login(username,pw)

if __name__ =='__main__':
    main()