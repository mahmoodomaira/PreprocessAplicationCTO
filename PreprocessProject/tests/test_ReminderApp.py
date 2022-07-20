import pytest
import datetime
from scripts.ReminderApp import difference_in_second, reminder, enter_dates_in_lists

@pytest.mark.parametrize("date,expected",[[datetime.datetime(2022,7,18,20,15,00),900]])
def test_difference_in_second(date,expected,mocker):
    mock_now = mocker.patch("scripts.ReminderApp.datetime")
    mock_now.now.return_value = datetime.datetime(2022,7,18,20,00,00)
    assert difference_in_second(date)==expected


@pytest.mark.parametrize("date_time_list,expected",[[[datetime.datetime(2022,7,18,20,15,00)],'The 1 date has been reached! 2022-07-18 20:15:00\n']])
def test_reminder(date_time_list,expected,mocker,capfd):
    mocker.patch("scripts.ReminderApp.difference_in_second",return_value=1)
    mocker.patch("scripts.ReminderApp.time.sleep",return_value=None)
    reminder(date_time_list)
    out, err = capfd.readouterr()
    assert out == expected
    
