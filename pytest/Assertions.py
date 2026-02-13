from playwright.sync_api import sync_playwright,expect

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    
    page = browser.new_page()
    
    page.goto("https://google.com")
    
    expect(page).to_have_url("https://www.google.com/")
    expect(page).to_have_title("Google")