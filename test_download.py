from playwright.sync_api import Playwright, sync_playwright, expect, Page

def test_run(page: Page) -> None:
    page.goto("https://ndrrma.yilab.org.np/np/daily-bulletin/1145")
    with page.expect_download() as download_i:
        page.locator("div").click()
    dl = download_i.value

print(dl.path())

page.wait_for_timeout(5000)

#default download downloads in odd locations. to put it in favorable location,

working_dir_path = os.getcwd()

final_path = os.path.join(working_dir_path, "<fileLocation>/<Filename.txt>")

dl.save_as(final_path)
