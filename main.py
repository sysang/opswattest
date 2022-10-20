import fire

from opswattest.utils.challenge_3 import decode_string_matrix


def decode_matrix(script='', script_file=''):
    return decode_string_matrix(script, script_file)


if __name__ == '__main__':
    fire.Fire()
