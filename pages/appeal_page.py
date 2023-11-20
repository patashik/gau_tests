from .base_page import BasePage
from .locators import AppealPageLocators
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
import time

class AppealPage(BasePage):
    def create_new_appeal(self, input, phone, file_path):
        self.open_ask_form()
        self.fill_ask_form(input, phone, file_path)

    def fill_ask_form(self, input, phone, file_path):
        ask_form_name = self.is_clickable(*AppealPageLocators.ASK_FORM_NAME)
        ask_form_name.send_keys(input)
        ask_form_telephone = self.is_clickable(*AppealPageLocators.ASK_FORM_TELEPHONE)
        ask_form_telephone.send_keys(phone)
        ask_form_email = self.is_clickable(*AppealPageLocators.ASK_FORM_EMAIL)
        ask_form_email.send_keys(input)
        ask_form_address = self.is_clickable(*AppealPageLocators.ASK_FORM_ADDRESS)
        ask_form_address.send_keys(input)
        ask_form_addressee = self.is_clickable(*AppealPageLocators.ASK_FORM_ADDRESSEE)
        ask_form_addressee.click()
        ask_form_addressee_item = self.is_clickable(*AppealPageLocators.ASK_FORM_ADDRESSEE_ITEM)
        ask_form_addressee_item.click()
        ask_form_type = self.is_clickable(*AppealPageLocators.ASK_FORM_TYPE)
        ask_form_type.click()
        ask_form_type_item = self.is_clickable(*AppealPageLocators.ASK_FORM_TYPE_ITEM)
        ask_form_type_item.click()
        ask_form_topic = self.is_clickable(*AppealPageLocators.ASK_FORM_TOPIC)
        ask_form_topic.click()
        ask_form_topic_item = self.is_clickable(*AppealPageLocators.ASK_FORM_TOPIC_ITEM)
        ask_form_who = self.is_clickable(*AppealPageLocators.ASK_FORM_WHO)
        ask_form_who.click()
        ask_form_who_item = self.is_clickable(*AppealPageLocators.ASK_FORM_WHO_ITEM)
        ask_form_who_item.click()
        ask_form_title = self.is_clickable(*AppealPageLocators.ASK_FORM_TITLE)
        ask_form_title.send_keys(input)
        ask_form_question = self.is_clickable(*AppealPageLocators.ASK_FORM_QUESTION)
        ask_form_question.send_keys(input)
        ask_form_attach = self.is_clickable(*AppealPageLocators.ASK_FORM_ATTACH)
        ask_form_attach.send_keys(file_path)
        ask_form_agree_name = self.is_clickable(*AppealPageLocators.ASK_FORM_AGREE_NAME)
        ask_form_agree_name.click()
        ask_form_agree_data = self.is_clickable(*AppealPageLocators.ASK_FORM_AGREE_DATA)
        ask_form_agree_data.click()
        ask_form_send_answer = self.is_clickable(*AppealPageLocators.ASK_FORM_SEND_ANSWER)
        ask_form_send_answer.click()
        #assert input in ask_form_name.text, 'Name empty'
        #assert phone in ask_form_telephone.text, 'Telephone empty'
        #assert input in ask_form_email.text, 'Email empty'
        #assert input in ask_form_address.text, 'Address empty'
        #assert input in ask_form_title.text, 'Title empty'
        #assert input in ask_form_question, 'Question empty'
        #assert file_path in ask_form_attach.text, 'File not attached'
        #assert ask_form_addressee_item.text in ask_form_addressee.text, 'Addressee not correct'
        #assert ask_form_topic_item.text in ask_form_topic_item, 'Topic not correct'
        #assert ask_form_who_item.text in ask_form_who.text, 'Sender not correct'
    
    def open_ask_form(self):
        letter_button = self.is_clickable(*AppealPageLocators.LETTER_BUTTON)
        letter_button.click()
        appeal_rules_form = self.is_visible(*AppealPageLocators.APPEAL_RULES_FORM)
        #self.browser.switch_to.alert(appeal_rules_form)
        accept_rules_button = self.is_clickable(*AppealPageLocators.ACCEPT_RULES_BUTTON)
        accept_rules_button.click()
        ask_form = self.is_visible(*AppealPageLocators.ASK_FORM)
        assert ask_form, 'Did not open ask form'



