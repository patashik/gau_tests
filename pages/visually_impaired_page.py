from .base_page import BasePage
from .locators import VisuallyImpairedPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import time

class VisuallyImpairedPage(BasePage):
    def should_be_search_request_in_search_string(self, search_request):
        search_string = self.is_visible(*VisuallyImpairedPageLocators.SEARCH_BAR_INPUT)
        search_input = search_string.get_attribute("value")
        assert search_request == search_input, "Search string does not match initial search request"
    
    def start_search_by_button(self, search_request):
        search_button = self.is_clickable(*VisuallyImpairedPageLocators.SEARCH_BUTTON)
        search_button.click()
        self.url_changed()
        self.should_be_correct_response_status_code()
        search_string = self.is_clickable(*VisuallyImpairedPageLocators.SEARCH_STRING)
        search_string.click()
        search_string.send_keys(search_request)
        start_search_button = self.is_clickable(*VisuallyImpairedPageLocators.START_SEARCH_BUTTON)
        start_search_button.click()
        
    def start_search_by_enter(self, search_request):
        search_button = self.is_clickable(*VisuallyImpairedPageLocators.SEARCH_BUTTON)
        search_button.click()
        self.url_changed()
        self.should_be_correct_response_status_code()
        search_string = self.is_clickable(*VisuallyImpairedPageLocators.SEARCH_STRING)
        search_string.click()
        search_string.send_keys(search_request)
        search_string.send_keys(Keys.ENTER)

    def should_be_results_message(self):
        text = "По Вашему запросу найдено"
        search_result_message = self.is_visible(*VisuallyImpairedPageLocators.SEARCH_RESULT_MESSAGE)
        print(search_result_message.text)
        assert text in search_result_message.text, "Search did not start"

    def switch_to_normal_mode(self):
        normal_mode_button = self.is_visible(*VisuallyImpairedPageLocators.NORMAL_MODE_BUTTON)
        normal_mode_button.click()
        self.url_changed()
        self.should_be_correct_response_status_code()
        vis_mode_button = self.is_visible(*VisuallyImpairedPageLocators.VIS_MODE_BUTTON)
        assert vis_mode_button, "Did not switch back to normal mode"


        
