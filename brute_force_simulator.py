import time

def brute_force(target_password, wordlist):
    start_time = time.time()

    for attempt in wordlist:
        attempt = attempt.strip()

        print(f"Trying: {attempt}")

        if attempt == target_password:
            end_time = time.time()
            print("\nPassword Cracked!")
            print("Password:", attempt)
            print("Time taken:", round(end_time - start_time, 2), "seconds")
            return

    print("\nPassword not found!")

# Load common passwords
with open("common_passwords.txt", "r") as file:
    passwords = file.readlines()

target = input("Enter password to crack: ")
brute_force(target, passwords)