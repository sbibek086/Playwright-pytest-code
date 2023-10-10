import os
from playwright.sync_api import Playwright, sync_playwright, expect, Page

def run(page: Page) -> None:
    app_data_path = os.getenv("LOCALAPPDATA")
    user_data_path = os.path.join(app_data_path, 'Chromium\\User Data\\Default')
    context= playwright.chromium.launch_persistent_context(user_data_path, channel = 'msedge',  headless= False)
    page = context.new_page()
    page.goto("https://ndrrma.yilab.org.np/")
    page.wait_for_timeout(5000)
