class BasePage():
    '''Description of a base class for all webpages'''
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)