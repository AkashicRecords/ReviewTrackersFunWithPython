import pytest
from demo.locators.register import RegistrationPage


@pytest.fixture(scope="module")
def register_page_locator() -> RegistrationPage:
    return RegistrationPage()
