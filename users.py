import os
import random
import re

# Task 1: Check if file exists, if not, create one in a subfolder
def check_file(file_path):
    if not os.path.exists(file_path):
        os.makedirs(os.path.dirname(file_path))
        with open(file_path, 'w') as file:
            file.write("")

# Task 2: Read usernames from file into a generator
def read_usernames_generator(file_path):
    check_file(file_path)
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

# Task 3: Read usernames into an array, skip first 10%
def read_usernames_array(file_path):
    check_file(file_path)
    with open(file_path, 'r') as file:
        usernames = [line.strip() for line in file]
    num_to_skip = int(len(usernames) * 0.1)
    return usernames[num_to_skip:]

# Task 4: Implement function for users of even rows
def even_usernames(file_path):
    usernames = read_usernames_array(file_path)
    return [username for i, username in enumerate(usernames) if i % 2 == 0]

# Task 5: Read email addresses and addresses, check correctness
def check_email_addresses(file_path):
    check_file(file_path)
    with open(file_path, 'r') as file:
        for line in file:
            email, address = line.strip().split(',')
            if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                print(f"Invalid email address: {email}")
            # Additional checks for address if needed

# Task 6: Function to return Gmail email addresses only
def get_gmail_addresses(file_path):
    check_file(file_path)
    gmail_addresses = []
    with open(file_path, 'r') as file:
        for line in file:
            email, _ = line.strip().split(',')
            if email.endswith('@gmail.com'):
                gmail_addresses.append(email)
    return gmail_addresses

# Task 7: Check if email username matches the username from list
def check_email_username_match(emails_file, usernames_file):
    check_file(emails_file)
    check_file(usernames_file)
    email_username_match = {}
    with open(emails_file, 'r') as emails, open(usernames_file, 'r') as usernames:
        for email, username in zip(emails, usernames):
            email_username_match[email.strip()] = email.strip().split('@')[0] == username.strip()
    return email_username_match

# Task 8: Check if user is in the list and modify name
def check_user_in_list(username, usernames_file):
    check_file(usernames_file)
    with open(usernames_file, 'r') as file:
        usernames = [line.strip() for line in file]
    if username in usernames:
        # Change name format
        modified_name = ''.join([chr(ord(char) + 1) for char in username])
        # Check if modified name contains 'A'
        return 'A' in modified_name
    return False

# Task 9: Capitalize all names in the list
def capitalize_usernames(usernames_file):
    check_file(usernames_file)
    with open(usernames_file, 'r') as file:
        usernames = [line.strip().upper() for line in file]
    return usernames

# Task 10: Calculate earnings from customer groups
def calculate_earnings(customers_list):
    total_earnings = 0
    for customer_count in customers_list:
        if customer_count % 8 == 0:
            total_earnings += 200
        else:
            total_earnings += 200 + 50 * (customer_count % 8)
    return total_earnings

