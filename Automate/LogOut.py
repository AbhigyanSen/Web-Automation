import re
from playwright.sync_api import Playwright, sync_playwright, expect
import time


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://dcs.myadrenalin.com/AdrenalinMax/#/")
    page.locator("#txtID").fill("11003")
    page.locator("#txtID").press("Tab")
    time.sleep(3)
    page.locator("#txtPwd").fill("pu55le")
    time.sleep(3)
    page.locator("#lblLogin").click()
    time.sleep(3)
    page.get_by_title("Signout/Exit").locator("a").click()
    time.sleep(3)
    page.get_by_role("button", name="Sign Me Out").click()
    time.sleep(3)
    page.get_by_role("button", name="OK").click()
    time.sleep(3)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)