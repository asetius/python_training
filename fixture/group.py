import selenium.webdriver.common.by


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        self.driver = self.app.driver
        self.driver.find_element(selenium.webdriver.common.by.By.LINK_TEXT, "groups").click()

    def create(self, group):
        self.driver = self.app.driver
        self.open_group_page()
        # init group creation
        self.driver.find_element(selenium.webdriver.common.by.By.NAME, "new").click()
        self.fill_group_form(group)
        # submit
        self.driver.find_element(selenium.webdriver.common.by.By.NAME, "submit").click()
        self.return_to_groups()

    def fill_group_form(self, group):
        self.driver = self.app.driver
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        self.driver = self.app.driver
        if text is not None:
            self.driver.find_element(selenium.webdriver.common.by.By.NAME, field_name).click()
            self.driver.find_element(selenium.webdriver.common.by.By.NAME, field_name).clear()
            self.driver.find_element(selenium.webdriver.common.by.By.NAME, field_name).send_keys(text)

    def delete_first_group(self):
        self.driver = self.app.driver
        self.open_group_page()
        self.select_first_group()
        # submit deletion
        self.driver.find_element(selenium.webdriver.common.by.By.NAME, "delete").click()
        self.return_to_groups()

    def select_first_group(self):
        self.driver = self.app.driver
        self.driver.find_element(selenium.webdriver.common.by.By.NAME, "selected[]").click()

    def modify_first_group(self, new_group_data):
        self.driver = self.app.driver
        self.open_group_page()
        self.select_first_group()
        # open modification form
        self.driver.find_element(selenium.webdriver.common.by.By.NAME, "edit").click()
        # fill group form
        self.fill_group_form(new_group_data)
        # submit modification
        self.driver.find_element(selenium.webdriver.common.by.By.NAME, "update").click()
        self.return_to_groups()


    def return_to_groups(self):
        self.driver = self.app.driver
        self.driver.find_element(selenium.webdriver.common.by.By.LINK_TEXT, "group page").click()
