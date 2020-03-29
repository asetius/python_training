import selenium.webdriver.common.by


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        self.driver = self.app.driver
        self.driver.find_element(selenium.webdriver.common.by.By.LINK_TEXT, "groups").click()

    def create_group(self, group):
        self.driver = self.app.driver
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
        self.driver = self.app.driver
        self.driver.find_element(selenium.webdriver.common.by.By.LINK_TEXT, "group page").click()
