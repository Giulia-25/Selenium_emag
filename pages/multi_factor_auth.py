from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MultiFactorAuth:

    ACTIVATE_LATER_BUTTON = (By.LINK_TEXT, "Activează mai târziu")
    URL = "https://www.emag.ro/user/mfa-optin"

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def click_activate_later_button(self):
        activate_later_button = WebDriverWait(self.browser, 4).until(EC.presence_of_element_located((By.LINK_TEXT, "Activează mai târziu")))
        activate_later_button.click()

    def is_activate_later_button_displayed(self):
        activate_later_button = WebDriverWait(self.browser, 4).until(EC.presence_of_element_located((By.LINK_TEXT, "Activează mai târziu")))
        return activate_later_button.is_displayed()