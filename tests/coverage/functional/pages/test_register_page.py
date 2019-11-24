from tests.coverage.markers import smoke
from demo.input.register import RegisterPageInput
from demo.locators.register import RegistrationPage
from demo.map.handlers import HandlerBy
from demo.pages.register import RegisterPage


@smoke
def test_register_page_register_text(register_page: RegisterPage) -> None:
    assert register_page.register_text().is_displayed()


@smoke
def test_set_first_name(
    register_page: RegisterPage,
    register_page_input: RegisterPageInput,
    register_page_locator: RegistrationPage,
    handler_by: HandlerBy,
) -> None:
    element = register_page.set_first_name(register_page_input)
    assert element.text(handler_by.xpath(), register_page_locator.first_name) == ""


@smoke
def test_registration(register_page: RegisterPage, register_page_input: RegisterPageInput) -> None:
    register_page.set_first_name(register_page_input)
    register_page.set_last_name(register_page_input)
    register_page.set_email(register_page_input)
    register_page.set_phone(register_page_input)
    register_page.set_country(register_page_input)
    register_page.set_user_name(register_page_input)
    register_page.set_password(register_page_input)
    register_page.confirm_password(register_page_input)
    register_page.submit()
    assert register_page.confirm_registration().is_displayed()
