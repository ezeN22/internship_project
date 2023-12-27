from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from support.logger import logger




class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)


    def open_url(self, url):
        self.driver.get(url)
        #logger.info(f'Opening url {url}')

    def click(self, *locator):
        self.driver.find_element(*locator).click()
         #logger.info(f'Clicking on {locator}')


    def find_element(self, *locator):
        #logger.info(f'Searching for element {locator}')
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        #logger.info(f'Searching for elements {locator}')
        return self.driver.find_elements(*locator)

    def input(self, text, *locator):
        #logger.info(f"Inputting text '{text}' for element {locator}")
        self.driver.find_element(*locator).send_keys(text)

    def wait_for_url_to_change(self, initial_url):
        self.wait.until(
            EC.url_changes(initial_url),
            message=f'Url {initial_url} did not change'
        )

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, \
            f"Expected text '{expected_text}' not in actual '{actual_text}'"

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text == actual_text, \
            f"Expected text '{expected_text}' did not match actual '{actual_text}'"

    def verify_partial_url(self, expected_partial_url):
        self.wait.until(
            EC.url_contains(expected_partial_url),
            message=f'Expected {expected_partial_url} not in url'
        )

    def wait_for_element_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by {locator} not clickable'
        ).click()

    def wait_for_text_present(self, *locator, text):
        self.wait.until(
            EC.text_to_be_present_in_element(locator, text),
            message=f'The text "{text}" did not appear.'
        )

    def wait_for_element_disappear(self, *locator):
        self.wait.until(
            EC.invisibility_of_element_located(locator),
            message=f'The element did not appear locator: {locator}'
        )



