import pytest

from utils.challenge_2 import find_domain_ip_adress
from utils.challenge_2 import InvalidDomainName


def test_find_domain_ip_adress():
    name = 'www.example.com'

    expected = {
        "ipv4": [{"address": "93.184.216.34"}],
        "ipv6": [{"address": "2606:2800:220:1:248:1893:25c8:1946"}],
    }
    actual = find_domain_ip_adress(name)

    assert actual['ipv4'][0]['address'] == expected['ipv4'][0]['address']
    assert actual['ipv6'][0]['address'] == expected['ipv6'][0]['address']


def test_find_domain_ip_adress_exception():
    with pytest.raises(InvalidDomainName):
        find_domain_ip_adress('')

    with pytest.raises(InvalidDomainName):
        find_domain_ip_adress(None)
