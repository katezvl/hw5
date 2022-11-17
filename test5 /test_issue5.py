from unittest.mock import patch
from what_is_year_now import what_is_year_now
from io import StringIO


def test_issue5_1():
    with patch('urllib.request.urlopen', return_value=StringIO('{"currentDateTime": "2022-02-02T12:52Z"}')):
        assert what_is_year_now() == 2022


def test_issue5_2():
    with patch('urllib.request.urlopen', return_value=StringIO('{"currentDateTime": "02.02.2022T12:52Z"}')):
        assert what_is_year_now() == 2022


def test_issue5_3():
    with patch('urllib.request.urlopen', return_value=StringIO('{"currentDateTime": "2022/02/02T12:52Z"}')):
        assert what_is_year_now() == 2022
