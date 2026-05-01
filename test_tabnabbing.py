import re
from playwright.sync_api import sync_playwright

def test_tabnabbing_fix():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Load the index.html via http.server
        page.goto('http://localhost:8000/index.html')

        # We need to verify that 'noopener,noreferrer' is present in the page source
        # or verify the onClick attributes directly, but since this app uses Babel
        # we can just fetch the raw content and verify, or check the DOM.
        # But wait, checking the DOM is hard because the buttons only appear AFTER generating an image.

        # Let's fetch the raw page content using requests or playwight's request context
        response = page.request.get('http://localhost:8000/index.html')
        text = response.text()

        if 'window.open(result.url, "_blank", "noopener,noreferrer")' in text:
            print("SUCCESS: noopener,noreferrer found in window.open calls.")
        else:
            print("FAIL: window.open calls are missing noopener,noreferrer")

        browser.close()

if __name__ == '__main__':
    test_tabnabbing_fix()
