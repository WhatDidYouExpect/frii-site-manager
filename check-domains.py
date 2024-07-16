import requests
import json


def read_token_from_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            if line.startswith('Token:'):
                return line.split('Token: ')[1].strip()
    return None

token = read_token_from_file('creds.txt')

url = 'https://server.frii.site/get-domains'
headers = {
    'Content-Type': 'application/json'
}




if token is None:
    print("Token not found in creds.txt, Did you run the setup?")
    exit()


payload = {
    "TOKEN": token
}


response = requests.post(url, data=json.dumps(payload), headers=headers)


if response.status_code == 200:
    data = response.json()
    for name, details in data.items():
        ip = details.get('ip')
        print(f"Name: {name}, IP: {ip}")
else:
    print(f"Error: {response.status_code} - {response.text}")
