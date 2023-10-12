from playwright.sync_api import Playwright, sync_playwright, expect

# from playwright.sync_api import Playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=2000)
    context = browser.new_context()
    context2 = browser.new_context()

    # Open new page
    page = context.new_page()
    page.goto("https://ndrrma.yilab.org.np")

    page2 = context2.new_page()
    page2.goto("https://ndrrma.yilab.org.np/en/rastra-parisad", timeout=60000)

    page.wait_for_timeout(3000)

#increase wait_for_timeout to delay

    context.close()
    browser.close()

with sync_playwright() as playwright:
        run(playwright)
