from selene import Browser, Config
import pytest
from selene.support import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Remote


@pytest.fixture(scope='function', autouse=True)
def browser_config(request):

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {"enableVNC": True, "enableVideo": True},
    }
    options.capabilities.update(selenoid_capabilities)

    # Использовать класс Remote из модуля selenium.webdriver, а не selene.support.webdriver
    driver = Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options,
    )

    browser = Browser(Config(driver))
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1440
    browser.config.window_height = 900

    yield

    browser.quit()
