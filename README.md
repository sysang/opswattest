# opswattest

## Dependencies

Before checking the challenges please install packages: requests, fire. 
`pip install requests~=2.8.1` 
`pip install fire~=0.4.0` 

## Dev pependencies

Before running tests please install pytest.
`pytest~=7.1.3`

## Challenge 1, find single different character between two strings

Execute command: `python3 main.py diff_char`, for argument description: `python3 main.py diff_char -h`

Example: `python3 main.py diff_char --s1='qwer1234' --s2='qwer12345'`

Output: 
> [8, "5"]

## Challenge 2, find domain ip address

Execute command: `python3 main.py domain_ip_address`, for argument description: `python3 main.py domain_ip_address -h`

Example: `python3 main.py domain_ip_address --qname=www.example.com`

Output: 
> ipv4: [{"address": "93.184.216.34", "TTL": 82569}]
> ipv6: [{"address": "2606:2800:220:1:248:1893:25c8:1946", "TTL": 84179}]

## Challenge 3, decode text matrix

Execute command: `python3 main.py decode_matrix`, for argument description: `python3 main.py decode_matrix -h`

Example 1: 
```
python3 main.py decode_matrix --script="\
15 6
TTTTTT
hhhhhh
iiiiii
ssssss
######
iiiiii
ssssss
$$$$$$
MMMMMM
aaaaaa
tttttt
rrrrrr
iiiiii
xxxxxx
@@@@@@"
```

Output: 
> This is Matrix This is Matrix This is Matrix This is Matrix This is Matrix This is Matrix

Example 2: `python3 main.py decode_matrix --script_file=path/to/text/file`

## Unittest:

At project root run `pytest`

## API References
[Functions](https://github.com/sysang/opswattest/blob/master/docs/build/markdown/index.md)

## Build documentation

Install pip packages: Sphinx, sphinx_markdown_builder, then run `make docs`

