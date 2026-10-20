import pytest

@pytest.mark.parametrize("a,b,expected",[(10,20,40),(12,8,20),(5,3,8)])
def test_add(a,b,expected):
    result = a + b
    assert expected == result, f"Expected value does not matches with the result"

