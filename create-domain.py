import requests
import random
import string
import time
import argparse

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
    url = "https://server.frii.site/register-domain"
    user_ip = get_user_ip()

    payload = {
            "TOKEN": token,
            "domain": domain,
            "ip": user_ip,
            "type": "A"
        }

        # send the post request
    response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})

        # check if it worked or got rate-limited
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Modify domain with user's IP")
    parser.add_argument('domain', type=str, help="Domain to be modified")
    args = parser.parse_args()
    main(args.domain)
