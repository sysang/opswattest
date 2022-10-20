import math
import random
import string

from typing import Tuple


SUPPORTED_CHARACTER = string.ascii_lowercase + string.digits
char_table = { c:True for c in SUPPORTED_CHARACTER }

class InvalidInputString(Exception):
    pass


def _checkif_characters_valid(string_seq: str) -> bool:
    for char in string_seq:
        if not char_table.get(char, None):
            return False

    return True


def find_different_character(s1: str, s2: str) -> Tuple[int, str]:
    """
    Find the single different char between two input strings

    Args:
        s1 (str): input string for comparison, contains only lowercase ascii letters and digits
        s2 (str): input string for comparison, contains only lowercase ascii letters and digits

    Returns:
        Tuple[int, str]: different sequence index, different character


    Raises:
        InvalidInputString:
            inputs are not string,
            input string contains any character other than lowercase ascii letters and digits
    """

    if not isinstance(s1, str) or not isinstance(s2, str):
        raise InvalidInputString("Input is not string.")

    if not _checkif_characters_valid(s1) or not _checkif_characters_valid(s2):
        raise InvalidInputString('Input string contains any character other than lowercase ascii letters and digits.')

    probe = s1 if len(s1) > len(s2) else s2
    probe_size = len(probe)

    for i in range(probe_size - 1):
        if s1[i] != s2[i]:
            return (i, probe[i])

    return (probe_size - 1, probe[-1])
