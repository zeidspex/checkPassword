#!/usr/bin/env python
# checkPassword.py
# This script checks if a password has been compromised in known data breaches
# It uses the "Have I Been Pwned" API to check the password against a database of compromised passwords.


import requests
import hashlib

class CheckPasswordAPI:
    def __init__(self):
        self.api_url = 'https://api.pwnedpasswords.com/range/'

    def check_password(self, password):
        sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        prefix, suffix = sha1_password[:5], sha1_password[5:]
        url = f"{self.api_url}{prefix}"

        try:
            response = requests.get(url)
            response.raise_for_status()

            hashes = (line.split(':') for line in response.text.splitlines())
            for h, count in hashes:
                if h == suffix:
                    return int(count)
            return 0
        
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Error querying API: {str(e)}")

class CheckPasswordCLI:
    def __init__(self):
        self.checker = CheckPasswordAPI()

    def run(self):
        while True:
            password = input("\nEnter the password to check (or 'q' to quit): ")
            if password.lower() == 'q':
                break
            
            try:
                compromised_count = self.checker.check_password(password)
                if compromised_count > 0:
                    print(f"\nThe password '{password}' has appeared in {compromised_count} data breaches.")
                    print("It is recommended to change this password.")
                else:
                    print(f"\nThe password '{password}' was not found in any known data breaches.")
                    print("The password is safe!")
            except Exception as e:
                print(f"\nAn error occurred during verification: {str(e)}")

def main():
    app = CheckPasswordCLI()
    app.run()

if __name__ == "__main__":
    main()
