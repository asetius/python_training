# from selenium import webdriver
import selenium.webdriver.common.by


class SessionHelper:

    def __init__(self, app):
        self.app = app
        # self.driver = webdriver.Firefox()
        # self.vars = {}


    def login(self, username, password):
        self.app.open_home_page()
        self.driver.find_element(selenium.webdriver.common.by.By.NAME, "user").send_keys(username)
        self.driver.find_element(selenium.webdriver.common.by.By.NAME, "pass").click()
        self.driver.find_element(selenium.webdriver.common.by.By.NAME, "pass").send_keys(password)
        self.driver.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR, "input:nth-child(7)").click()

    def logout(self):
        self.driver.find_element(selenium.webdriver.common.by.By.LINK_TEXT, "Logout").click()
