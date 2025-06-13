# checkPassword

`checkPassword` is a command line tool developed in Python that allows you to check if a password has been compromised against known databases of leaked passwords. Use Have I Been Pwned's Pwned Passwords API to perform this verification safely and efficiently.

## Features

### Verification of Compromised Passwords:

Enter a password to check if it has appeared in known leaks.

It uses a secure hashing technique to protect password privacy during verification.

## Command Line Interface (CLI):

Friendly interaction with the user through the terminal.

Displays warning messages if the password is compromised and recommendations to change it.

## Security and Privacy:

Verification is performed without sending the full password over the network.

Only a portion of the SHA-1 hash of the password is sent to match the compromised password database.

## Requirements:

Make sure you have `Python3` installed on your system.

## Execution:

To verify a password, simply run:

```bash
python3 checkPassword.py
```

## Installation:
1. Clone the repository:
2. Copy script into your bin directory.

```bash
sudo cp checkPassword.py /usr/bin/checkPassword
```
## Info:

```bash
Enter the password to verify (or 'q' to exit): secret123

The password 'secret123' has not been compromised in known databases.
The password is secure!
```

## Credits:

Developed by `@d1se0` - [GitHub Profile Link](https://github.com/D1se0)
Translated to English and Cleaned by Zaid Marji
