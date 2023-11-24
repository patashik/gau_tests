from .base_page import BasePage
from .locators import ExtendedSearchPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import time
import allpairspy
from allpairspy import AllPairs

class ExtendedSearchPage(BasePage):
    def fill_all_pairs_form(self, where, comment, date, period, sortby, sort_order, section):
        where = self.is_clickable(*ExtendedSearchPageLocators.WHERE)
        where.click()
        time.sleep(3)
        where_item = self.is_presented(By.XPATH, f'//*[@id="titleonly"]/option[{where}]')
        where_item.click()
        comments_rule = self.is_clickable(*ExtendedSearchPageLocators.COMMENTS_RULE)
        comments_rule.click()
        time.sleep(3)
        comments_rule_item = self.is_clickable(By.XPATH, f'//*[@id="replyless"]/option[{comment}]')
        comments_rule_item.click()
        date = self.is_clickable(*ExtendedSearchPageLocators.DATE)
        date.click()
        time.sleep(3)
        date_item = self.is_clickable(By.XPATH, f'//*[@id="searchdate"]/option[{date}]')
        date_item.click()
        period = self.is_clickable(*ExtendedSearchPageLocators.PERIOD)
        period.click()
        time.sleep(3)
        period_item = self.is_clickable(By.XPATH, f'//*[@id="beforeafter"]/option[{period}]')
        period_item.click()
        sort_by = self.is_clickable(*ExtendedSearchPageLocators.SORT_BY)
        sort_by.click()
        time.sleep(3)
        sort_by_item = self.is_clickable(By.XPATH, f'//*[@id="sortby"]/option[{sortby}]')
        sort_by_item.click()
        sort_order = self.is_clickable(*ExtendedSearchPageLocators.SORT_ORDER)
        sort_order.click()
        time.sleep(3)
        sort_order_item = self.is_clickable(By.XPATH, f'//*[@id="resorder"]/option[{sort_order}]')
        sort_order_item.click()
        section_item = self.is_clickable(By.XPATH, f'//*[@id="fullsearch"]/table/tbody/tr/td/div/table/tbody/tr[2]/td[2]/fieldset/div/div/select/option[{section}]')
        section_item.click()
    
    def fill_single_extended_search_form(self):
        where_item = self.is_clickable(By.XPATH, f'//*[@id="titleonly"]/option[1]')
        where_item.click()
        comments_rule_item = self.is_clickable(By.XPATH, f'//*[@id="replyless"]/option[1]')
        comments_rule_item.click()
        date_item = self.is_clickable(By.XPATH, f'//*[@id="searchdate"]/option[1]')
        date_item.click()
        period_item = self.is_clickable(By.XPATH, f'//*[@id="beforeafter"]/option[1]')
        period_item.click()
        sort_by_item = self.is_clickable(By.XPATH, f'//*[@id="sortby"]/option[1]')
        sort_order_item = self.is_clickable(By.XPATH, f'//*[@id="resorder"]/option[1]')
        sort_order_item.click()
        section_item = self.is_clickable(By.XPATH, f'//*[@id="fullsearch"]/table/tbody/tr/td/div/table/tbody/tr[2]/td[2]/fieldset/div/div/select/option[1]')
        section_item.click()

    def should_be_extended_search_form(self):
        extended_search_form = self.is_visible(*ExtendedSearchPageLocators.EXTENDED_SEARCH_FORM)
        assert extended_search_form, 'No extended search form'
    
    def start_extended_search(self, where, comment, date, period, sortby, sort_order, section):
        self.fill_all_pairs_form(where, comment, date, period, sortby, sort_order, section)
        start_search_button = self.is_clickable(*ExtendedSearchPageLocators.START_SEARCH_BUTTON)
        start_search_button.click()
    
    def start_single_extended_search(self):
        self.fill_single_extended_search_form()
        start_search_button = self.is_clickable(*ExtendedSearchPageLocators.START_SEARCH_BUTTON)
        start_search_button.click()