from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

class OrangeHRM():
    def test_login_valid(self):
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        driver.get("https://opensource-demo.orangehrmlive.com/")

        # Find Elements
        username = driver.find_element(By.ID, "txtUsername")
        password = driver.find_element(By.NAME, "txtPassword")
        login_btn= driver.find_element(By.ID, "btnLogin")

        # Login Action
        username.clear()
        username.send_keys("Admin")

        password.clear()
        password.send_keys("admin123")

        login_btn.click()

        #driver.close()

test_obj = OrangeHRM()
test_obj.test_login_valid()