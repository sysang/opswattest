import fire

from opswattest.utils.challenge_1 import find_different_character
from opswattest.utils.challenge_3 import decode_string_matrix


def find_diff_char(str1, str2):
    return find_different_character(str1, str2)


def decode_matrix(script='', script_file=''):
    return decode_string_matrix(script, script_file)


if __name__ == '__main__':
    fire.Fire()
