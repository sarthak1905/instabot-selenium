from selenium import webdriver 
from getpass import getpass
import time

class InstaBot:
    def __init__(self):
        self.PATH = "C:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(self.PATH)
    
    def start(self):
        self.driver.get('https://www.instagram.com/')
        time.sleep(2)
        return

    def login(self,username,pw):
        self.username = username
        self.pw = pw
        user_field = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        pw_field = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        login_button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
        user_field.send_keys(self.username)
        pw_field.send_keys(self.pw)
        login_button.click()
        time.sleep(2)
        not_now1 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now1.click()
        time.sleep(1)
        not_now2 = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        not_now2.click()
        time.sleep(1)
        return

    def open_profile(self):
        profile_link = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a')
        profile_link.click()
        time.sleep(2)
        return

    def open_following(self):
        following_link = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a')
        following_link.click()
        return

    def scroll_list_following(self):
        SCROLL_PAUSE_TIME = 1

        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height
        return

def main():
    username = input('Enter your username:')
    pw = getpass('Enter your password(will NOT appear as you type):')
    bb8 = InstaBot()
    bb8.start()
    bb8.login(username,pw)
    bb8.open_profile()
    bb8.open_following()
    bb8.scroll_list_following()
    time.sleep(1000)

if __name__ =='__main__':
    main()