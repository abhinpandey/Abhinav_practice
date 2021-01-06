from selenium import webdriver

from Pytest.conftest import crossBrowser


def test_crossBrowser(crossBrowser):
    print(crossBrowser)
