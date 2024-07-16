import requests
import random
import string
import time
import argparse
import os

def read_token_from_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('Token:'):
                return line.split('Token: ')[1].strip()
    return None

token = read_token_from_file('creds.txt')

def get_user_ip():
    response = requests.get('https://api.ipify.org?format=json')
    return response.json()['ip']


def main(domain):
    url = "https://server.frii.site/modify-domain"
    user_ip = get_user_ip()

    payload = {
            "TOKEN": token,
            "domain": domain,
            "ip": user_ip,
            "type": "A"
        }

    response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})

    print("Status Code:", response.status_code)
    print("Response Body:", response.text)
    if response.status_code == 200: {
        print("Domain Updated!")
    }
    else: {
        print("Update Failed....")
    }

    os.system("python check-domains.py")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="mod domain")
    parser.add_argument('domain', type=str, help="gfd")
    args = parser.parse_args()
    main(args.domain)

