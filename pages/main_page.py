from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By
import time

class MainPage(BasePage):
    def should_be_results_message(self):
        text = "По Вашему запросу найдено"
        search_result_message = self.is_visible(*MainPageLocators.SEARCH_RESULT_MESSAGE)
        print(search_result_message.text)
        assert text in search_result_message.text, "Search did not start"
    
    def should_be_search_request_in_search_string(self, search_request):
        search_string = self.is_visible(*MainPageLocators.SEARCH_BAR_INPUT)
        search_input = search_string.get_attribute("value")
        assert search_request == search_input, "Search string does not match initial search request"
