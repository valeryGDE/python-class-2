import pytest
from selene import browser, by, be, have


@pytest.fixture()
def precondition():
    browser.open('https://google.com')
    browser.driver.set_window_size(1280, 720)
    if browser.element(by.text('Accept all')).matching(be.visible):
        browser.element(by.text('Accept all')).click()
    yield
    browser.driver.quit()


def test_successful_google_search(precondition):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_blank_google_search(precondition):
    search = 'ettedwwefdqwfqestcteactce12312wwdwwdw3'
    browser.element('[name="q"]').should(be.blank).type(search).press_enter()
    browser.element('//p[.//em[contains(text(), "%s")]]' % search).should(have.text('- did not match any documents.'))
