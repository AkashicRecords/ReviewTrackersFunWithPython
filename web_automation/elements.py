from abc import ABC, abstractmethod
from selenium.webdriver.remote import webelement


class Element(ABC):
    """Abstraction of a web element."""

    @abstractmethod
    def is_displayed(self) -> bool:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass

    @abstractmethod
    def send_keys(self, value: str) -> None:
        pass

    @abstractmethod
    def click(self) -> None:
        pass


class WebElement(Element):
    """Represent concrete web element."""

    def __init__(self, element: webelement.WebElement) -> None:
        self._element = element

    def is_displayed(self) -> bool:
        return self._element.is_displayed()

    def clear(self) -> None:
        self._element.clear()

    def send_keys(self, value: str) -> None:
        self._element.send_keys(value)

    def click(self) -> None:
        self._element.click()
