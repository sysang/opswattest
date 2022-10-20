import pytest

from utils.challenge_1 import find_different_character
from utils.challenge_1 import InvalidInputString


@pytest.mark.parametrize(
    "s1,s2,expected", [
        (
            'qwer01234',
            'qwer1234',
            (4, '0'),
        ),
        (
            'qwer1234',
            'qqwer1234',
            (1, 'q'),
        ),
        (
            'aqwer1234',
            'qwer1234',
            (0, 'a'),
        ),
        (
            'qwer12345',
            'qwer1234',
            (8, '5'),
        ),
        (
            'qwer1234',
            'qwer12345',
            (8, '5'),
        ),
    ]
)
def test_find_different_character(s1, s2, expected):

    actual = find_different_character(s1, s2)
    assert actual == expected


    actual = find_different_character(s1, s2)
    assert actual == expected


    actual = find_different_character(s1, s2)
    assert actual == expected


    actual = find_different_character(s1, s2)
    assert actual == expected


    actual = find_different_character(s1, s2)
    assert actual == expected


def test_find_different_character__exception():

    with pytest.raises(InvalidInputString):
        s1 = 'qwer1234'
        s2 = None
        find_different_character(s1, s2)

        s1 = 123
        s2 = 'qwer1234'
        find_different_character(s1, s2)

        s1 = 'QWER1234'
        s2 = 'qwer1234'
        find_different_character(s1, s2)
