import requests
import hashlib
import os
import subprocess
import time

os.system("cls")
login_url = 'https://server.frii.site/login'
user_info_url = 'https://server.frii.site/get-user-info'

def hash_credentials(username, password):
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    hashed_username = hashlib.sha256(username.encode('utf-8')).hexdigest()
    return f"{hashed_password}|{hashed_username}"

username = input("Enter your username: ")
password = input("Enter your password: ")

hashed_token = hash_credentials(username, password)

login_payload = {
    'TOKEN': hashed_token
}

login_response = requests.post(login_url, json=login_payload)

if login_response.status_code == 200:

    user_info_payload = {
        'TOKEN': hashed_token
    }
    
    user_info_response = requests.post(user_info_url, json=user_info_payload)

    if user_info_response.status_code == 200:
        try:

            user_info = user_info_response.json()
            email = user_info.get('email')
            
            if email:

                username_part = email.split('@')[0]
                print(f"Hello {username_part}!")
                with open('creds.txt', 'w') as f:
                    f.write(f'Token: {hashed_token}\n')
                time.sleep(1)
                subprocess.run(['python3', 'main.py'])
            else:
                print("Email not found in user info response.")
        except ValueError:
            print("Failed to parse user info response as JSON.")
    else:
        print(f"Failed to get user info. Status code: {user_info_response.status_code}")
else:
    print(f"Login failed. Status code: {login_response.status_code}")
