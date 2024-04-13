import hashlib
import requests

def check_password_strength(password):
    # Hash the password using SHA-1 algorithm
    password_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = password_hash[:5], password_hash[5:]
    
    # Send a request to the Have I Been Pwned API
    url = 'https://api.pwnedpasswords.com/range/' + prefix
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Extract the list of suffixes (hashes) from the response
        suffixes = (line.split(':') for line in response.text.splitlines())
        # Check if the password suffix exists in the response
        for suf, count in suffixes:
            if suf == suffix:
                # If the password suffix exists, return the number of times it has been pwned
                return int(count)
        # If the password suffix does not exist, return 0
        return 0
    else:
        # If the request was not successful, raise an exception
        raise Exception('Error fetching data from API')

def main():
    password = input("Enter your password: ")
    count = check_password_strength(password)
    if count > 0:
        print(f"The password '{password}' has been pwned {count} times. Please choose a stronger password.")
    else:
        print(f"The password '{password}' has not been pwned. You can use it, but consider making it stronger.")

if __name__ == "__main__":
    main()
