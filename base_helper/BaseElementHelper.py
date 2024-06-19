from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class BaseElementHelper(object):

    def __init__(self,  browser):
        self.browser = browser

    def navigate_to(self, url_path):
        try:
            self.browser.get(url_path)
        except TimeoutException:
            print("No URL found")

    def get_element_by_xpath(self, xpath_expresion):
        try:
            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_expresion)))
        except TimeoutException:
            print("No element found")

        return element

    def get_element_by_id(self, element_id):
        try:
            element = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.ID, element_id)))
        except TimeoutException:
            print("No element found")

        return element

    def element_click(self, element):
        try:
            element.click()
        except TimeoutException:
            print("No element found")

    def element_send_keys(self, element, keys):
        try:
            element.click()
            element.clear()
            element.send_keys(keys)
        except TimeoutException:
            print("No element found")

    def element_select_by_visible_value(self, element, value):
        try:
            elem = Select(element)
            elem.select_by_value(value)
        except TimeoutException:
            print("No element found")
