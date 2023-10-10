from playwright.sync_api import Playwright, sync_playwright, expect, Page

def test_trackNetworkEvent(page: Page) -> None:
    page.goto("https://ndrrma.yilab.org.np")
    #page.locator("#username").fill("someName")
    #page.locator("#password").fill("somePassword")
    #page.get_by_role("button", name= "Login").click()
    page.wait_for_timeout(2000)

    with page.expect_request("**/secure") as req:
        page.goto("https://ndrrma.yilab.org.np")
        #page.locator("#username").fill("someName")
        #page.locator("#password").fill("somePassword")
        #page.get_by_role("button", name= "Login").click()
        page.wait_for_timeout(2000)

print(req.value.url)
print(req.value.method)
print(req.value.redirected_from)
print(req.value.redirected_to)
print(req.value.all_headers())
