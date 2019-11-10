from functools import lru_cache
from typing import Callable
from lib.browsers import WebBrowser
from lib.driver.driver import Driver
from lib.pages import Page
from lib.map.urls import Url


class BasePage(Page):
    """Represent base page."""

    def __init__(self, browser: WebBrowser, url: Url) -> None:

        @lru_cache(maxsize=128)
        def _driver() -> Driver:
            driver: Driver = browser.driver()
            driver.set_page_load_timeout(10)
            driver.implicitly_wait(10)
            driver.get(url.get())
            return driver

        self._url: Url = url
        self._driver: Callable[..., Driver] = _driver

    def driver(self) -> Driver:
        return self._driver()

    def open(self, url: Url = None) -> None:
        if not url:
            url: Url = self._url
        self._driver().get(url.get())

    def close(self) -> None:
        self._driver().close()
