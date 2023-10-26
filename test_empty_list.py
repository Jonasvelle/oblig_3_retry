import pytest
from main import isLeapYear

@pytest.fixture(params=[2000, 2004, 2028])
def leap_years(request):
    return request.param


def test_leap_years(leap_years):
    result = isLeapYear(leap_years)
    assert result == True, f"Year {leap_years} should be a leap year."

if __name__== "main":
    pytest.main()