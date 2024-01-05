from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page




class MainPage(Page):
    OFF_PLAN = (By.CSS_SELECTOR, "address [href='/off-plan']")
    OFF_PLAN_MENU_MOBILE = (By.CSS_SELECTOR, 'div[wized="mobileMenuForVerifiedUsers"] a.menu-link[href="/off-plan"]')

    def open_main_page(self):
        self.open_url('https://soft.reelly.io/')
        sleep(4)

    def click_off_plan_menu(self):
        self.wait_for_element_click(*self.OFF_PLAN)

    def click_off_plan_menu_mobile(self):
        self.wait_for_element_click(*self.OFF_PLAN_MENU_MOBILE)


