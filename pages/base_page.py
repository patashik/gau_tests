from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests

class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def should_be_correct_response_status_code(self):
        code = 200
        try:
            status_code = requests.get(self.browser.current_url).status_code
            print(self.browser.current_url)
            print(status_code)
            assert status_code == code, "Status not correct"
        except TimeoutException:
            return False
        return True

    def change_language(self, language):
        language_button = self.is_clickable(*BasePageLocators.LANGUAGE_BUTTON)
        language_button.click()
        language_bar = self.is_visible(*BasePageLocators.LANGUAGE_BAR)
        self.browser.switch_to.frame(language_bar)
        language_item = self.browser.find_element(By.XPATH, '//span[text()="'+language+'"]')
        language_item.click()
        self.browser.implicitly_wait(5)
        self.should_be_correct_response_status_code()

    def go_to_register_page(self):
        register_url = "http://academy21.ru/index.php?do=register"
        register_button = self.is_clickable(*BasePageLocators.REGISTER_BUTTON)
        register_button.click()
        self.url_changed()
        self.should_be_correct_response_status_code()
        assert self.url_contains(register_url), "Did not open Register page"
    
    def go_to_appeal_page(self):
        letter_url = "http://appeal.academy21.ru/"
        letter_button = self.is_clickable(*BasePageLocators.LETTER_BUTTON)
        letter_button.click()
        self.url_changed()
        self.should_be_correct_response_status_code()
        assert self.url_contains(letter_url), "Did not open Appeal page"

    def has_disappeared(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
    
    def is_clickable(self, how, what, timeout=10):
        element = WebDriverWait(self.browser, timeout, 1).until(EC.element_to_be_clickable((how, what)))
        return element
    
    def is_visible(self, how, what, timeout=100):
        element = WebDriverWait(self.browser, timeout, 1).until(EC.visibility_of_element_located((how, what)))
        return element
    
    def start_search_by_button(self, search_request):
        search_string = self.is_clickable(*BasePageLocators.SEARCH_STRING)
        search_string.click()
        search_string.send_keys(search_request)
        search_button = self.is_clickable(*BasePageLocators.SEARCH_BUTTON)
        search_button.click()

    def start_search_by_enter(self, search_request):
        search_string = self.is_clickable(*BasePageLocators.SEARCH_STRING)
        search_string.click()
        search_string.send_keys(search_request)
        search_string.send_keys(Keys.ENTER)

    def switch_to_visually_impaired_mode(self):
        vis_mode_button = self.is_visible(*BasePageLocators.VIS_MODE_BUTTON)
        vis_mode_button.click()
        normal_mode_button = self.is_visible(*BasePageLocators.NORMAL_MODE_BUTTON)
        assert normal_mode_button, "Did not switch to visually impaired mode"

    def url_changed(self, timeout=30):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until(EC.url_changes((self.browser.current_url)))
        except TimeoutException:
            return False
        return True

    def url_contains(self, url_text, timeout=30):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until(EC.url_contains(url_text))
        except TimeoutException:
            return False
        return True
        
    def url_to_be(self, new_url, timeout=30):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until(EC.url_to_be(new_url))
        except TimeoutException:
            return False
        return True