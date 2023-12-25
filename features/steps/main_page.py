from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given('Open the main page')
def open_main_page(context):
    context.app.main_page.open_main_page()
    sleep(10)


@when('Click on “off plan” at the left side menu')
def click_off_plan_menu(context):
    context.app.main_page.click_off_plan_menu()

