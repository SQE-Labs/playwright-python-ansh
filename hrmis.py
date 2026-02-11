from time import sleep
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    
    browser = p.chromium.launch(headless=False,slow_mo=100)
    
    page = browser.new_page()
    
    page.goto("https://topuptalent.com")
    
    page.get_by_placeholder("Email Address").type("vishal.thakur1@caeliusconsulting.com")
    page.get_by_placeholder("Enter Password").type("Test@123")
    
    page.locator("#submitButton").click()
    
    page.get_by_role("link",name="Raise Concern").click()
    sleep(2)