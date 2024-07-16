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

def main(domain):
    url = "https://server.frii.site/delete-domain"

    payload = {
            "TOKEN": token,
            "domain": domain,
        }

        # send the post request
    response = requests.post(url, json=payload, headers={"Content-Type": "application/json"})

        # check if it worked or got rate-limited
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="mods a domain")
    parser.add_argument('domain', type=str, help="kill me")
    args = parser.parse_args()
    print("WARNING!!")
    time.sleep(1)
    print("DELETEING A DOMAIN IS PERMENENT AND CANNOT BE UNDONE!")
    time.sleep(5)
    main(args.domain)
