import pytest

from one_hot_encoder import fit_transform


def test_1():
    assert fit_transform('cold', 'hot') == [('cold', [0, 1]), ('hot', [1, 0])]


def test_2():
    assert fit_transform('cold', 'hot', 'warm') == [('cold', [0, 0, 1]), ('hot', [0, 1, 0]), ('warm', [1, 0, 0])]


def test_3():
    assert fit_transform('cold', 'hot', 'warm', '1') == [('cold', [0, 0, 0, 1]), ('hot', [0, 0, 1, 0]),
                                                         ('warm', [0, 1, 0, 0]), ('1', [1, 0, 0, 0])]


def test_4():
    with pytest.raises(TypeError):
        fit_transform(100)
