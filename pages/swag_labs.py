from selenium.common.exceptions import NoSuchElementException
from pages.base_page import BasePage


class SwagLabs(BasePage):
    def exist_icon(self):

        try:
            self.find_element(locator="div.login_logo")
        except NoSuchElementException:
            return False
        return True

    def field_name(self):

        try:
            self.find_element(locator='input#user-name')
        except NoSuchElementException:
            return False
        return True

    def password_field(self):

        try:
            self.find_element(locator='input#password')
        except NoSuchElementException:
            return False
        return True
