from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

class OrangeHRM():
    def login(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.get("https://opensource-demo.orangehrmlive.com/")

        username = driver.find_element(By.ID, "txtUsername")

        if username is not None:
            print("We found username by ID")
        else:
            print("We dont found username by id")

        password = driver.find_element(By.NAME, "txtPassword")

        if password is not None:
            print("We found password by Name")
        else:
            print("We dont found password by Name")

        driver.close()

test_obj = OrangeHRM()
test_obj.login()