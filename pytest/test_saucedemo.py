from playwright.sync_api import Page
import pytest

def test_title(page: Page):
    page.goto("https://www.saucedemo.com/")
    assert page.title() == "Swag Labs" 

def test_inventory_sit(page: Page):
    page.goto("https://www.saucedemo.com/inventory.html")
    assert page.inner_text('h3') == "Epic sadface: You can only access '/inventory.html' when you are logged in." 
    
def test_login(page: Page):
    page.goto("https://www.saucedemo.com/")
    
    #Enter details
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    
    #Click login button
    page.locator("#login-button").click()
    assert page.inner_text('span') == "Products"