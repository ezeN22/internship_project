from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep



@then('Verify the right page opens')
def Verify_right_page_opens(context):
    context.app.off_plan_page.Verify_right_page_opens()


@then('Filter by sale status of Newly Launched')
def filter_sale_status_with_Newly_Lunched(context):
    context.app.off_plan_page.filter_sale_status_with_newly_lunched()
    context.app.off_plan_page.click_Newly_Lunched()



@then('click on Newly Lunched')
def click_Newly_Lunch(context):
    context.app.off_plan_page.click_Newly_Lunched()

@then('Verify each product contains the Newly Launched tag')
def Verify_product_contains_Newly_Launched_tag(context):
    context.app.off_plan_page.Verify_product_contains_Newly_Launched_tag('Newly Launched')







