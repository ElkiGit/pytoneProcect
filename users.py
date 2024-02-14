import os
import random
import re


# Task 1: Check if file exists, if not, create one in a subfolder
def check_file(file_path):
    if not os.path.exists(file_path):
        dir_name = os.path.dirname(file_path)
        print(dir_name)
        if dir_name == '':
            dir_name = "users"
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)
        print(dir_name + '/' + os.path.basename(file_path))
        with open(dir_name + '/' + os.path.basename(file_path), 'w') as file:
            file.write("")


# Task 2: Read usernames from file into a generator
def read_usernames_generator():
    check_file("UsersName.txt")
    with open("UsersName.txt", 'r') as file:
        for line in file:
            yield line.strip()


# Task 3: Read usernames into an array
def read_usernames_array():
    usernames = []
    for username in read_usernames_generator():
        usernames.append(username)
    return usernames


# skip first 10%
def skip_10_precents():
    usernames = read_usernames_array()
    num_to_skip = int(len(usernames) * 0.1)
    return usernames[num_to_skip:]


# Task 4: Implement function for users of even rows
def even_usernames():
    usernames = read_usernames_array()
    return [username for i, username in enumerate(usernames) if i % 2 == 0]


# Task 5: Read email addresses and addresses, check correctness
def check_email_addresses():
    check_file("UsersEmail.txt")
    with open("UsersEmail.txt", 'r') as file:
        for line in file:
            email = line.strip()
            if not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
                print(f"Invalid email address: {email}")


# Task 6: Function to return Gmail email addresses only
def get_gmail_addresses():
    check_file("UsersEmail.txt")
    gmail_addresses = []
    with open("UsersEmail.txt", 'r') as file:
        for line in file:
            email = line.strip()
            if email.endswith('@gmail.com'):
                gmail_addresses.append(email)
    return gmail_addresses


# Task 7: Check if email username matches the username from list
def check_email_username_match():
    check_file("UsersEmail.txt")
    check_file("UsersName.txt")
    email_username_match = {}
    with open("UsersEmail.txt", 'r') as emails, open("UsersName.txt", 'r') as usernames:
        for email, username in zip(emails, usernames):
            email_username_match[email.strip()] = username.strip() in email.strip().split('@')[0]
    return email_username_match


# Task 8: Check if user is in the list and modify name
def check_username_in_file(name):
    check_file("UsersName.txt")
    count = 0
    with open("UsersName.txt", 'r') as file:
        for line in file:
            username = line.strip()
            if name == username:
                count += 1
    if count == 0:
        print("Name not found in the file")
    else:
        print("Name found in the file")
    # Convert to ASCII code
    ascii_code = [ord(char) for char in name]
    print("ascii code:", ascii_code)

    # Convert to hexadecimal
    print("hex string:", ''.join([hex(ord(char))[2:] for char in name]))

    # Convert back to string from ASCII code
    print("converted string:", ''.join([chr(code) for code in ascii_code]))

    # Check for the letter 'A' in the name
    letter_count = name.lower().count('a')
    print("Number of 'A' letters in the name:", letter_count)


# Task 9: Capitalize all names in the list
def capitalize_usernames():
    check_file("UsersName.txt")
    with open("UsersName.txt", 'r') as file:
        usernames = [line.strip() for line in file]
    return all(name[0].isupper() for name in usernames)


# Task 10: Calculate earnings from customer groups
def calculate_earnings(customers_list):
    total_earnings = 0
    for customer_count in customers_list:
        total_earnings += (customer_count // 8) * 200 + (customer_count % 8) * 50
    return total_earnings


if __name__ == '__main__':
    check_file("folder/file")
    for username in read_usernames_generator():
        print(username)
    print(read_usernames_array())
    print(skip_10_precents())
    print(even_usernames())
    check_email_addresses()
    print(get_gmail_addresses())
    print(check_email_username_match())
    check_username_in_file("Bracha")
    print(capitalize_usernames())
    print(calculate_earnings([9, 5, 19, 43, 4, 88, 76, 20, 15]))

