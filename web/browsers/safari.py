from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from web.browsers import WebBrowser
from web.driver.web_driver import WebDriverOf
from web.driver.driver import Driver


class Safari(WebBrowser):
    """Representation of a safari web browser."""

    def __init__(self) -> None:
        self._safari: WebDriver = webdriver.Safari()

    def driver(self) -> Driver:
        return WebDriverOf(self._safari)

    def close(self) -> None:
        self._safari.close()

    def name(self) -> str:
        return 'Safari'