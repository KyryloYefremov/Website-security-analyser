from pprint import pprint
from headers_list import HeadersList

import requests


def check_url(url: str) -> dict:
    headers = dict(requests.get(url).headers)
    report = headers_list.check_headers(headers)
    return report


if __name__ == "__main__":
    try:
        headers_list = HeadersList("data/sec_headers.json")
    except FileNotFoundError as e:
        print(e)
        exit(1)
    except ValueError as e:
        print(e)
        exit(1)

    print("Welcome to the Website Security Analyser!")
    input_url = input("Enter the URL: ")

    result = check_url(input_url)
    print(f"Safety score: {result['total_score'] / result['max_score'] * 100}%")
    pprint(result)