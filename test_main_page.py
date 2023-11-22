import pytest
import time
import os
from .pages.base_page import BasePage
from .pages.register_page import RegisterPage
from .pages.visually_impaired_page import VisuallyImpairedPage
from .pages.appeal_page import AppealPage
import allure
import allpairspy
from allpairspy import AllPairs

@pytest.mark.chrome
@allure.epic("Chrome tests for Main page")
@allure.parent_suite("Chrome tests for Main page")
@allure.feature("Main page menu")
@allure.suite("Main page menu")
class TestHappyPathChrome():
    @pytest.mark.reg
    @allure.story("User registration")
    @allure.sub_suite("User registration")
    @allure.title("Register new user")
    def test_register_new_user(self, browser_chrome):
        link = "http://academy21.ru/" 
        login = "testik"
        email = "test"
        password = "test"
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser_chrome, link)
            main_page.open()
            main_page.should_be_correct_response_status_code()
        with allure.step("Step 2: go to register page"):
            main_page.go_to_register_page()
            register_page = RegisterPage(browser_chrome, browser_chrome.current_url)
        with allure.step("Step 3: register new user"):
            register_page.register_new_user(login, email, password)

    @pytest.mark.login
    @allure.story("User login")
    @allure.sub_suite("User login")
    @allure.title("Log in, go to profile, log out")
    def test_login_go_to_profile_logout(self, browser_chrome):
        link = "http://academy21.ru/" 
        name = "test"
        password = "test"
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser_chrome, link)
            main_page.open()
            main_page.should_be_correct_response_status_code()
        with allure.step("Step 2: log in"):
            main_page.log_in(name, password)
        with allure.step("Step 3: go to user profile"):
            main_page.go_to_user_profile(name)
        with allure.step("Step 4: log out"):
            main_page.log_out()
            
    @pytest.mark.search
    @allure.story("Search")
    @allure.sub_suite("Search")
    @allure.title("Search by string and button")
    def test_search_by_string_and_button(self, browser_chrome):
        search_request = "ректор"
        link = "http://academy21.ru/" 
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser_chrome, link)
            main_page.open()
            main_page.should_be_correct_response_status_code()
        with allure.step("Step 2: insert text in string and activate search"):
            browser_chrome.implicitly_wait(5) 
            main_page.start_search_by_button(search_request)
        with allure.step("Step 3: list search results"):
            main_page.should_be_search_request_in_search_string(search_request)
        
    @pytest.mark.search
    @allure.story("Search")
    @allure.sub_suite("Search")
    @allure.title("Search by string and enter")
    def test_search_by_string_and_enter(self, browser_chrome):
        search_request = "ректор"
        link = "http://academy21.ru/" 
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser_chrome, link)
            main_page.open()
            main_page.should_be_correct_response_status_code()
        with allure.step("Step 2: insert text in string and activate search"):
            browser_chrome.implicitly_wait(5) 
            main_page.start_search_by_enter(search_request)
        with allure.step("Step 3: list search results"):
            main_page.should_be_search_request_in_search_string(search_request)

    @pytest.mark.vis
    @allure.story("Search")
    @allure.sub_suite("Search")
    @allure.title("Search by button in visually impaired mode")
    def test_search_by_button_in_visually_impaired_mode(self, browser_chrome):
        search_request = "ректор"
        link = "http://academy21.ru/" 
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser_chrome, link)
            main_page.open()
            main_page.should_be_correct_response_status_code()
        with allure.step("Step 2: switch to visually impaired mode"):
            browser_chrome.implicitly_wait(5)
            main_page.switch_to_visually_impaired_mode() 
        with allure.step("Step 3: insert text and activate search"):
            visually_impaired_page = VisuallyImpairedPage(browser_chrome, browser_chrome.current_url)
            visually_impaired_page.start_search_by_button(search_request)
        with allure.step("Step 3: list search results"):
            visually_impaired_page.should_be_search_request_in_search_string(search_request)
            visually_impaired_page.should_be_results_message()
    
    @pytest.mark.vis
    @allure.story("Search")
    @allure.sub_suite("Search")
    @allure.title("Search by enter in visually impaired mode")
    def test_search_by_enter_in_visually_impaired_mode(self, browser_chrome):
        search_request = "ректор"
        link = "http://academy21.ru/" 
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser_chrome, link)
            main_page.open()
            main_page.should_be_correct_response_status_code()
        with allure.step("Step 2: switch to visually impaired mode"):
            browser_chrome.implicitly_wait(5)
            main_page.switch_to_visually_impaired_mode() 
        with allure.step("Step 3: insert text and activate search"):
            visually_impaired_page = VisuallyImpairedPage(browser_chrome, browser_chrome.current_url)
            visually_impaired_page.start_search_by_enter(search_request)
        with allure.step("Step 4: list search results"):
            visually_impaired_page.should_be_search_request_in_search_string(search_request)
            visually_impaired_page.should_be_results_message()
    
    @pytest.mark.back
    @allure.story("Search")
    @allure.sub_suite("Search")
    @allure.title("Search by button in visually impaired mode and switch normal mode")
    def test_search_by_button_for_visually_impaired_switch_normal(self, browser_chrome):
        search_request = "ректор"
        link = "http://academy21.ru/" 
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser_chrome, link)
            main_page.open()
            main_page.should_be_correct_response_status_code()
        with allure.step("Step 2: switch to visually impaired mode"):
            browser_chrome.implicitly_wait(5)
            main_page.switch_to_visually_impaired_mode() 
        with allure.step("Step 3: insert text and activate search"):
            visually_impaired_page = VisuallyImpairedPage(browser_chrome, browser_chrome.current_url)
            visually_impaired_page.start_search_by_button(search_request)
        with allure.step("Step 4: list search results"):
            visually_impaired_page.should_be_search_request_in_search_string(search_request)
            visually_impaired_page.should_be_results_message()
        with allure.step("Step 5: switch to normal mode"):
            visually_impaired_page.switch_to_normal_mode()
            visually_impaired_page.should_be_correct_response_status_code()

    @pytest.mark.tatar
    @allure.story("Search")
    @allure.sub_suite("Search")
    @allure.title("Change language and search by string and button")
    def test_change_language_and_search_by_string_and_button(self, browser_chrome):
        language = "татарский"
        search_request = "ректор"
        link = "http://academy21.ru/" 
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser_chrome, link)
            main_page.open()
            main_page.should_be_correct_response_status_code()
        with allure.step("Step 2: change language"):
            main_page.change_language(language)
        with allure.step("Step 3: insert text and activate search"):
            main_page.start_search_by_button(search_request)
        with allure.step("Step 4: list search results"):
            main_page.should_be_search_request_in_search_string(search_request)

    @pytest.mark.tatar
    @allure.story("Search")
    @allure.sub_suite("Search")
    @allure.title("Change language and search by string and enter")
    def test_change_language_and_search_by_string_and_enter(self, browser_chrome):
        language = "татарский"
        search_request = "ректор"
        link = "http://academy21.ru/" 
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser_chrome, link)
            main_page.open()
            main_page.should_be_correct_response_status_code()
        with allure.step("Step 2: change language"):
            main_page.change_language(language)
        with allure.step("Step 3: insert text and activate search"):
            main_page.start_search_by_enter(search_request)
        with allure.step("Step 4: go to search result page"):
            main_page.should_be_search_request_in_search_string(search_request)

    @pytest.mark.ask
    @allure.story("Appeal")
    @allure.sub_suite("Appeal")
    @allure.title("Go to appeal page and create single appeal")
    def test_send_new_appeal(self, browser_chrome):
        link = "http://academy21.ru/" 
        input = "test"
        phone = "1111111111"
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'test_data', 'test_image.jpg')
        with allure.step("Step 1: open main page"):
            main_page = BasePage(browser_chrome, link)
            main_page.open()
            main_page.should_be_correct_response_status_code()
        with allure.step("Step 2: go to Appeal page"):
            main_page.go_to_appeal_page()
            appeal_page = AppealPage(browser_chrome, browser_chrome.current_url)
        with allure.step("Step 3: create new appeal"):
            appeal_page.create_single_appeal(input, phone, file_path)
            
    @pytest.mark.allpairs
    @allure.story("Appeal")
    @allure.sub_suite("Appeal")
    @allure.title("Create all combinations of appeal")
    @pytest.mark.parametrize(["addressee_item", "type_item", "topic_item", "who_item"], [
        values for values in AllPairs([
            [1, 2],
            [2, 3],
            [2, 3],
            [2, 3]
        ])
    ])
    def test_send_all_pairs_appeal(self, browser_chrome, addressee_item, type_item, topic_item, who_item):
        link = "http://appeal.academy21.ru/" 
        input = "test"
        phone = "1111111111"
        current_dir = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_dir, 'test_data', 'test_image.jpg')
        with allure.step("Step 1: open appeal page"):
            appeal_page = AppealPage(browser_chrome, link)
            appeal_page.open()
            appeal_page.should_be_correct_response_status_code()
        with allure.step("Step 2: create all combinations of appeal"):
            appeal_page.create_all_pairs_appeal(input, phone, file_path, addressee_item, type_item, topic_item, who_item)