 #Created by 18327 at 12/19/2023
Feature: Filter by sale status

  Scenario: User can filter by sale status Newly Launch
    Given Open the main page
    When Log in to the page
    When Click on “off plan” at the left side menu
    Then Verify the right page opens
    Then Filter by sale status of Newly Launched
    Then Verify each product contains the newly launched tag

