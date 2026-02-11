import re #re is used regular expression 
from playwright.sync_api import expect #this gives us assertions 

def test_google_search(page):
    page.wait_for_timeout(8000)
    page.goto("http://google.com/ncr")
    
    try:
        page.get_by_role("button",name="Accept all").click(timeout=5000)
    except:
        print("No popup to accept")
        
        
    page.get_by_role("combobox",name="Search").fill("Playwright")
    
    page.keyboard.press("Enter")
    
    expect(page).to_have_title(re.compile("Playwright",re.IGNORECASE))