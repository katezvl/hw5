from morse import decode
import pytest


@pytest.mark.parametrize("test_input,expected", [('.....', '5'), ('... --- ...', 'SOS'), ('.- -... -.-.', 'ABC')])
def test_decode(test_input, expected):
    assert decode(test_input) == expected
