import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://dcs.myadrenalin.com/AdrenalinMAX/#/")
    page.locator("#txtID").click()
    page.locator("#txtID").fill("11003")
    time.sleep(3)
    page.locator("#txtPwd").click()
    page.locator("#txtPwd").fill("pu55le")
    time.sleep(3)
    page.locator("#lblLogin").click()
    time.sleep(3)
    page.get_by_role("button", name="OK").click()
    time.sleep(3)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)