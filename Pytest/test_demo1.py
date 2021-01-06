from builtins import print
from BaseClass import BaseClass
import pytest


@pytest.mark.smoke
def test_firstProgram(BaseClass):
    print("Hello")


def test_crossBrowser(crossBrowser):
    print("crossBrowser")
