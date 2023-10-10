def test_right_click(page: Page) -> None:
    page.goto("https://ndrrma.yilab.org.np/")
    context_area = page.locator("#hot-spot")

    context_area.click(button="right")

#Run this in 4000 ms delay by    pytest -s --headed <.\FileCurrentPath\FileName.py> --slowmo=4000
