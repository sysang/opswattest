import fire

from opswattest.utils.challenge_1 import find_different_character
from opswattest.utils.challenge_2 import find_domain_ip_adress
from opswattest.utils.challenge_3 import decode_string_matrix


def diff_char(str1, str2):
    return find_different_character(str1, str2)


def decode_matrix(script='', script_file=''):
    return decode_string_matrix(script, script_file)


def domain_ip_adress(name):
    return find_domain_ip_adress(name)


if __name__ == '__main__':
    fire.Fire()
