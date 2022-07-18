import pytest
import datetime
from ReminderApp import difference_in_second

@pytest.mark.parametrize("date,expected",[[datetime.datetime(2022,7,18,20,15,00),400]])
def test_difference_in_second(date,expected,mocker):
    mock_now = mocker.patch("datetime.datetime")
    mocknow.now.return_value = datetime(2022,7,18,20,0,0)
    assert difference_in_second()==expected
    


