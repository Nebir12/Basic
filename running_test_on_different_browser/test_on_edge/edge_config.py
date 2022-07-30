from selenium import webdriver

class Test_Edge():
    def launch_Edge(self):
        # instantiate edge browser
        driver = webdriver.Edge(executable_path="C:\pythonProject1\drivers\msedgedriver103.0.exe")


firefox_obj= Test_Edge()
firefox_obj.launch_Edge()

