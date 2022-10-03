from selenium.webdriver.common.by import By


class LoginPage:

    TITLE_PAGE_TEXT = (By.CSS_SELECTOR, "h1")
    EMAIL_INPUT = (By.ID, "user_login_email")
    SUBMIT_BUTTON = (By.ID, "user_login_continue")
    PASSWORD_INPUT = (By.ID, "user_login_password")
    REMEMBER_ME_CHECKBOX = (By.CSS_SELECTOR, '[for="remember_me"]')
    FORGOT_PASSWORD = (By.LINK_TEXT, "Ai uitat parola?")

    URL = 'https://auth.emag.ro/user/login'

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)

    def get_title_page(self):
        return self.browser.find_element(*self.TITLE_PAGE_TEXT).text

    def insert_email(self, email):
        self.browser.find_element(*self.EMAIL_INPUT).send_keys(email)

    def insert_password(self, password):
        self.browser.find_element(*self.PASSWORD_INPUT).send_keys(password)

    def click_submit_button(self):
        self.browser.find_element(*self.SUBMIT_BUTTON).click()

    def is_submit_button_displayed(self):
        return self.browser.find_element(*self.SUBMIT_BUTTON).is_displayed()

