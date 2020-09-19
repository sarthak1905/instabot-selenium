from selenium import webdriver 
from getpass import getpass
import time

#Class for the bot
class InstaBot:

    #Initializes bot 
    def __init__(self):
        self.PATH = "C:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(self.PATH)
    
    #Starts Instagram
    def start(self):
        self.driver.get('https://www.instagram.com/')
        time.sleep(2)
        return

    #Logs into your account, also closes various dialogue boxes that open on the way 
    def login(self,username,pw):

        self.username = username
        self.pw = pw

        user_field = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        pw_field = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        login_button = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
        user_field.send_keys(self.username)
        pw_field.send_keys(self.pw)
        login_button.click()
        time.sleep(2.5)
        not_now1 = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        not_now1.click()
        time.sleep(1)
        not_now2 = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        not_now2.click()
        time.sleep(1)
        return

    #Opens your profile
    def open_profile(self):
        profile_link = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a')
        profile_link.click()
        time.sleep(2)
        return

    #Opens the list of the people you follow
    def open_following(self):
        following_link = self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[3]/a')
        following_link.click()
        return

    #Gets the list of the people you follow
    def get_following(self):
        self.following = self.scroll_list_following()
        print(self.following)
        return

    #Scrolls the list of your following and retrieves their names
    def scroll_list_following(self):
        time.sleep(2)
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[4]/div/div")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            time.sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        return names

def main():

    #Inputs username and password of your account 
    username = input('Enter your username:')
    pw = getpass('Enter your password(will NOT appear as you type):')

    #Actual bot working 
    bb8 = InstaBot()
    bb8.start()
    bb8.login(username,pw)
    bb8.open_profile()
    bb8.open_following()
    bb8.get_following()
    time.sleep(1000)

if __name__ =='__main__':
    main()