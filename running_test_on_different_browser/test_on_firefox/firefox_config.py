from selenium import webdriver

class Test_Firefox():
    def launch_firefox(self):
        # instantiate firefox browser
        driver = webdriver.Firefox(executable_path="C:\pythonProject1\drivers\geckodriver-0.31.0.exe")
        driver.get("http://google.com")
        driver.quit()

firefox_obj= Test_Firefox()
firefox_obj.launch_firefox()

