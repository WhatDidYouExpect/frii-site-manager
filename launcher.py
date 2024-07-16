import subprocess
import sys
import os
#im too lazy the os.system was a last minute thing
os.system("cls")

scripts = {
    "1": {"name": "create-domain.py", "accepts_args": True},
    "2": {"name": "check-domains.py", "accepts_args": False},
    "3": {"name": "update-domain.py", "accepts_args": True},
    "4": {"name": "delete-domain.py", "accepts_args": True},
}

def display_menu():
    print("Choose a script to run:")
    for key, script in scripts.items():
        print(f"{key}). {script['name']} {'(no arguments)' if not script['accepts_args'] else ''}")

def get_user_choice():
    choice = input("Enter the number of the script you want to run: ").strip()
    if choice in scripts:
        return choice
    else:
        print("Not an option buckaroo.")
        return get_user_choice()

def get_arguments(script_name):
    if scripts[script_name]["accepts_args"]:
        args = input(f"Enter the domain for {scripts[script_name]['name']} : ").strip()
        return args.split()
    else:
        return []

def launch_script(script_name, args):
    try:
        if args:
            subprocess.run([sys.executable, scripts[script_name]["name"]] + args)
        else:
            subprocess.run([sys.executable, scripts[script_name]["name"]])
    except Exception as e:
        print(f"X_X: {e}")

if __name__ == "__main__":
    display_menu()
    user_choice = get_user_choice()
    script_args = get_arguments(user_choice)
    os.system("cls")
    launch_script(user_choice, script_args)
