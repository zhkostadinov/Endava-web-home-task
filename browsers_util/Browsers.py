from selenium import webdriver


class Browsers(object):

    def __init__(self):
        self.browser = None

    def get_chrome_browser(self, path_to_driver):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        browser = webdriver.Chrome(executable_path=path_to_driver, options=options)

        self.browser = browser
        self.browser.maximize_window()
        self.browser.implicitly_wait(60)

        return self.browser
