from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.trendyol.com")
    page.wait_for_timeout(60000)  # manuel login
    context.storage_state(path="cookies.json")
    browser.close()