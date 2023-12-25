from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep


@given('Open the login page')
def open_login_page(context):
    context.app.login_page.open_login_page()
    sleep(5)


@when('Log in to the page')
def Login_to_page(context):
    context.app.log_in_page.input_email()
    context.app.log_in_page.input_password()
    context.app.log_in_page.click_continue_btn()
    sleep(10)