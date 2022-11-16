from unittest.mock import patch
from issue5 import what_is_year_now
import json


def test_issue5_1():
    with patch("issue5.urllib.request.urlopen") as mocked_date:
        json.load(mocked_date)['currentDateTime'] = lambda: '2019-03-01'
        assert what_is_year_now() == '2019'


def test_issue5_2():
    with patch("issue5.urllib.request.urlopen") as mocked_date:
        json.load(mocked_date)['currentDateTime'] = lambda: '01.03.2019'
        assert what_is_year_now() == '2019'


def test_issue5_3():
    with patch("issue5.urllib.request.urlopen") as mocked_date:
        json.load(mocked_date)['currentDateTime'] = lambda: '2019/03/01'
        assert what_is_year_now() == '2019'
