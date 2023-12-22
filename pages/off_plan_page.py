from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page




class OffPlanPage(Page):
    RIT_PAG_OPENS = (By.CSS_SELECTOR, 'div.page-title')
    STATUS_WITH_NL = (By.CSS_SELECTOR, '.filter-button.w-inline-block')
    NEWLY_LUNCH = (By.CSS_SELECTOR, "[wized='priorityStatusNewlyLaunched']")
    PDT_NEWLY_LUNCH = (By.CSS_SELECTOR, "[wized='projectStatus']")


    def Verify_right_page_opens(self):
        expected = 'Total projects'
        actual = self.find_element(*self.RIT_PAG_OPENS).text
        assert expected == actual, f'Expected {expected} did not match actual {actual}'

        sleep(4)

    def filter_sale_status_with_Newly_Lunch(self):
        self.wait_for_element_click(*self.STATUS_WITH_NL)
        sleep(3)

    def click_Newly_Lunch(self):
        self.click(*self.NEWLY_LUNCH)

    def Verify_product_contains_Newly_Launch_tag(self, expected_name):
        self.verify_text(expected_name, *self.PDT_NEWLY_LUNCH)






