from selenium import webdriver
import selenium.webdriver.common.by
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.vars = {}
        self.session = SessionHelper(self)

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")

    def open_group_page(self):
        self.driver.find_element(selenium.webdriver.common.by.By.LINK_TEXT, "groups").click()

    def create_group(self, group):
        self.open_group_page()
        # init group creation
        self.driver.find_element(selenium.webdriver.common.by.By.NAME, "new").click()
        # fill group form
        self.driver.find_element(selenium.webdriver.common.by.By.NAME, "group_name").click()
        self.driver.find_element(selenium.webdriver.common.by.By.NAME, "group_name").send_keys(group.name)
        self.driver.find_element(selenium.webdriver.common.by.By.NAME, "group_header").click()
        self.driver.find_element(selenium.webdriver.common.by.By.NAME, "group_header").send_keys(group.header)
        self.driver.find_element(selenium.webdriver.common.by.By.NAME, "group_footer").click()
        self.driver.find_element(selenium.webdriver.common.by.By.NAME, "group_footer").send_keys(group.footer)
        # submit
        self.driver.find_element(selenium.webdriver.common.by.By.NAME, "submit").click()
        self.return_to_groups()

    def return_to_groups(self):
        self.driver.find_element(selenium.webdriver.common.by.By.LINK_TEXT, "group page").click()

    def destroy(self):
        self.driver.quit()
