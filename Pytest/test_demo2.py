import pytest
from Pytest.BaseClass import BaseClass
# @pytest.mark.xfail
def test_second_Greet_creditcard(BaseClass):
    msg = "Hello"
    # assert msg == "Hi", "Test Failed because stpyrings do not match"




# @pytest.mark.smoke
# @pytest.mark.skip
# def test_secondCreditCard():
#     a = 4
#     b = 6
#     assert a + 2 == 6, "Addition dosent match"
#
#
# def setup():
#     print("I will be executed first")
#
#
# def test_fixtureDemo():
#     print("I will execute steps in fixture Demo method")
