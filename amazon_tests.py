import unittest
from browsers_util.Browsers import Browsers
from base_helper.BaseElementHelper import BaseElementHelper
from yml_parser.YmlParser import YmlParser


class AmazonTests(unittest.TestCase):

    def setUp(self):
        self.browser = Browsers().get_chrome_browser("drivers/chromedriver.exe")
        self.web_page = BaseElementHelper(self.browser)
        self.test_data = YmlParser()
        self.test_data.load_file('test_data/TestData.yml')

    def test_orderFirstHarryPotterLegoToy(self):
        self.web_page.navigate_to(self.test_data.get_values('amazon_url'))

        element = self.web_page.get_element_by_id(self.test_data.get_values('search_input'))
        self.web_page.element_send_keys(element, 'Harry Potter')

        element = self.web_page.get_element_by_xpath(self.test_data.get_values('go_button'))
        self.web_page.element_click(element)

        element = self.web_page.get_element_by_xpath(self.test_data.get_values('see_all'))
        self.web_page.element_click(element)

        element = self.web_page.get_element_by_xpath(self.test_data.get_values('toys_and_games'))
        self.web_page.element_click(element)

        element = self.web_page.get_element_by_id(self.test_data.get_values('low_price'))
        self.web_page.element_click(element)
        self.web_page.element_send_keys(element, self.test_data.get_values('low_value'))

        element = self.web_page.get_element_by_id(self.test_data.get_values('high-price'))
        self.web_page.element_click(element)
        self.web_page.element_send_keys(element, self.test_data.get_values('high_value'))

        element = self.web_page.get_element_by_xpath(self.test_data.get_values('search_button'))
        self.web_page.element_click(element)

        element = self.web_page.get_element_by_xpath(self.test_data.get_values('14_years_and_up'))
        self.web_page.element_click(element)

        element = self.web_page.get_element_by_xpath(self.test_data.get_values('lego_harry_potter'))
        self.web_page.element_click(element)

        element = self.web_page.get_element_by_xpath(self.test_data.get_values('quantity_button'))
        self.web_page.element_select_by_visible_value(element, self.test_data.get_values('desired_quantity'))

        element = self.web_page.get_element_by_id(self.test_data.get_values('add_to_cart_button'))
        self.web_page.element_click(element)

        element = self.web_page.get_element_by_xpath(self.test_data.get_values('view_cart_button'))
        self.web_page.element_click(element)

        element = self.web_page.get_element_by_id(self.test_data.get_values('active_cart_button'))
        self.web_page.element_click(element)

        self.assertEqual(element.text, self.test_data.get_values('test_orderFirstHarryPotterLegoToy_exp_result'))

    def tearDown(self):
        self.browser.quit()


if __name__ == "__main__":
        unittest.main()
