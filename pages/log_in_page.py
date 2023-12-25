from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page



class LogInPage(Page):
    EMAIL_FIELD = (By.ID,'email-2')
    PASSWORD_FIELD = (By.ID,'field')
    LOGIN_BTN = (By.CSS_SELECTOR, '.login-button.w-button')



    def open_login_page(self):
        self.open_url('https://soft.reelly.io/sign-in')
        sleep(5)

    def input_email(self):
        self.input('ezenwitte@gmail.com', *self.EMAIL_FIELD)

    def input_password(self):
        self.input('Ugo1grace2$', *self.PASSWORD_FIELD)

    def click_continue_btn(self):
        self.wait_for_element_click(*self.LOGIN_BTN)
        #self.click(*self.LOGIN_BTN)




