from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page




class OffPlanPage(Page):
    RIT_PAG_OPENS = (By.CSS_SELECTOR, 'div.page-title')
    STATUS_WITH_NL = (By.CSS_SELECTOR, '.filter-button.w-inline-block')
    NEWLY_LUNCH = (By.XPATH, "//div[@class='filters-tags']//div[contains(text(), 'Newly Launched')]")
    PDT_NEWLY_LUNCH = (By.CSS_SELECTOR, "[wized='projectStatus']")



    def Verify_right_page_opens(self):
        expected = 'Total projects'
        actual = self.find_element(*self.RIT_PAG_OPENS).text
        assert expected == actual, f'Expected {expected} did not match actual {actual}'
        sleep(4)

    def filter_sale_status_with_newly_lunched(self):
        self.wait_for_element_click(*self.STATUS_WITH_NL)


    def click_Newly_Lunched(self):
        self.click(*self.NEWLY_LUNCH)
        sleep(4)


    def Verify_product_contains_Newly_Launched_tag(self, expected_name):
        tags = self.find_elements(*self.PDT_NEWLY_LUNCH)
        for tag in tags:
            assert expected_name in tag.text, f'Expected {expected_name} not in {tag.text}'
            sleep(2)








