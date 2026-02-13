#Importing sync playwright api
from playwright.sync_api import sync_playwright

# Start Playwright
with sync_playwright() as p:
    
    # Launch Chromium browser (visible + slowed down for debugging)
    browser = p.chromium.launch(headless=False, slow_mo=1000)
    
    # Open a new browser tab
    page = browser.new_page()
    
    # Navigate to website
    page.goto("https://trytestingthis.netlify.app")
    
    # Handle JavaScript alert popup
    
    #Lambda Function (Shorter version of normal function)
    # page.on("dialog", lambda dialog: (
    #     print("Alert message:", dialog.message),  # Print alert text
    #     dialog.accept()  # Click OK on alert
    # ))
    
    def handle_dialog(dialog):
        print("Alert message:", dialog.message)
        dialog.accept()
    #page on is an event listener
    page.on("dialog", handle_dialog)

    # Locate button by its ARIA role and visible name, then click it
    page.get_by_role("button", name=" Your Sample Alert Button!").click()
    
    #Get by label
    page.get_by_label("First name:").type("Ansh")
    page.get_by_label("Last name:").type("Arora")
    
    page.get_by_role("radio",name="Male",exact=True).check()
    
    page.get_by_label("Option 1").check()
    
    #locator.check()
    page.locator("input[name='option1']").uncheck()
    page.locator("input[name='option2']").check()
    page.locator("input[name='option3']").check()
    
    #locator.uncheck()
    page.locator("input[name='option2']").uncheck()
    
    #locator.focus()
    page.locator("input[name='Options']").focus()
    
    #locator.select_option()
    page.locator("#option").select_option("Option 2")
    
    #locator.get_by_text()
    page.get_by_text(" This is your Sample Tooltip Option").hover()
    
    #locator.drage_drop
    page.drag_and_drop("#drag1","#div1")
    
    page.wait_for_timeout(3000)
    
    # Close browser
    browser.close()