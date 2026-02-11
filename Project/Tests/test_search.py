import pytest
from time import sleep
from playwright.sync_api import sync_playwright

def test_search_product():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://trytestingthis.netlify.app")

        page.get_by_text("Your Sample Alert Button").click()
        browser.close()
    