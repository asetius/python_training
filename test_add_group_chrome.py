# Generated by Selenium IDE
import selenium.webdriver.common.by
from selenium import webdriver
from group import Group

class TestAddGroup():
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def test_add_group(self):
        self.open_home_page()
        self.login(username="admin", password="secret")
        self.open_group_page()
        self.create_group(Group(name="Clients", header="Clients", footer="Clients"))
        self.return_to_groups()
        self.logout()

    def test_add_empty_group(self):
        self.open_home_page()
        self.login(username="admin", password="secret")
        self.open_group_page()
        self.create_group(Group(name="", header="", footer=""))
        self.return_to_groups()
        self.logout()

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")

    def login(self, username, password):
        self.driver.find_element(selenium.webdriver.common.by.By.NAME, "user").send_keys(username)
        self.driver.find_element(selenium.webdriver.common.by.By.NAME, "pass").click()
        self.driver.find_element(selenium.webdriver.common.by.By.NAME, "pass").send_keys(password)
        self.driver.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR, "input:nth-child(7)").click()

    def open_group_page(self):
        self.driver.find_element(selenium.webdriver.common.by.By.LINK_TEXT, "groups").click()

    def create_group(self, group):
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

    def return_to_groups(self):
        self.driver.find_element(selenium.webdriver.common.by.By.LINK_TEXT, "group page").click()

    def logout(self):
        self.driver.find_element(selenium.webdriver.common.by.By.LINK_TEXT, "Logout").click()

    def teardown_method(self):
        self.driver.quit()
