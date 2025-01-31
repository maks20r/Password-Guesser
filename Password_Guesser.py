import itertools
import string
import time
from datetime import timedelta


correct_password = "abcdef" 

def check_password(password):
    """Check if the given password is correct."""
    return password == correct_password


def generate_passwords(length):
    """Generate all possible passwords of a given length."""
    characters = string.ascii_lowercase + string.digits + string.punctuation  
    for password in itertools.product(characters, repeat=length):
        yield ''.join(password)

def brute_force_password():
    """Run the brute-force attack until the correct password is found."""
    start_time = time.time()
    length = 1
    attempts = 0
    while True:
        for password in generate_passwords(length):
            attempts += 1
            if attempts % 1000 == 0: 
                print(f"\rTrying password length {length} | Attempts: {attempts}", end="", flush=True)
            if check_password(password):
                end_time = time.time()
                elapsed_time = end_time - start_time
                return password, attempts, elapsed_time
        length += 1

found_password, attempts, elapsed_time = brute_force_password()
elapsed_time_str = str(timedelta(seconds=elapsed_time))
print(f"\nThe correct password is: {found_password}")
print(f"Total attempts: {attempts}")
print(f"Time taken: {elapsed_time_str}")
