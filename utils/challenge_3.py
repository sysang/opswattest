import re
import string

from typing import TextIO, Union, Tuple, List


SUPPORTED_CHARACTER = string.ascii_letters + string.digits + '!@#$%&' + ' '
char_table = { c:True for c in SUPPORTED_CHARACTER }


class MalformedMatrix(Exception):
    pass


def _regex_replace_symbols(match):
    groups = match.groups()

    return groups[0] + ' ' + groups[2]


def parse_volume(text: str) ->  Tuple[int]:
    # matching only 2 numbers and arbitrary spaces in between
    p = re.compile(r'\s*(\d+)\s+(\d+)\s*')

    m = p.fullmatch(text)

    if m:
        row_num, col_num = m.groups()

        return int(row_num), int(col_num)

    raise MalformedMatrix(f'Unavailable row/column numbers, first line: {text}')


def checkif_data_sufficient(lines: List[str], row_num: str, col_num: str) -> bool:

    if len(lines) < row_num + 1:
        return False

    return all([ len(line) >= col_num for line in lines[1:] ])


def checkif_characters_valid(string_seq: List[str]) -> bool:
    for char in string_seq:
        if not char_table.get(char, None):
            print(char)
            return False

    return True


def decode_string_matrix(
    script: str = '',
    script_file: Union[TextIO, None] = None
) -> str:

    assert script or script_file, 'Script or script file is required.'

    if script:
        lines = script.splitlines()
    else:
        with open(script_file) as fd:
            lines = fd.readlines()

    row_num, col_num = parse_volume(lines[0])

    if not checkif_data_sufficient(lines, row_num, col_num):
        raise MalformedMatrix(f'Matrix data and its meta data are not match together. Meta data -> row number: {row_num}, column number: {col_num}')

    string_seq = [''] * row_num * col_num

    for row_idx, line_content in enumerate(lines[1:row_num + 1]):
        for col_idx in range(col_num):
            idx = row_idx + col_idx * row_num
            string_seq[idx] = line_content[col_idx]

    if not checkif_characters_valid(string_seq):
        raise MalformedMatrix(f'Maxtrix contains invalid character.')

    strseq = ''.join(string_seq)

    p = re.compile(r'([a-zA-Z0-9])([\!\@\#\$\%\&\s]+)([a-zA-Z0-9])')

    return  p.sub(_regex_replace_symbols, strseq)
