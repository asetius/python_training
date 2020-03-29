import selenium.webdriver.common.by


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        self.driver = self.app.driver
        self.app.open_home_page()
        self.driver.find_element(selenium.webdriver.common.by.By.NAME, "user").send_keys(username)
        self.driver.find_element(selenium.webdriver.common.by.By.NAME, "pass").click()
        self.driver.find_element(selenium.webdriver.common.by.By.NAME, "pass").send_keys(password)
        self.driver.find_element(selenium.webdriver.common.by.By.CSS_SELECTOR, "input:nth-child(7)").click()

    def logout(self):
        self.driver = self.app.driver
        self.driver.find_element(selenium.webdriver.common.by.By.LINK_TEXT, "Logout").click()
