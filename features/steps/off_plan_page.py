from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep



@then('Verify the right page opens')
def Verify_right_page_opens(context):
    context.app.off_plan_page.Verify_right_page_opens()


@then('Filter by sale status of Newly Launch')
def filter_sale_status_with_Newly_Lunch(context):
    context.app.off_plan_page.filter_sale_status_with_Newly_Lunch()
    context.app.off_plan_page.click_Newly_Lunch()



@then('click on Newly Lunch')
def click_Newly_Lunch(context):
    context.app.off_plan_page.click_Newly_Lunch()

@then('Verify each product contains the Newly Launch tag')
def Verify_product_contains_Newly_Launch_tag(context):
    context.app.off_plan_page.Verify_product_contains_Newly_Launch_tag('Newly Launch')







