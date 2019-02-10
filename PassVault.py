from os import path
from sys import exit
from time import sleep


class cipher():
    def __init__(self, c):
        self.c = c
        lc = len(c)
        self.lc = lc
        # test cipher validity
        if lc == 0:
            self.valid = "no"
        else:
            for i in range(lc):
                if 31 < ord(c[i]) < 127:
                    self.valid = "yes"
                else:
                    self.valid = "no"
                    break

    def key(self):
        if self.valid == "yes":
            # conversion of cipher
            key = ""
            for char in self.c:
                i_c = str(ord(char))
                key = key + i_c
            self.c = key


def check_for_file():
    file_status = path.exists(location)
    return file_status


def file_create(location):
    print("\nNo password file found.\n")
    i = input("Would you like to create a password file?"
              " Enter \"yes\" or \"no\": ")
    if i == "yes":
        with open(location, "w") as openf:
            openf
    else:
        terminate(0.5)


def read_file(location, c):
    file = open(location, "r")
    cipher_text = file.read()
    lr = len(cipher_text)
    text = ""
    # iterate and decrypt cipher_text
    for i in range(lr):
        text_val = ord(cipher_text[i]) - 31
        text_val = text_val + 95 - int(c.c[i % c.lc])
        text_val = text_val % 95 + 31
        text_char = chr(text_val)
        text = f"{text}{text_char}"
    return text


def add_to_file(text, c):
    # iterate and encrypt text
    ln = len(text)
    cipher_text = ""
    for i in range(ln):
        text_val = ord(text[i]) - 31
        text_val = text_val + int(c.c[i % c.lc])
        text_val = text_val % 95 + 31
        text_char = chr(text_val)
        cipher_text = f"{cipher_text}{text_char}"
    # rewrite file with old and new data
    with open(location, "w") as file:
        file.write(cipher_text)


def terminate(t):
    print(
        f"There has been an error. The program will terminate in {t} seconds")
    sleep(t)
    exit()


location = "password"
file_status = check_for_file()
if file_status is False:
    file_create(location)
print("Welcome to PassVault, please enter your cipher.\n")
print("It may be made of numbers, letters or symbols\n")
while True:
    c = input("Enter your cipher: ")
    c = cipher(c)
    if c.valid != "yes":
        print("Invalid cipher. Try another one")
    else:
        break
c.key()
while True:
    unciphered = read_file(location, c)
    print(unciphered)
    request_p = input("Would you like to add more passwords?\n"
                      "Enter any input to quit, or enter \"yes\": ")
    if request_p != "yes":
        exit()
    else:
        account = input("If you have entered \"yes\" by accident,"
                        " exit the program immediately.\n"
                        "Otherwise, enter what account"
                        " you wish to enter a password for: ")
        password = input("Enter password: ")
        unciphered = f"{unciphered}{account}: {password},"
        add_to_file(unciphered, c)
