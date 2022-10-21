<!-- opswattest documentation master file, created by
sphinx-quickstart on Wed Oct 19 18:49:24 2022.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
# opswattest documentation!


### utils.challenge_1.find_different_character(s1: str, s2: str)
Find the single different char between two input strings


* **Parameters**

    
    * **s1** (*str*) – input string for comparison, contains only lowercase ascii letters and digits


    * **s2** (*str*) – input string for comparison, contains only lowercase ascii letters and digits



* **Returns**

    different sequence index, different character



* **Return type**

    Tuple[int, str]



* **Raises**

    **InvalidInputString** – inputs are not string,
        input string contains any character other than lowercase ascii letters and digits



### utils.challenge_2.find_domain_ip_adress(qname: str)
Find IP adresses of give domain name


* **Parameters**

    **qname** (*str*) – domain name



* **Returns**

    list of ip adresses keyed by ipv4, ipv6



* **Return type**

    dict



* **Raises**

    **InvalidDomainName** – 



### utils.challenge_3.decode_string_matrix(script: str = '', script_file: Optional[TextIO] = None)
Decode text as string matrix. Replace symbols or spaces between two alphanumeric characters.


* **Parameters**

    
    * **script** (*str*) – multi line string as matrix data


    * **script_file** (*Union**[**TextIO**, **None**]*) – text file that contains matrix data



* **Returns**

    decoded string



* **Return type**

    str



* **Raises**

    **MalformedMatrix** – unvailable row/column medatata,
        matrix data and its meta data are not matched together,
        matrix contains unsupported character,


### Example

Input:

    7 3
    Tsi
    h%x
    i#
    sM
    $a
    #t%
    ir!

Output:

    This is Matrix#  %!
