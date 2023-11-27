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

    def any_of(self, how1, what1, how2, what2, timeout=10):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until(
                EC.any_of(
                    EC.presence_of_element_located((how1, what1)),
                    EC.presence_of_element_located((how2, what2)),
                )
            )
        except TimeoutException:
            return False
        return True

    def change_language(self, language):
        language_button = self.is_clickable(*BasePageLocators.LANGUAGE_BUTTON)
        language_button.click()
        language_bar = self.is_visible(*BasePageLocators.LANGUAGE_BAR)
        self.browser.switch_to.frame(language_bar)
        language_item = self.browser.find_element(By.XPATH, f'//span[text()="{language}"]')
        language_item.click()
        self.browser.implicitly_wait(5)
        self.should_be_correct_response_status_code()

    def click_extended_search(self):
        extended_search_button = self.is_clickable(*BasePageLocators.EXTENDED_SEARCH_BUTTON)
        extended_search_button.click()
        self.url_changed()
        self.should_be_correct_response_status_code()
        assert self.url_contains("search"), "Did not open Extended Search page"
    
    def go_to_appeal_page(self):
        letter_url = "http://appeal.academy21.ru/"
        letter_button = self.is_clickable(*BasePageLocators.APPEAL_BUTTON)
        letter_button.click()
        self.url_changed()
        self.should_be_correct_response_status_code()
        assert self.url_contains(letter_url), "Did not open Appeal page"
        
    def go_to_main_page(self):
        main_url = "http://academy21.ru/"
        logo_button = self.is_clickable(*BasePageLocators.LOGO_BUTTON)
        logo_button.click()
        self.url_changed()
        self.should_be_correct_response_status_code()
        assert self.url_to_be(main_url), "Did not open Main page"
    
    def go_to_register_page(self):
        register_url = "http://academy21.ru/index.php?do=register"
        register_button = self.is_clickable(*BasePageLocators.REGISTER_BUTTON)
        register_button.click()
        self.url_changed()
        self.should_be_correct_response_status_code()
        assert self.url_contains(register_url), "Did not open Register page"
    
    def go_to_search(self):
        search_button = self.is_clickable(*BasePageLocators.SEARCH_BUTTON)
        search_button.click()
        search_string = self.is_clickable(*BasePageLocators.SEARCH_BAR_INPUT)
        assert search_string, 'Did not go to search'
    
    def go_to_user_profile(self, name):
        profile_button = self.is_clickable(*BasePageLocators.PROFILE_BUTTON)
        profile_button.click()
        profile_menu = self.is_visible(*BasePageLocators.PROFILE_MENU)
        my_profile_button = self.is_clickable(*BasePageLocators.MY_PROFILE_BUTTON)
        my_profile_button.click()
        self.url_changed()
        self.should_be_correct_response_status_code()
        assert self.url_contains(f"user/{name}"), "Did not open user profile"
    
    def has_disappeared(self, how, what, timeout=10):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True
    
    def is_clickable(self, how, what, timeout=10):
        element = WebDriverWait(self.browser, timeout, 1).until(EC.element_to_be_clickable((how, what)))
        return element

    def is_presented(self, how, what, timeout=10):
        element = WebDriverWait(self.browser, timeout, 1).until(EC.presence_of_element_located((how, what)))
        return element
    
    def is_visible(self, how, what, timeout=100):
        element = WebDriverWait(self.browser, timeout, 1).until(EC.visibility_of_element_located((how, what)))
        return element
    
    def log_in(self, name, password):
        login_button = self.is_clickable(*BasePageLocators.LOGIN_BUTTON)
        login_button.click()
        login_name = self.is_clickable(*BasePageLocators.LOGIN_NAME)
        login_name.send_keys(name)
        login_password = self.is_clickable(*BasePageLocators.LOGIN_PASSWORD)
        login_password.send_keys(password)
        login_submit_button = self.is_clickable(*BasePageLocators.LOGIN_SUBMIT_BUTTON)
        login_submit_button.click()
        profile_button = self.is_clickable(*BasePageLocators.PROFILE_BUTTON)
        logout_button = self.is_clickable(*BasePageLocators.LOGOUT_BUTTON)
        assert profile_button and logout_button, 'Login unsuccessful'

    def log_out(self):
        logout_button = self.is_clickable(*BasePageLocators.LOGOUT_BUTTON)
        logout_button.click()
        login_button = self.is_clickable(*BasePageLocators.LOGIN_BUTTON)
        register_button = self.is_clickable(*BasePageLocators.REGISTER_BUTTON)
        assert login_button and register_button, 'Logout unsuccessful'
    
    def should_be_any_of_messages(self):
        assert self.any_of(*BasePageLocators.SEARCH_RESULT_MESSAGE, *BasePageLocators.NO_SEARCH_RESULT_MESSAGE)
    
    def should_be_results_message(self):
        text = "По Вашему запросу найдено"
        search_result_message = self.is_visible(*BasePageLocators.SEARCH_RESULT_MESSAGE)
        print(search_result_message.text)
        assert text in search_result_message.text, "Search did not start"
    
    def should_be_no_search_request_in_search_string(self):
        search_string = self.is_visible(*BasePageLocators.SEARCH_BAR_INPUT)
        search_input = search_string.get_attribute("value")
        assert search_input == '', "Search string is not empty"

    def should_be_search_request_in_search_string(self, search_request):
        search_string = self.is_visible(*BasePageLocators.SEARCH_BAR_INPUT)
        search_input = search_string.get_attribute("value")
        assert search_input == search_request, "Search string does not match initial search request"
    
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