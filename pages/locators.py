from selenium.webdriver.common.by import By

class BasePageLocators():
    LANGUAGE_BAR = (By.XPATH, "/html/body/iframe") 
    LANGUAGE_BUTTON = (By.XPATH, "/html/body/div[2]/div/div[1]/div[1]")
    LETTER_BUTTON = (By.XPATH, '//*[@id="messrek"]')
    NORMAL_MODE_BUTTON = (By.XPATH, "//*[@id='header']/p/a")
    REGISTER_BUTTON = (By.XPATH, "/html/body/div[2]/div/div[1]/div[2]/table/tbody/tr/td[2]/a")
    SEARCH_BUTTON = (By.XPATH, "/html/body/div[2]/div/div[3]/div/form/div/input[4]")
    SEARCH_STRING = (By.XPATH, "//*[@id='story']")
    VIS_MODE_BUTTON = (By.XPATH, "/html/body/div[2]/div/div[3]/p/a")

class MainPageLocators():
    LANGUAGE_BAR = (By.XPATH, "/html/body/iframe") 
    LANGUAGE_BUTTON = (By.XPATH, "/html/body/div[2]/div/div[1]/div[1]")
    SEARCH_BAR_INPUT = (By.XPATH, "//*[@id='searchinput']")
    SEARCH_RESULT_MESSAGE = (By.XPATH, "//*[@id='dle-content']/table[1]/tbody/tr/td/div[2]/span")
    
class VisuallyImpairedPageLocators():
    VIS_MODE_BUTTON = (By.XPATH, "/html/body/div[2]/div/div[3]/p/a")
    NORMAL_MODE_BUTTON = (By.XPATH, "//*[@id='header']/p/a")
    SEARCH_BUTTON = (By.XPATH, "//*[@id='out']/div[1]/p[1]/a")
    START_SEARCH_BUTTON = (By.XPATH, "//*[@id='dosearch']")
    SEARCH_STRING = (By.XPATH, "//*[@id='searchinput']")
    SEARCH_BAR_INPUT = (By.XPATH, "//*[@id='searchinput']")
    SEARCH_RESULT_MESSAGE = (By.XPATH, "//*[@id='dle-content']/div[3]")

class RegisterPageLocators():
    ACCEPT_RULES_BUTTON = (By.XPATH, '//*[@id="registration"]/input[1]')
    RULES_FORM = (By.XPATH, '//*[@id="dle-content"]') 
    REGISTER_FORM = (By.XPATH, '//*[@id="registration"]')
    REGISTER_LOGIN_FROM = (By.XPATH, '//*[@id="name"]')
    REGISTER_PASSWORD_FROM = (By.XPATH, '//*[@id="registration"]/table/tbody/tr[2]/td/table/tbody/tr[2]/td[2]/input')
    REGISTER_PASSWORD_REPEAT_FROM = (By.XPATH, '//*[@id="registration"]/table/tbody/tr[2]/td/table/tbody/tr[3]/td[2]/input')
    REGISTER_EMAIL_FORM = (By.XPATH, '//*[@id="registration"]/table/tbody/tr[2]/td/table/tbody/tr[4]/td[2]/input')
    SEND_BUTTON = (By.XPATH, '//*[@id="registration"]/table/tbody/tr[2]/td/table/tbody/tr[6]/td[2]/div/input')

class AppealPageLocators():
    ACCEPT_RULES_BUTTON = (By.XPATH, '//*[@id="toggle_rules"]')
    APPEAL_RULES_FORM = (By.XPATH, '//*[@id="askModal"]/div/div')
    LETTER_BUTTON = (By.XPATH, '//*[@id="ask"]')
    ASK_FORM = (By.XPATH, '//*[@id="askModal"]/div/div/div[2]/div')
    ASK_FORM_NAME = (By.XPATH, '//*[@id="askform"]/table/tbody/tr[1]/td[2]/input')
    ASK_FORM_TELEPHONE = (By.XPATH, '//*[@id="id_phone"]')
    ASK_FORM_EMAIL = (By.XPATH, '//*[@id="email"]')
    ASK_FORM_ADDRESS = (By.XPATH, '//*[@id="askform"]/table/tbody/tr[4]/td[2]/input')
    ASK_FORM_ADDRESSEE = (By.XPATH, '//*[@id="askform"]/table/tbody/tr[5]/td[2]/div/a')
    ASK_FORM_ADDRESSEE_ITEM = (By.XPATH, '//*[@id="askform"]/table/tbody/tr[5]/td[2]/div/div/ul/li[1]')
    ASK_FORM_TYPE = (By.XPATH, '//*[@id="askform"]/table/tbody/tr[6]/td[2]/select')
    ASK_FORM_TYPE_ITEM = (By.XPATH, '//*[@id="askform"]/table/tbody/tr[6]/td[2]/select/option[2]')
    ASK_FORM_TOPIC = (By.XPATH, '//*[@id="askform"]/table/tbody/tr[7]/td[2]/select')
    ASK_FORM_TOPIC_ITEM = (By.XPATH, '//*[@id="askform"]/table/tbody/tr[7]/td[2]/select/option[2]')
    ASK_FORM_WHO = (By.XPATH, '//*[@id="askform"]/table/tbody/tr[8]/td[2]/select')
    ASK_FORM_WHO_ITEM = (By.XPATH, '//*[@id="askform"]/table/tbody/tr[8]/td[2]/select/option[2]')
    ASK_FORM_TITLE = (By.XPATH, '//*[@id="askform"]/table/tbody/tr[9]/td[2]/input')
    ASK_FORM_QUESTION = (By.XPATH, '//*[@id="question_original"]')
    ASK_FORM_ATTACH = (By.XPATH, '//*[@id="file"]')
    ASK_FORM_AGREE_NAME = (By.XPATH, '//*[@id="showfio"]')
    ASK_FORM_AGREE_DATA = (By.XPATH, '//*[@id="person"]')
    ASK_FORM_SEND_ANSWER = (By.XPATH, '//*[@id="send_post"]')


