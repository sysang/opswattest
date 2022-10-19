import pytest

from pathlib import Path

from  utils.challenge_3 import decode_string_matrix, MalformedMatrix


happy_case_data = \
"""\
9 3
#%i
!ix
!s#
$! 
T@%
hM&
ia 
st 
$r """

unchanged_case_data = \
"""\
15 6
TTTTTT
hhhhhh
iiiiii
ssssss
      
iiiiii
ssssss
      
MMMMMM
aaaaaa
tttttt
rrrrrr
iiiiii
xxxxxx
      """


one_row_case_data = \
"""\
1 29
%%% This!@#$%%is    Matrix##!"""


@pytest.mark.parametrize(
    "script,expected", [
        (
            happy_case_data,
            "#!!$This is Matrix# %&   ",
        ),
        (
            unchanged_case_data,
            "This is Matrix This is Matrix This is Matrix This is Matrix This is Matrix This is Matrix "
        ),
        (
            one_row_case_data,
            "%%% This is Matrix##!"
        ),
    ])
def test_decode_string_matrix__script(script, expected):
    actual = decode_string_matrix(script)
    assert actual == expected


def test_decode_string_matrix__script_file():
    current_dir = Path(__file__).parent
    data_file = current_dir / 'data/one_column_case_data.txt'

    expected = '!@#This is Matrix#@ $ ! &'
    actual = decode_string_matrix(script_file=data_file.absolute())
    assert actual == expected


unavailable_meta_data_case_1 = \
"""\
#%i
!ix
!s#
$! 
T@%
hM&
ia 
st 
$r """
def test_decode_string_matrix__no_argument():
    with pytest.raises(AssertionError):
        decode_string_matrix()


unavailable_meta_data_case_1 = \
"""\
%s%r
%!ii
%@sx
T#M#
h$a#
i%t!"""

unavailable_meta_data_case_2 = \
"""\
6 4 4
%s%r
%!ii
%@sx
T#M#
h$a#
i%t!"""

unavailable_meta_data_case_3 = \
"""\
6 4 ab
%s%r
%!ii
%@sx
T#M#
h$a#
i%t!"""

unavailable_meta_data_case_4 = \
"""\
6
%s%r
%!ii
%@sx
T#M#
h$a#
i%t!"""

unavailable_meta_data_case_5 = \
"""\
6 5
%s%r
%!ii
%@sx
T#M#
h$a#
i%t!"""

unavailable_meta_data_case_6 = \
"""\
7 4
%s%r
%!ii
%@sx
T#M#
h$a#
i%t!"""

invalid_characters_data_case = \
"""\
6 4
(s%r
)!ii
%@sx
T#M#
h$a#
i%t!"""

@pytest.mark.parametrize(
    "script", [
        unavailable_meta_data_case_1,
        unavailable_meta_data_case_2,
        unavailable_meta_data_case_3,
        unavailable_meta_data_case_4,
        unavailable_meta_data_case_5,
        unavailable_meta_data_case_6,
        invalid_characters_data_case,
    ])
def test_decode_string_matrix__exception(script):
    with pytest.raises(MalformedMatrix):
        decode_string_matrix(script)
