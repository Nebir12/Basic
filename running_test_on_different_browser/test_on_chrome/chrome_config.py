from selenium import webdriver

class Test_Chrome():
    def launch_Chrome(self):
        # instantiate Chrome browser
        driver = webdriver.Chrome(executable_path="C:\pythonProject1\drivers\chromedriver.exe")
        driver.get("http://google.com")
firefox_obj= Test_Chrome()
firefox_obj.launch_Chrome()

