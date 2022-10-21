import contextlib
import requests

from typing import List, Dict
from collections import defaultdict


class InvalidDomainName(Exception):
    pass


def find_domain_ip_adress(qname: str) -> Dict[str, List[Dict[str, str]]]:
    """
    Find IP adresses of give domain name

    Args:
        qname (str): domain name

    Returns:
        dict: list of ip adresses keyed by ipv4, ipv6

    Raises:
        InvalidDomainName
    """
    if not qname:
        raise InvalidDomainName

    ns = '1.1.1.1/dns-query'
    qtypes = {
        'ipv4': 'A',
        'ipv6': 'AAAA',
    }
    headers = {
        "accept": "application/dns-json"
    }
    params = {
        'ns': ns,
        'qname': qname,
    }
    base_url = "https://{ns}?name={qname}&type={qtype}"

    result = defaultdict(list)

    with contextlib.ExitStack() as stack:
        session = stack.enter_context(requests.sessions.Session())

        for iptype, qtype in qtypes.items():
            params.update({ 'qtype': qtype})
            url = base_url.format(**params)

            response = session.get(url, headers=headers)

            if response.status_code < 200 or response.status_code > 299:
                raise ValueError('{} responded with status code {}'
                                '\nResponse body: {}'.format(url,
                                                            response.status_code,
                                                            response.content))

            data = response.json()
            answers = data.get('Answer')
            if answers and isinstance(answers, list):
                for answer in answers:
                    address = answer.get('data')
                    ttl = answer.get('TTL')
                    result[iptype].append({
                        'address': address,
                        'TTL': ttl
                    })

    return result
