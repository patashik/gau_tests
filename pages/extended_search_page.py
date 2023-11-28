from .base_page import BasePage
from .locators import ExtendedSearchPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import time
import allpairspy
from allpairspy import AllPairs

class ExtendedSearchPage(BasePage):
    def clear_search_request(self):
        clear_button = self.is_clickable(*ExtendedSearchPageLocators.CLEAR_BUTTON)
        clear_button.click()

    def fill_all_pairs_form(self, where, comment, date, period, sortby, sort_order, section):
        where_item = self.is_clickable(By.XPATH, f'//*[@id="titleonly"]/option[{where}]')
        where_item.click()
        comments_rule_item = self.is_clickable(By.XPATH, f'//*[@id="replyless"]/option[{comment}]')
        comments_rule_item.click()
        date_item = self.is_clickable(By.XPATH, f'//*[@id="searchdate"]/option[{date}]')
        date_item.click()
        period_item = self.is_clickable(By.XPATH, f'//*[@id="beforeafter"]/option[{period}]')
        period_item.click()
        sort_by_item = self.is_clickable(By.XPATH, f'//*[@id="sortby"]/option[{sortby}]')
        sort_by_item.click()
        sort_order_item = self.is_clickable(By.XPATH, f'//*[@id="resorder"]/option[{sort_order}]')
        sort_order_item.click()
        section_item = self.is_clickable(By.XPATH, f'//*[@id="fullsearch"]/table/tbody/tr/td/div/table/tbody/tr[2]/td[2]/fieldset/div/div/select/option[{section}]')
        section_item.click()

    def should_be_extended_search_form(self):
        extended_search_form = self.is_visible(*ExtendedSearchPageLocators.EXTENDED_SEARCH_FORM)
        assert extended_search_form, 'No extended search form'
    
    def start_extended_search(self, where, comment, date, period, sortby, sort_order, section):
        self.fill_all_pairs_form(where, comment, date, period, sortby, sort_order, section)
        start_search_button = self.is_clickable(*ExtendedSearchPageLocators.START_SEARCH_BUTTON)
        start_search_button.click()