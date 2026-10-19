# Learning custom markers

import pytest

# @pytest.mark.maths
# def test_addition():
#     cal = 20 + 5
#     expected = 25
#     assert cal == expected , f"The result should be {expected} but we got {cal}"

# @pytest.mark.maths
# def test_sub():
#     cal = 12 - 5
#     expected = 7
#     assert cal == expected , f"The result should be {expected} but we got {cal}"

# @pytest.mark.name
# def test_fname():
#     name = "Vishnu"
#     expected = "Vishnu"
#     assert expected == name , f"We got {name} but expected is {expected}"

# @pytest.mark.name
# def test_lname():
#     name = "kumar"
#     expected = "kumar"
#     assert expected == name , f"We got {name} but expected is {expected}"

# Learning inbuilt markers
@pytest.mark.skip(reason="We dont need to check as its not implemented")
def test_login():
    user = "Vishnu"
    age = 21
    assert age >= 18 , f"Age should be >= 18 but the users age is {age}"

@pytest.mark.skipif( 5>3, reason="Condition is true")
def test_verify():
    assert True

@pytest.mark.xfail(reason="under development")
def test_calculation():
    val1 = 20
    val2 = 13
    result = val1+val2
    expected = 39
    assert result == expected , f"We should get {expected} but we got {result}"
